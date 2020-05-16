import pytest

from orm_client.orm_client import SqlOrmConnection


@pytest.fixture(scope='session')
def orm_client():
    return SqlOrmConnection('root', '', 'TEST_PYTHON_ORM')