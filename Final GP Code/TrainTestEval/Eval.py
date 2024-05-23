import os
import tensorflow as tf
import numpy as np
from Functions import clean_text, remove_diacritics, predict, split_data
from DER_WER import WER, DER


# Load test data
test_raw = []
filename = r"C:\Users\user\Downloads\test (1).txt"
with open(filename, 'r', encoding='utf-8') as file:
    lines = file.readlines()
    test_raw.extend(lines)


# Split test data
test_split = split_data(test_raw)
print('test examples (split):', len(test_split))


# Clean test data
clean_test = []
for line in test_split:
    clean_test.append(clean_text(line))


# Just add the model names and the max sequence lengths and the code will generate the results for all models
models_names = ['shape400withResiduals', 'shape400withResiduals2']
max_seq_lens = [400, 400]

if not os.path.exists('Models Results'):
    os.makedirs('Models Results')
for model_name, max_seq_len in zip(models_names, max_seq_lens):
    if not os.path.exists('Models Results/{model_name}.txt'):
        print(f"Predicting for model: {model_name}")
        model = tf.keras.models.load_model(f'models/{model_name}.h5')
        results = list()
        for line in test_split:
            x = predict(line, model)
            results.append(x)
        # Create file with model name
        with open(f'Models Results/{model_name}.txt', 'w', encoding='utf-8') as file:
            for line, result in zip(test_split, results):
                file.write(f"{line}\n")
                file.write(f"{result}\n")


# Calculate DER and WER for each model
models_names = ['shape400withResiduals', 'shape400withResiduals2']

for model_name in models_names:
    with open(f'Models Results/{model_name}.txt', 'r', encoding='utf-8') as file:
        # original content is the odd lines
        # predicted content is the even lines
        content = file.readlines()
        original_content = ''.join(content[::2])
        predicted_content = ''.join(content[1::2])
        
    DER_VALUES = []

    for org, pred in zip(original_content.split('\n'), predicted_content.split('\n')):
        DER_VALUES.append(DER(org, pred))

    print(f'{model_name} DER: {sum(sublist[2] for sublist in DER_VALUES) / len(DER_VALUES)}')
    # WER
    WER_VALUES = []
    for org, pred in zip(original_content.split('\n'), predicted_content.split('\n')):
        WER_VALUES.append(WER(org, pred))
    print(f'{model_name} WER: {sum(WER_VALUES) / len(WER_VALUES)}')
    print('---------------------------------')
