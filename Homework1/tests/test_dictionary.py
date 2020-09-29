import pytest


class TestDict:
    def test_dict_key(self):
        d = {a: a ** 2 for a in range(7)}
        with pytest.raises(KeyError):
            assert d['1'] == 2

    def test_dict_update(self):
        d = {a: a for a in range(4)}
        other = {'dict': 1, 'd': 2}
        d.update(other)
        assert d == {0: 0, 1: 1, 2: 2, 3: 3, 'dict': 1, 'd': 2}

    def test_dict_get(self):
        d = {a: a for a in range(4)}
        assert d.get(1) == 1

    @pytest.mark.parametrize('n', [1, 2, 3, 5])
    def test_dict_clear(self, n):
        d = {a: a for a in range(n)}
        assert d.clear() is None

    def test_dict_pop(self):
        car = {
            "brand": "Ford",
            "model": "Mustang",
            "year": 1964
        }
        assert car.popitem() == ('year', 1964)
