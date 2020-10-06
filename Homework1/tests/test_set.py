import pytest


class TestSet:

    def test_set_alpha(self):
        a = set('hello')
        with pytest.raises(AssertionError):
            assert a == {'h', 'a', 'l', 'o'}

    @pytest.mark.parametrize('b', [6, 7, 8])
    def test_set_len(self, b):
        a = {(i + 7) * 5 for i in range(b)}
        assert len(a) == b

    def test_set_union(self):
        set1 = set("1, 2, 3")
        set2 = set("World")
        assert set.union(set1, set2) == {'1', '2', '3', ' ', ',',
                                         'W', 'o', 'r', 'l', 'd'}

    def test_set_frozen(self):
        b = frozenset('frozen')
        with pytest.raises(AttributeError):
            assert b.add(1)

    def test_set_remove(self):
        c = {1, 2, 3, 4}
        with pytest.raises(KeyError):
            c.remove(5)
