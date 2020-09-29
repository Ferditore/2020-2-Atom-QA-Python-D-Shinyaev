import pytest


class TestIntOperation:

    def test_int_remainder(self):
        assert 3 % 2 == 1

    def test_int_abs(self):
        x = -3
        assert abs(x) == 3

    @pytest.mark.parametrize('a', list(range(-1, 2)))
    def test_int_pow(self, a):
        assert pow(a, 0) == 1

    def test_int_inversion(self):
        z = 0
        assert -z == 0


def test_int_bit_length():
    n = -34
    bin(n)
    assert n.bit_length() == 6
