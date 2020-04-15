import json
import time
import requests


class ApiClient:

    def __init__(self, url, user, password):
        self.base_url = url
        self.user = user
        self.password = password
        self.session = requests.Session()
        self.get_token()
        self.authorization()

    def _request(self, method, location, headers=None, data=None, redirect=False):
        response = self.session.request(method, location, headers=headers, data=data, allow_redirects=redirect)
        return response

    def get_token(self):
        response = self._request('GET', 'https://target.my.com/csrf/')
        headers = response.headers
        cookie = headers['Set-Cookie'].split(';')
        return cookie[0].split('=')[1]

    def authorization(self):
        location = 'https://auth-ac.my.com/auth?lang=ru&nosavelogin=0'
        headers = {'Content-Type': 'application/x-www-form-urlencoded',
                   'Referer': 'https://target.my.com/'}
        data = {
            'email': self.user,
            'password': self.password,
            'continue': 'https://target.my.com/auth/mycom?state=target_login%3D1#email'
        }
        response = self._request('POST', location, headers=headers, data=data)
        while response.status_code == 302:
            location = response.headers['Location']
            response = self._request('GET', location)
        return response

    def create(self):
        data = {"name": f'Новый аудиторный сегмент {time.ctime()}',
                "pass_condition": 1,
                "relations": [{
                    "object_type": "remarketing_vk_group",
                    "params": {"source_id": 31480508, "type": "positive"}
                 }
                ],
                "logicType": "or"}
        data = json.dumps(data)
        location = 'https://target.my.com/api/v2/remarketing/segments.json'
        headers = {'Content-Type': 'application/json',
                   'X-CSRFToken': self.get_token(),
                   'Referer': 'https://target.my.com/segments/segments_list/new',
                   'X-Requested-With': 'XMLHttpRequest'}
        response = self._request('POST', location, data=data, headers=headers)
        return response

    def delete(self, response):
        id = response.json()['id']
        location = f'https://target.my.com/api/v2/remarketing/segments/{id}.json'
        headers = {'X-CSRFToken': self.get_token(),
                   'Referer': 'https://target.my.com/segments/segments_list'}
        response = self._request('DELETE', location, headers=headers)
        return response
