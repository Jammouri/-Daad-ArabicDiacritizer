
from Constants import LoadConstants

ARABIC_LETTERS_LIST, DIACRITICS_LIST, CHARACTERS_MAPPING, CLASSES_MAPPING, REV_CLASSES_MAPPING, REV_CHARACTERS_MAPPING = LoadConstants()

def WER(original_content,predicted_content):
    original = original_content.split()
    prediction = predicted_content.split()

    # Delete words that doesn't have atleast 1 arabic letters using for loop
    for word in original:
        if not any(char in ARABIC_LETTERS_LIST for char in word):
            original.remove(word)

    for word in prediction:
        if not any(char in ARABIC_LETTERS_LIST for char in word):
            prediction.remove(word)

    Counter=0

    for original_word,predicted_word in zip(original,prediction):
        if original_word==predicted_word:
            continue
        else:
            Counter+=1

    return round(Counter/max(1, len(original)) * 100,2)



def DER(original_content,predicted_content):
    original_content += " "
    predicted_content += " "
    original_vector = []
    predicted_vector = []
    correct=0
    wrong=0

    for idx, char in enumerate(original_content):
        if char not in DIACRITICS_LIST and char != " ":
            if original_content[idx+1] in DIACRITICS_LIST:
                original_vector.append(original_content[idx+1])
                if original_content[idx+2] in DIACRITICS_LIST:
                    original_vector.append(original_content[idx+2])

                else:
                    original_vector.append(" ")
            else:
                original_vector.append(" ")
                original_vector.append(" ")
        
    for idx, char in enumerate(predicted_content):
        if char not in DIACRITICS_LIST and char != " ":
            if predicted_content[idx+1] in DIACRITICS_LIST:
                predicted_vector.append(predicted_content[idx+1])
                if predicted_content[idx+2] in DIACRITICS_LIST:
                    predicted_vector.append(predicted_content[idx+2])

                else:
                    predicted_vector.append(" ")
            else:
                predicted_vector.append(" ")
                predicted_vector.append(" ")

    original_vector = original_vector[:len(predicted_vector)]

    for idx, element in enumerate(original_vector):
        if original_vector[idx]==predicted_vector[idx]:
            if original_vector[idx]==" " or predicted_vector[idx]==" ":
                continue
            else:
                correct+=1
        else:
            wrong+=1


    rate=round(wrong/ max(1, (correct+ wrong)) * 100, 2)
    
    
    return original_vector, predicted_vector, rate, correct, wrong
