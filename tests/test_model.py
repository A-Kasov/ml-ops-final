from keras.models import load_model
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import numpy as np

model = load_model('./model/my_model.h5')
x_data = np.genfromtxt('./data/preprocessed/x_data.csv', delimiter=',')
y_true = np.genfromtxt('./data/preprocessed/y_data.csv', delimiter=',')

y_pred = (model.predict(x_data) > 0.5).astype("int32")


def test_accuracy():
    accuracy = accuracy_score(y_true, y_pred)
    threshold = 0.8
    assert (
            accuracy >= threshold
    ), f"Expected accuracy_score >= {threshold}, but got {accuracy}"


def test_precision():
    precision = precision_score(y_true, y_pred)
    threshold = 0.7
    assert (
            precision >= threshold
    ), f"Expected precision_score >= {threshold}, but got {precision}"


def test_recall():
    recall = recall_score(y_true, y_pred)
    threshold = 0.7
    assert (
            recall >= threshold
    ), f"Expected recall_score >= {threshold}, but got {recall}"


def test_f1():
    f1 = f1_score(y_true, y_pred)
    threshold = 0.7
    assert (
            f1 >= threshold
    ), f"Expected f1_score >= {threshold}, but got {f1}"
