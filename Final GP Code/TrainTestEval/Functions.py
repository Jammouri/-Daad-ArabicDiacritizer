from Constants import LoadConstants

ARABIC_LETTERS_LIST, DIACRITICS_LIST, CHARACTERS_MAPPING, CLASSES_MAPPING, REV_CLASSES_MAPPING, REV_CHARACTERS_MAPPING = LoadConstants()

def clean_text(text):
    """
    Function to clean text by keeping the elements in characters mapping values list and diacritics only
    input: text (string)
    output: cleaned text (string)
    """
    cleaned_text = ''
    for char in text:
        if char in CHARACTERS_MAPPING.keys() or char in DIACRITICS_LIST:
            cleaned_text += char
    return cleaned_text

def remove_diacritics(Diacritized_data):
    """
    Remove diacritics from the data
    This function receives a string and removes the diacritics from it
    Input: Diacritized_data: String with diacritics
    Output: String with no diacritics
    """
    
    for diacritic in DIACRITICS_LIST:
        Diacritized_data = Diacritized_data.replace(diacritic, '')
    return Diacritized_data


def to_one_hot(data, size):
    """
    Convert the data to one hot encoding
    This function receives a list of integers and converts it to one hot encoding
    Used for converting the labels to one hot encoding for model training
    Input: data: List of integers
    size: Size of the one hot encoding
    Output: List of one hot encoded vectors
    """
    
    one_hot = list()
    for elem in data:
        cur = [0] * size
        cur[elem] = 1
        one_hot.append(cur)
    return one_hot


def split_data(data_raw, max_seq_len=400):
    """
    Split the data into sequences of length less than or equal to max_seq_len
    This function receives a list of strings and splits them into sequences of length less than or equal to max_seq_len
    Input: data_raw: List of strings
    Output: List of strings with sequences of length less than or equal to max_seq_len
    """

    data_new = list()

    for line in data_raw:
        for sub_line in line.split('\n'):
            if len(remove_diacritics(sub_line).strip()) == 0:
                continue

            if len(remove_diacritics(sub_line).strip()) > 0 and len(remove_diacritics(sub_line).strip()) <= max_seq_len:
                data_new.append(sub_line.strip())
            else:
                sub_line = sub_line.split()
                tmp_line = ''
                for word in sub_line:
                    if len(remove_diacritics(tmp_line).strip()) + len(remove_diacritics(word).strip()) + 1 > max_seq_len:
                        if len(remove_diacritics(tmp_line).strip()) > 0:
                            data_new.append(tmp_line.strip())
                        tmp_line = word
                    else:
                        if tmp_line == '':
                            tmp_line = word
                        else:
                            tmp_line += ' '
                            tmp_line += word
                if len(remove_diacritics(tmp_line).strip()) > 0:
                    data_new.append(tmp_line.strip())

    return data_new


def map_data(data_raw, max_seq_len=400):
    """
    Map the data to the required format for training
    This function receives a list of strings and maps them to the required format for training
    Input: data_raw: List of strings
    Output: X: List of mapped strings without diacritics and with <SOS> and <EOS> tokens
    Y: List of one hot encoded vectors for each character in X
    """

    X = list()
    Y = list()

    for line in data_raw:
        x = [CHARACTERS_MAPPING['<SOS>']]
        y = [CLASSES_MAPPING['<SOS>']]

        for idx, char in enumerate(line):
                if char in DIACRITICS_LIST:
                    continue
                # if char wasn't a diacritic add it to x
                try:
                    x.append(CHARACTERS_MAPPING[char])
                except KeyError as e:
                    print(f"Error: Character '{char}' not found in CHARACTERS_MAPPING at index {idx} in line: {line}")

                # if char wasn't a diacritic and wasn't an arabic letter add '' to y (no diacritic)
                if char not in ARABIC_LETTERS_LIST:
                    y.append(CLASSES_MAPPING[''])
                # if char was an arabic letter only.
                else:
                    char_diac = ''
                    if idx + 1 < len(line) and line[idx + 1] in DIACRITICS_LIST:
                        char_diac = line[idx + 1]
                        if idx + 2 < len(line) and line[idx + 2] in DIACRITICS_LIST and char_diac + line[idx + 2] in CLASSES_MAPPING:
                            char_diac += line[idx + 2]
                        elif idx + 2 < len(line) and line[idx + 2] in DIACRITICS_LIST and line[idx + 2] + char_diac in CLASSES_MAPPING: # شدة فتحة = فتحة شدة
                            char_diac = line[idx + 2] + char_diac
                    y.append(CLASSES_MAPPING[char_diac])

        assert(len(x) == len(y))

        

        x.append(CHARACTERS_MAPPING['<EOS>'])
        y.append(CLASSES_MAPPING['<EOS>'])

        x = x[:max_seq_len]
        y = y[:max_seq_len]

        # Padding
        pad_len = max_seq_len - len(x)
        x.extend([CHARACTERS_MAPPING['<PAD>']] * pad_len)  # Pad with '<PAD>' token
        y.extend([CLASSES_MAPPING['<PAD>']] * pad_len)  # Pad with '<PAD>' token

        y = to_one_hot(y, len(CLASSES_MAPPING))

        X.append(x)
        Y.append(y)

    return X, Y