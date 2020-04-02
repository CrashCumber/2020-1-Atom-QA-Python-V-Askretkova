
import pytest

from api.api_client import ApiClient

from conftest import Settings


class BaseCase:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, config, request):
        self.config: Settings = config
        self.api_client: ApiClient = request.getfixturevalue('api_client')