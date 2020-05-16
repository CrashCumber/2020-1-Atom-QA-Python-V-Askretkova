import pytest

from ssh_client.ssh_client import SSH


@pytest.fixture(scope='session')
def ssh_client():
    with SSH(hostname='127.0.0.1', username='centos', password='centos', port=2222) as ssh:
        yield ssh

