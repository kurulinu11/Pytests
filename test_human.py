import pytest

class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def introduce_self(self):
        return f'My name is: {self.name} and I am {self.age} years old'
    
    def set_age(self, new_age):
        if not isinstance(new_age, (int, float)):
            return False
        self.age = new_age


@pytest.fixture
def set_up_human():
    return Human("Jan", 50)
    

def test_attributes(set_up_human):
    assert isinstance(set_up_human.name, str)
    assert isinstance(set_up_human.age, (int, float))

def test_setting_age(set_up_human):
    assert set_up_human.set_age("22") == False
    assert set_up_human.set_age(22) == None
    set_up_human.set_age(25)
    assert set_up_human.age == 25

def test_introduce_self_as_string(set_up_human):
    assert isinstance(set_up_human.introduce_self(), str)