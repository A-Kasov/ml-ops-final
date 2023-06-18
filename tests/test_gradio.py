from gradio_client import Client

client = Client("http://127.0.0.1:7860/")


def test_positive():
    result = client.predict("Very good cafe!", fn_index=0)
    assert result == "Positive"


def test_negative():
    result = client.predict("I really don't understand that rest. Stupid waiters", fn_index=0)
    assert result == "Negative"
