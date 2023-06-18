# Tokenize
import pickle
from keras.utils import pad_sequences
import pandas as pd
import numpy as np


def preprocess(df):
    with open('./model/tokenizer.pkl', 'rb') as f:
        tokenizer = pickle.load(f)
    tokenized_text = tokenizer.texts_to_sequences(df.Review)
    tokenized_text = pad_sequences(tokenized_text, maxlen=400, padding='post')
    np.savetxt('./data/preprocessed/x_data.csv', tokenized_text, delimiter=",")
    np.savetxt('./data/preprocessed/y_data.csv', df.label, delimiter=",")


if __name__ == '__main__':
    print('Data preprocess...')
    preprocess(pd.read_csv('./data/YELP_data.csv'))
    print('Data preprocess completed!')
