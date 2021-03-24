"""
I have prepared simple examples of words that easily display how to pronounce a phoneme

words are in lower case with the letter(s) representing the phoneme in upper case
"""

phoneme_words = {
    "ˌɛ": ["tEchnological", "outlEt", "handhEld", "watershEd", "Entertain", "documEnted"],
    "ð": ["moTHer", "boTher", "raTHer", "cloTHing", "smooTH", "THose"],
    "ˌʊ": ["outpUt", "handbOOk", "mUmbai", "childhOOd", "gOOdbye", "hollywOOd"],
    "t": ["Tanks", "prompT", "inTake", "moTors", "daTE", "aTTempTed"],
    "ˌɑː": ["bookmARks", "radAR", "photogrAphs", "courtyARd", "moustAche", "paragrAphs"],
    "aʊ": ["fOUndation", "handOUt", "sOUthampton", "accOUntability"],
    "eɪ": ["purEE", "foyER", "detAIl", "trAIn", "berET", "cafE"],
    "ˈaɪ": ["brIde", "Ivy", "vIral", "shY", "mIld", "prIce"],
    "v": ["eVil", "surViVal", "motiVated", "Veto", "preView", "saVe"],
    "ˌeɪ": ["donAte", "fAce", "calculAte", "overtAke", "anywAY", "operAte"],
    "ˌuː": ["bathrOOms", "andrEWs", "constitUte", "revenUEs", "intervIEWs", "residUE"],
    "ɔɪ": ["convOY", "andrOId", "explOItation", "cOYote", "envOY"],
    "ˈʊ": ["cOOked", "shOULd", "wOman", "cUshion", "brOOk", "bUlly"],
    "ˈæ": ["pAd", "adApters", "Acid", "Acts", "pAnda", "flAts"],
    "ˌəʊ": ["downlOAding", "borrOWed", "hormOne", "envelOpe", "tomatO", "shadOWs"],
    "k": ["aCt", "arK", "banK", "neCK", "identiCal", "Campaign"],
    "ˌɛə": ["freewARE", "wHEreas", "somewHEre", "fAREwell", "hardwARE", "vAriations"],
    "ˌɐ": ["outcOme", "Undermine", "cucUmber", "everyOne", "haircUt", "samsUng"],
    "ʒ": ["deciSions", "viSion", "massaGe", "eroSion", "caSualty", "Genres"],
    "ɒ": ["carlOs", "coupOn", "chaOs", "vOlcano", "Ontario", "neurOne"],
    "p": ["keePer", "PoPs", "Pouch", "jumPing", "Plain", "lifesPan"],
    "ˌɔː": ["rainfAll", "airpORt", "indOOR", "passpORt", "jigsAW", "hardcORE"],
    "ˈɔː": ["crAWl", "cAll", "accOrd", "awArd", "scOre", "fOUGHt"],
    "m": ["huMble", "caMpus", "siMilar", "screaM", "MuseuM", "coMMitMent"],
    "ˈiː": ["tEEnagers", "retrIEve", "fEE", "hEAted", "frEEly", "Equal"],
    "ɹ": ["Royal", "pRinting", "Runner", "matRon", "aRRange", "Roll"],
    "ɑː": ["pARticipate", "avatAR", "packARd", "nuAnce", "ARcade", "mARquee"],
    "ˌɪ": ["sImulation", "Infrared", "sYstematic", "Independent", "flagshIp", "dIsappear"],
    "əʊ": ["torsO", "margOT", "Oman", "videO", "marrOW", "shallOW"],
    "n": ["News", "dowN", "titaN", "iNceNtive", "eNd", "iNNoceNt"],
    "h": ["Hand", "Hat", "inHerit", "withHold", "Holiday", "Help"],
    "ˌɒ": ["icOn", "laptOp", "ecOmmerce", "Opportunities", "Obligations", "lOllipop", "pokemOn"],
    "ɪ": ["Incur", "InevItable", "chIswIck", "sayIng", "antIcs", "dIsrupt"],
    "ɪə": ["omniscIEnt", "latvIA", "victorIA", "warrIORs", "socIOlogical", "idIOm"],
    "ŋ": ["duriNG", "daNk", "kiNGs", "haNG", "stiNk", "aloNG"],
    "z": ["treeS", "froZen", "coneS", "eaSier", "haZe", "apologiSE"],
    "ˈɑː": ["cARd", "pARts", "mARks", "ARctic", "chARged", "pAss"],
    "ˌaʊ": ["discOUnted", "eyebrOW", "inbOUnd", "anyhOW", "sOUthend", "breakdOWn"],
    "ˈʊə": ["tOUrs", "pUre", "rUral", "endURE", "obscURE", "assUrance"],
    "ˌaɪ": ["coincIdes", "uruguAY", "organIser", "airlInes", "otherwIse", "mYself"],
    "ˈaʊ": ["hOUseholds", "encOUnter", "vOwel", "pOWer", "lOUd", "OUtlook"],
    "ˈɪə": ["hERE", "EAR", "spEAR", "wEIRd", "idEA", "bEER"],
    "ˈɜː": ["gIRl", "tERm", "squIRt", "fIRstly", "bURgers", "EARlier"],
    "ˌiː": ["parenthesEs", "indicEs", "athlEtes", "margarIne", "dEviation", "nebulAE"],
    "ˈə": ["cOs"],
    "ˌæ": ["cAscade", "formAt", "Animation", "meerkAt", "progrAm", "granddAd"],
    "ˌʊə": ["bUreaucratic", "jUrisdiction", "EUropean", "flUOrescent"],
    "w": ["Witness", "spyWare", "passWord", "Wires", "Warwick", "ecUAdor"],
    "l": ["fLeet", "Length(1)", "rituaL", "Lions", "expLain", "gLee"],
    "i": ["hurrY", "heavY", "jointlY", "oilY", "lorrIEs", "worrIEs"],
    "ˈɐ": ["sUnset", "dUcks", "pUmps", "rUgged", "Ultimate", "plUg"],
    "ˈɪ": ["twItch", "bIll", "sYmmetry", "zIp", "pIxels", "Injured"],
    "ˈɔɪ": ["trOY", "bOIl", "tOYs", "jOIn", "plOY", "paranOIa"],
    "ɔː": ["Albeit", "Already", "wARsAW", "AUtomation", "Almighty", "mOreover"],
    "ˌɪə": ["pEriodic", "hemisphERE", "hEREby", "rEAlistic", "atmosphERE", "lancashIRE"],
    "ʃ": ["SHy", "muSHrooms", "accompliSH", "raTios", "perfecTIon", "miSSions"],
    "ˈɒ": ["blOgging", "hydrAUlic", "swOt", "blOcked", "dOt", "pOnd"],
    "aɪ": ["bIology", "turbIne", "prIority", "vampIre", "mobIles", "Ideally"],
    "ˈɛə": ["pAIR", "shAREd", "lAIR", "stAIRs", "flAIR", "cAring"],
    "ʊ": ["calcUlate", "docUmentary", "spiritUality", "fluctUations", "compUtation", "singUlar"],
    "ə": ["Allow", "syllabUs", "dreadfUl", "compressIOn", "marmAlade", "Amaze"],
    "b": ["laBor", "haBit", "Beetle", "Boy", "aBsent", "fiBre"],
    "uː": ["Utility", "sinEW", "refUge", "sUdan", "dUet", "gotO"],
    "ˈəʊ": ["sOAp", "lOAthe", "blOke", "relOAd", "rOAst", "Overall"],
    "ɛə": [],
    "ˌɔɪ": ["playbOY", "invOIce", "powerpOInt", "asterOId", "paranOId", "cowbOY"],
    "ˈuː": ["glUE", "tOOth", "flEW", "sEWer", "bOO", "dOing"],
    "æ": ["Ambitious", "shAmpoo", "Advert", "mAgnetic", "webcAm", "decAff"],
    "ɛ": ["spEctator", "cortEx", "intEl", "gEneralise", "Enroll", "Embed"],
    "g": ["Guns", "Guys", "Grand", "stronG", "draG", "funGi"],
    "θ": ["THree", "THank", "birTH", "THeorem", "worTH", "meTHods"],
    "ʊə": ["eventUal", "sitUated", "inflUenced", "bUreaucracy", "unusUal", "usUal"],
    "d": ["DefenDant", "Deter", "auDi", "enDorse", "blaDE", "finD"],
    "ɜː": ["lURk", "hERself", "divERt", "gERm", "expERt", "thIRteenth"],
    "f": ["riFle", "Flush", "Furry", "Fist", "oFFicial", "Fellow"],
    "ˌɜː": ["passwORd", "univERse", "housewORk", "keywORd", "cERtification", "netwORks"],
    "ɐ": ["Unsure", "Updated", "hiccUp", "misUnderstanding", "prodUcts", "Undo"],
    "iː": ["crEate", "nemesEs", "maldIves", "rEload", "rEdo", "axEs"],
    "dʒ": ["briDGE", "cabbaGE", "maGic", "synerGy", "Jealousy", "clerGy"],
    "s": ["Stop", "Sir", "graSp", "dentiStS", "laSt", "Cider"],
    "tʃ": ["advenTURes", "wreTCH", "waTCH", "CHair", "preaCH", "stiTCHes"],
    "ˈɛ": ["sEmi", "Eggs", "affEcted", "Enter", "bEtter", "amEnded"],
    "ˈeɪ": ["awAY", "lAke", "bAsed", "nAture", "okAY", "stAIn"],
    "j": ["CUte", "MUsic", "TUne", "Yen", "Yoke", "Yes", "evalUating", "Fuse"],
}
# TODO: note on frontend that "j" is the "yer" sound
# TODO: note on frontend that "ʊ" is the ooh sound, often after the "j"