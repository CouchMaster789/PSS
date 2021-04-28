"""
Concatenation is processed in three steps, each step feeds into the next:

1) parse_text: text is parsed to generate a list of words

2) parse_words: words are parsed and converted into a list of phoneme tokens

3) generate_audio: audio is generated based on the list of phonemes
"""
import os
import random
import string
import subprocess

from flask import current_app
from flask_login import current_user

from app import create_app
from app.main.models import Phoneme


class UnknownWordError(Exception):
    pass


class MissingPhonemeError(Exception):
    pass


class MissingPhonemeRecordingError(Exception):
    def __init__(self, phoneme):
        self.phoneme = phoneme
        super().__init__(f"Phoneme recording missing for {phoneme.symbol}!")


# punctuation either takes a small pause or a long pause
small_punctuation = [",", "'", "\"", "(", ")", "-", ";", ":"]
long_punctuation = [".", "?", "!"]
punctuation = {
    " ": " ",
    **{punctuation: "  " for punctuation in small_punctuation},
    **{punctuation: "   " for punctuation in long_punctuation}
}


def parse_text(text):
    """
    raw text is passed in here and parsed into a list of words and spaces

    Notes:
    - spaces are represented by an empty list item
    """

    words = []

    for word in " ".join(text.split()).split(" "):
        punctuation_items = set(word) & set(punctuation.keys())
        punctuation_space = ""

        for punctuation_item in punctuation_items:
            word = word.replace(punctuation_item, "")
            punctuation_space = punctuation[punctuation_item]

        words.append(word.lower())

        if punctuation_space:
            words.append(punctuation_space)
        else:
            words.append(" ")

    return words[:-1]  # remove redundant final space


def parse_words(words):
    """
    word list is parsed and converted into a list of phonemes

    Notes:
    - spaces are represented by an empty list item
    """

    phonemes = []

    for word in words:
        if word in punctuation.values():
            phonemes.append(word)  # add space until the last word
        else:
            try:
                for phoneme in current_app.phoneme_map[word]:
                    phonemes.append(phoneme)
            except KeyError:
                raise UnknownWordError()

    return phonemes


def generate_audio(phonemes):
    """
    returns file address for generated audio
    """

    print(phonemes)

    # get users' phoneme recordings
    phoneme_recordings = {}
    for phoneme_needed in set(phonemes) - {" ", "  ", "   "}:
        phoneme = Phoneme.query.filter_by(symbol=phoneme_needed).first()
        if not phoneme:
            raise MissingPhonemeError()

        if phoneme.id not in current_user.phoneme_recordings:
            raise MissingPhonemeRecordingError(phoneme)

        local_address = current_user.phoneme_recordings[phoneme.id].local_address
        phoneme_recordings[phoneme_needed] = os.path.join(current_app.config.get("USER_DIR"), local_address).replace(
            "\\", "/")

    # setup concatenation command for actual recordings (ie minus the spaces)
    inputs_str = " ".join([f"-i \"{phoneme_recordings[phoneme]}\""
                           for phoneme in phonemes
                           if phoneme not in punctuation.values()])

    if len(phonemes) > 1:
        filter_str, filter_counter, recording_counter = "", 1, 0
        padding_lengths = {" ": 7000, "  ": 10000, "   ": 15000}
        for index in range(len(phonemes) - 1):
            if phonemes[index + 1] in punctuation.values():
                filter_str += f"[a{filter_counter - 1:02}]" if index > 0 else f"[{recording_counter}]"
                filter_str += f"apad=pad_len=8000"
                filter_str += f"[a{filter_counter:02}];"
            else:
                filter_str += f"[{0 if index == 0 else f'a{filter_counter - 1:02}'}]" \
                              f"[{1 if index == 0 else recording_counter}]"

                apad = padding_lengths[phonemes[index + 1]] if phonemes[index + 1] in padding_lengths else 2000
                filter_str += f"acrossfade=ns=2500:c1=esin:c2=esin, apad=pad_len={apad}"

                if index < len(phonemes) - 2:
                    filter_str += f"[a{filter_counter:02}];"

                recording_counter += 1
            recording_counter += 1 if index == 0 else 0
            filter_counter += 1

        filter_str += ", atempo=0.9"

        print(filter_str)

        filter_str = "-filter_complex \"" + filter_str + "\""
    else:
        filter_str = ""

    output_dir = os.path.join(current_app.config.get("USER_DIR"), current_user.relative_output_dir)
    output_filename = ''.join(random.choices(string.ascii_letters + string.digits, k=16)) \
                      + f".{current_app.config.get('AUDIO_FILE_EXT')}"
    output_rel = os.path.join(current_user.relative_output_dir, output_filename)
    output_abs = os.path.join(output_dir, output_filename).replace("\\", "/")

    current_user.ensure_dir_is_built()
    execute_str = f"ffmpeg {inputs_str} {filter_str} \"{output_abs}\" -hide_banner -loglevel error"

    # print("\n")
    # print(execute_str)

    subprocess.call(execute_str)

    return {
        "relative_address": output_rel,
        "absolute_address": output_abs
    }


def tts(input_text):
    words = parse_text(input_text)
    phonemes = parse_words(words)
    return phonemes, generate_audio(phonemes)


if __name__ == '__main__':
    # Tests

    with create_app(skip_dir_building=True).app_context():
        # tts("you")
        tts("how are you doing today")
