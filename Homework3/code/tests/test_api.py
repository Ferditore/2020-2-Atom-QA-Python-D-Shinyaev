from random import choice
from string import ascii_letters

import pytest

from api.client import ApiClient

EMAIL = 'qza34340@eoopy.com'
PASSWORD = 'qza34340-'


@pytest.mark.API
class TestApi:
    client = ApiClient()

    @pytest.fixture(scope='function')
    def login(self):
        self.client.login(EMAIL, PASSWORD)

    def test_create_segment(self, login):
        name = ''.join(choice(ascii_letters) for i in range(60))
        assert self.client.create_segment(name) in self.client.check_segment()

    def test_delete_segment(self, login):
        segment_json_id = self.client.create_segment('name')
        self.client.delete_segment(segment_json_id)
        assert segment_json_id not in self.client.check_segment()
