import pytest


def test_str_find():
    x = 'Python_'
    y = '3.8'
    assert x + y == 'Python_3.8'


class TestString:

    def test_str_count(self):
        string_1 = 'Privet, kak dela?'
        x = string_1.count('kak')
        assert x == 1

    def test_str_format(self):
        x = "The sum of 2 + 4 is {0}".format(2 + 4)
        assert x == "The sum of 2 + 4 is 6"

    def test_str_lower(self):
        string_2 = 'OFF CAPS LOCK'
        x = string_2.lower()
        assert x == 'off caps lock'

    @pytest.mark.parametrize('seven', ('s', 'e', 'v', 'e', 'n'))
    def test_str_find(self, seven):
        with pytest.raises(AssertionError):
            assert seven in 'two'
