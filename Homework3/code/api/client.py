from urllib.parse import urljoin

import requests


class ResponseStatusCodeException(Exception):
    pass


class ApiClient:
    def __init__(self):
        self.auth_url = 'https://target.my.com/'
        self.base_url = 'https://target.my.com/dashboard'

        self.session = requests.Session()
        self.csrf_token = None

    def _request(self, method, location, status_code=200, headers=None, params=None, data=None, json=None,
                 json_resp=True):

        url = urljoin(self.base_url, location)

        response = self.session.request(method, url, headers=headers, params=params, json=json, data=data)

        if response.status_code != status_code:
            raise ResponseStatusCodeException(f' Got {response.status_code} {response.reason} for URL "{url}"')
        if json_resp:
            return response.json()
        return response

    def login(self, email, password):
        location = 'https://auth-ac.my.com/auth'

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Referer': 'https://target.my.com/'
        }

        data = {
            'email': email,
            'password': password,
            'continue': 'https://target.my.com/auth/mycom?state=target_login%3D1%26ignore_opener%3D1#email',
            'failure': 'https://account.my.com/login/'

        }
        self._request('POST', location, status_code=200, headers=headers, data=data, json_resp=False)
        self.get_csrf()

    def get_csrf(self):
        location = 'https://target.my.com/csrf'
        self._request('GET', location, json_resp=False)

    def create_segment(self, name):
        location = 'api/v2/remarketing/segments.json'
        request_payload = {'name': name,
                           'pass_condition': 1,
                           'relations': [{'object_type': 'remarketing_player',
                                          'params': {'type': 'positive',
                                                     'left': 365,
                                                     'right': 0}}],
                           'logicType': 'or'}
        headers = {'Content-Type': 'application/json',
                   'X-CSRFToken': self.session.cookies['csrftoken']
                   }
        response = self._request('POST', location, headers=headers, json=request_payload)
        return response['id']

    def check_segment(self):
        location = 'api/v2/remarketing/segments.json'
        segment_json_id = self._request('GET', location)
        return (response['id'] for response in segment_json_id['items'])

    def delete_segment(self, id: int):
        location = f'api/v2/remarketing/segments/{id}.json'
        headers = {'X-CSRFToken': self.session.cookies['csrftoken']}
        self._request('DELETE', location, status_code=204, headers=headers, json_resp=False)