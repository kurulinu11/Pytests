import pytest

def count_chars(text):
    if not isinstance(text, str):
        return False
    counter = {}
    for char in text:
        if char in counter:
            counter[char] += 1
        else:
            counter[char] = 1
    return counter

# if __name__ == "__main__":
#     print(count_chars("TesTowanie"))  # -> powinno wyrdukwoac to: {'T': 2, 'e': 2, 's': 1, 'o': 1, 'w': 1, 'a': 1, 'n': 1, 'i': 1}
    

@pytest.fixture
def set_up_chars():
    text = count_chars("TesTowanie")
    return text

@pytest.fixture
def set_up_numeric_char():
    return count_chars("55555")
    
    
def test_count_validation(set_up_chars):
    assert set_up_chars.get("T") == 2
    assert set_up_chars.get('e') == 2
    assert set_up_chars.get('s') == 1

def test_numeric_char(set_up_numeric_char):
    assert set_up_numeric_char.get("5") == 5

def test_dictionary_content_validation():
    assert count_chars("TesTowanie") == {'T': 2, 'e': 2, 's': 1, 'o': 1, 'w': 1, 'a': 1, 'n': 1, 'i': 1}

def test_is_dictionary(set_up_chars):
    assert isinstance(set_up_chars, dict)




