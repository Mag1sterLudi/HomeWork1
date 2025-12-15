from main import get_message

def test_message_content():
    expected = "Hello MIFI and SF by Alexeev A.A."
    assert get_message() == expected
