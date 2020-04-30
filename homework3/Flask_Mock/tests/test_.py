import json

import pytest
import requests
from mock.mock import server_data, client_data
from faker import Faker
fake = Faker(locale='ru_RU')


class TestMockClient:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, mock_server):
        server_host, server_port = mock_server
        self.host = server_host
        self.port = server_port

    def test_post(self):

        data = {}
        for i in range(10):
            user = {'name': fake.name(), 'job': fake.job()}
            data.update({str(i): user})

        url = f'http://{self.host}:{self.port}/all_data'

        result = requests.post(url=url, json=data)
        response = requests.get(url=url)

        assert result.json() == response.json() == data

    def test_get_request(self):
        for i in range(3):
            user = {'name': fake.name(), 'job': fake.job()}
            server_data.update({str(i): user})

        url = f'http://{self.host}:{self.port}/get_request'

        response = requests.get(url=url)
        assert server_data == response.json()

    def test_post_request(self):
        data = {}
        for i in range(3):
            user = {'name': fake.name(), 'job': fake.job()}
            data.update({str(i): user})
        url = f'http://{self.host}:{self.port}/post_request'

        requests.post(url=url, json=data)

        assert client_data == data

    def test_invalid_url(self):
        url = f'http://{self.host}:{self.port}/badurl'
        response = requests.get(url=url)
        assert response.status_code != 200

