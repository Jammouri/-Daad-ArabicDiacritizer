import pickle as pkl


def LoadConstants():
    CONSTANTS_PATH = '../Constants'

    with open(CONSTANTS_PATH + '/ARABIC_LETTERS_LIST.pickle', 'rb') as file:
        ARABIC_LETTERS_LIST = pkl.load(file)
    with open(CONSTANTS_PATH + '/DIACRITICS_LIST.pickle', 'rb') as file:
        DIACRITICS_LIST = pkl.load(file)
    with open(CONSTANTS_PATH + '/RNN_BIG_CHARACTERS_MAPPING.pickle', 'rb') as file:
        CHARACTERS_MAPPING = pkl.load(file)
    with open(CONSTANTS_PATH + '/RNN_CLASSES_MAPPING.pickle', 'rb') as file:
        CLASSES_MAPPING = pkl.load(file)
    with open(CONSTANTS_PATH + '/RNN_REV_CLASSES_MAPPING.pickle', 'rb') as file:
        REV_CLASSES_MAPPING = pkl.load(file)
    REV_CHARACTERS_MAPPING = {value: key for key, value in CHARACTERS_MAPPING.items()}

    return ARABIC_LETTERS_LIST, DIACRITICS_LIST, CHARACTERS_MAPPING, CLASSES_MAPPING, REV_CLASSES_MAPPING, REV_CHARACTERS_MAPPING