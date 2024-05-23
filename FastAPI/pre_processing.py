# My explanation for map_data function:
# X is a mapped text without diacritics and with <SOS> and <EOS> tokens
# Y is a one-hot encoded list of diacritics for each character in X
# So, for each character in X, we have a corresponding diacritic in Y
# Then X == Y

import pickle as pkl
import numpy as np

WITH_EXTRA_TRAIN = False
DATASET_PATH = 'Data'
CONSTANTS_PATH = ''


with open(CONSTANTS_PATH + 'ARABIC_LETTERS_LIST.pickle', 'rb') as file:
    ARABIC_LETTERS_LIST = pkl.load(file)
with open(CONSTANTS_PATH + 'DIACRITICS_LIST.pickle', 'rb') as file:
    DIACRITICS_LIST = pkl.load(file)
if not WITH_EXTRA_TRAIN:
    with open(CONSTANTS_PATH + 'RNN_BIG_CHARACTERS_MAPPING.pickle', 'rb') as file:
        CHARACTERS_MAPPING = pkl.load(file)
else:
    with open(CONSTANTS_PATH + 'RNN_BIG_CHARACTERS_MAPPING.pickle', 'rb') as file:
        CHARACTERS_MAPPING = pkl.load(file)
with open(CONSTANTS_PATH + 'RNN_CLASSES_MAPPING.pickle', 'rb') as file:
    CLASSES_MAPPING = pkl.load(file)
with open(CONSTANTS_PATH + 'RNN_REV_CLASSES_MAPPING.pickle', 'rb') as file:
    REV_CLASSES_MAPPING = pkl.load(file)




def remove_diacritics(data_raw):
    return data_raw.translate(str.maketrans('', '', ''.join(DIACRITICS_LIST)))



def to_one_hot(data, size):
    one_hot = list()
    for elem in data:
        cur = [0] * size
        cur[elem] = 1
        one_hot.append(cur)
    return one_hot



def map_data(data_raw):
    
    max_seq_len = 400
    
    X = list()
    Y = list()

    for line in data_raw:
        x = [CHARACTERS_MAPPING['<SOS>']]
        y = [CLASSES_MAPPING['<SOS>']]

        

        for idx, char in enumerate(line):
            if char in DIACRITICS_LIST:
                continue

            try:
                x.append(CHARACTERS_MAPPING[char])
            except KeyError as e:
                print(f"Error: Character '{char}' not found in CHARACTERS_MAPPING at index {idx} in line: {line}")

            

            if char not in ARABIC_LETTERS_LIST:
                y.append(CLASSES_MAPPING[''])
            else:
                char_diac = ''
                if idx + 1 < len(line) and line[idx + 1] in DIACRITICS_LIST:
                    char_diac = line[idx + 1]
                    if idx + 2 < len(line) and line[idx + 2] in DIACRITICS_LIST and char_diac + line[idx + 2] in CLASSES_MAPPING:
                        char_diac += line[idx + 2]
                    elif idx + 2 < len(line) and line[idx + 2] in DIACRITICS_LIST and line[idx + 2] + char_diac in CLASSES_MAPPING:
                        char_diac = line[idx + 2] + char_diac
                y.append(CLASSES_MAPPING[char_diac])

        
        assert(len(x) == len(y))

        x.append(CHARACTERS_MAPPING['<EOS>'])
        y.append(CLASSES_MAPPING['<EOS>'])

        # Padding
        pad_len = max_seq_len - len(x)
        x.extend([CHARACTERS_MAPPING['<PAD>']] * pad_len)  # Pad with '<PAD>' token
        y.extend([CLASSES_MAPPING['<PAD>']] * pad_len)  # Pad with '<PAD>' token
        # Comment Padding lines while training 
        # and keep them while using .tflite model

        y = to_one_hot(y, len(CLASSES_MAPPING))

        X.append(x)
        Y.append(y)

        # print(len(x))
        # print("yyyyyyyyyyyyyyyyyyyyyy")
        # print(len(y))

    # X = np.asarray(X)
    # Y = np.asarray(Y)

    return X, Y

def predict(line, model):
    X, _ = map_data([line])
    predictions = model.predict(X).squeeze()
    print(predictions.shape)
    predictions = predictions[1:]

    output = ''
    for char, prediction in zip(remove_diacritics(line), predictions):
        output += char

        if char not in ARABIC_LETTERS_LIST:
            continue

        if '<' in REV_CLASSES_MAPPING[np.argmax(prediction)]:
            continue

        output += REV_CLASSES_MAPPING[np.argmax(prediction)]

    return output