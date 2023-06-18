import pandas as pd

dataset = pd.read_csv('./data/YELP_data.csv')


def test_null_check():
    assert dataset.isnull().any(axis=1).sum() == 0


def test_column_name():
    assert 'Review' in dataset.columns
    assert 'label' in dataset.columns


def test_duplicates():
    assert not dataset.Review.duplicated().any()
