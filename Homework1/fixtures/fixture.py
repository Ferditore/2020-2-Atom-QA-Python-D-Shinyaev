import random

import pytest


@pytest.fixture()
def random_list():
    numbers = []
    for i in range(5):
        numbers.append(random.randint(0, 50))
    return numbers
