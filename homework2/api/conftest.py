import logging
import os
from dataclasses import dataclass
import allure
import pytest

from api.api_client import ApiClient


@dataclass
class Settings:
    URL: str = None


@pytest.fixture(scope='session')
def config() -> Settings:
    settings = Settings(URL="https://target.my.com/")
    return settings


@pytest.fixture(scope='function')
def api_client(config):
    user = 'asktechnoatom@mail.ru'
    password = 'asktechnoatom'
    return ApiClient(config.URL, user, password)
