import pytest


class TestListMethod:

    def test_list_extend(self, random_list):
        lst = [random_list]
        lst.extend([5, 6, 7, 8, 9])
        assert lst == [random_list, 5, 6, 7, 8, 9]

    def test_list_append(self, random_list):
        lst = [1, 2, 3, 4]
        lst.append(random_list)
        assert lst == [1, 2, 3, 4, random_list]

    def test_list_clear(self):
        lst = ['list']
        lst.clear()
        assert lst == []

    def test_list_pop(self):
        lst = [1, 2, 0, 4]
        list.pop([3])
        print(lst)
        assert lst[3] != 0


@pytest.mark.parametrize('a, b', [([1, 2], [3, 4]), ([12, 21], [13, 31])])
def test_list_sum(a, b):
    assert a + b == [*a, *b]
