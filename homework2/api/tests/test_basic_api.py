from base import BaseCase
import pytest


class TestAPI(BaseCase):

    @pytest.mark.API
    def test_auto(self, api_client):
        response = api_client.authorization()
        assert response.status_code == 200

    @pytest.mark.API
    def test_segment_create(self, api_client):
        response = api_client.create()
        assert response.status_code == 200

    @pytest.mark.API
    def test_segment_delete(self, api_client):
        response = api_client.create()
        response = api_client.delete(response)
        assert response.status_code == 204

