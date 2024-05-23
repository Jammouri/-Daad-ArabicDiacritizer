from Constants import LoadConstants
from Functions import map_data
import numpy as np
import tensorflow as tf
import json

ARABIC_LETTERS_LIST, DIACRITICS_LIST, CHARACTERS_MAPPING, CLASSES_MAPPING, REV_CLASSES_MAPPING, REV_CHARACTERS_MAPPING = LoadConstants()

def predict(line, model, max_seq_len=400):
    """
    Predict the diacritics for the given line using the model
                    
    Input: line: String
    model: Model
    Output: String with diacritics
    """
    
    X, _ = map_data([line])
    predictions = model.predict(X).squeeze()
    predictions = predictions[1:]

    diacritized_line = ''
    for idx, char in enumerate(line):
        if char in ARABIC_LETTERS_LIST:
            diacritized_line += char
            max_idx = np.argmax(predictions[idx])
            diacritized_line += REV_CLASSES_MAPPING[max_idx]
        else:
            diacritized_line += char
    
    return diacritized_line

# load model .h5
model = tf.keras.models.load_model('..\weights\shape400ResidualsNormalized.h5')

# Define the maximum sequence length
max_seq_len = 400
# Predict the diacritics for the given line
line  = "إن الذي ملأ اللغات محاسنا ... جعل الجمال وسره في الضاد."
output = predict(line, model, max_seq_len)

# Save it as a JSON file
with open('output.json', 'w', encoding='utf-8') as f:
    json.dump({"input": line, "output": output}, f, ensure_ascii=False, indent=4)

