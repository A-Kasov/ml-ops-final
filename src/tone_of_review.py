from keras.models import load_model
from keras.utils import pad_sequences
import pickle


def get_prediction(txt):
    model = load_model('./model/my_model.h5')
    with open('./model/tokenizer.pkl', 'rb') as f:
        tokenizer = pickle.load(f)
    text = [txt]
    text = tokenizer.texts_to_sequences(text)
    text = pad_sequences(text, maxlen=400, padding='post')
    pred = model.predict(text)
    if pred > 0.5:
        return 'Positive'
    else:
        return 'Negative'
