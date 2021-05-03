import base64
import binascii
import datetime
import hashlib
import logging
import os
import subprocess

from flask import current_app, render_template, Blueprint, jsonify, request, send_from_directory
from flask_login import current_user
from flask_user import login_required

from app import db
from app.main.concatenator import tts, MissingPhonemeError, MissingPhonemeRecordingError, UnknownWordError
from app.main.models import PhonemeRecording, Phoneme

bp = Blueprint('main', __name__, url_prefix="/")


@bp.route('/synthesiser', methods=["GET", "POST"])
@login_required
def synthesiser():
    if request.method == "GET":
        return render_template("main/synthesiser.html")

    text_input = request.form.get("text_input", "", str)
    if not text_input:
        return jsonify({"msg": "Text cannot be empty!"}), 400

    try:
        phonemes, file_addresses = tts(text_input)
    except UnknownWordError as error_word:
        print(error_word)
        return jsonify({"code": 1, "msg": f"Unknown word provided!<br>{error_word}<br>"
                                          "Please only use words found in the Oxford Dictionary"}), 400
    except MissingPhonemeError:
        return jsonify({"code": 1, "msg": "Unknown phoneme identified!"}), 400
    except MissingPhonemeRecordingError as error:
        return jsonify({"code": 2, "msg": str(error), "phoneme_id": error.phoneme.id,
                        "symbol": error.phoneme.symbol}), 400

    relative_address = file_addresses["relative_address"]

    return jsonify({"text_input": text_input, "file": relative_address, "phonemes": phonemes}), 200


@bp.route('/concatenation_setup')
@login_required
def concatenation_setup():
    phonemes = Phoneme.query.all()
    return render_template("main/concatenation_setup.html", phonemes=phonemes)


@bp.route("/save_recording", methods=["POST"])
@login_required
def save_recording():
    """saves the provided phoneme recording audio stream into the users' personal directory under a random name"""

    phoneme_id = request.form.get("phoneme_id", 0, int)
    phoneme = Phoneme.query.filter_by(id=phoneme_id).first()

    if not phoneme:
        return jsonify({"msg": "Unknown phoneme id supplied!"}), 400

    # random name is to prevent caching issues when re-recording a phoneme
    random_name = hashlib.md5(str(datetime.datetime.utcnow()).encode('utf-8')).hexdigest().lower()
    file_name = f"{random_name}.{current_app.config.get('AUDIO_FILE_EXT')}"
    file_relative_address = current_user.relative_recording_dir
    file_address = os.path.join(current_app.config.get("USER_DIR"), file_relative_address, file_name)

    try:
        audio_stream = request.form.get("audio", "", str)
        audio_stream = audio_stream.replace(f"data:{current_app.config.get('AUDIO_MIME_TYPE')};base64,", "")
        audio_binary = base64.decodebytes(audio_stream.encode("utf-8"))

        current_user.ensure_dir_is_built()
        with open(file_address + ".temp", "wb") as file:
            file.write(audio_binary)

    except (OSError, binascii.Error):
        return jsonify({"msg": "Recording could not be saved successfully!"}), 400

    # crop audio cmd
    trim_start = request.form.get("start", 0, float)
    trim_end = request.form.get("end", 1, float)
    trim_cmd = f"-ss {trim_start:.2f} -to {trim_end:.2f}"

    # increase volume cmd for quiet phonemes [k]
    volume_cmd = f"-filter:a 'volume=2'" if phoneme_id in [16] else ""

    # subprocess.run(["ls", "/var/app/current/app/"])
    print(file_address)
    print(os.getcwd())
    logging.info(os.getcwd())
    subprocess.call(f"ffmpeg -i \"{file_address}.temp\" {trim_cmd} -c copy \"{file_address}\" -y {volume_cmd} "
                    f"-hide_banner -loglevel verbose")

    os.remove(file_address + ".temp")

    # delete old recording if exists
    if phoneme_id in current_user.phoneme_recordings:
        try:
            os.remove(os.path.join(current_app.config["USER_DIR"],
                                   current_user.phoneme_recordings[phoneme_id].local_address))
        except FileNotFoundError:
            pass
        db.session.delete(current_user.phoneme_recordings[phoneme_id])

    current_user.phoneme_recording_objects.append(PhonemeRecording(file_relative_address, file_name, phoneme_id))

    db.session.commit()

    return jsonify({"msg": "Recording successfully saved!"}), 200


@bp.route("user_data/<path:filename>")
@login_required
def user_data(filename):
    relative_address_parts = filename.split("/")
    if len(relative_address_parts) <= 2:
        return jsonify({"msg": "invalid file path"}), 400

    if "\\".join(relative_address_parts[:2]) != current_user.user_secure_dir:
        return jsonify({
            "msg": "Authorisation error! Attempt to access directory potentially belonging to another user!"
        }), 403

    return send_from_directory(current_app.config["USER_DIR"], filename)
