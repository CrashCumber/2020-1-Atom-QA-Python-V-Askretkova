
import time

import pytest

import requests

class TestLinux:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, ssh_client):
        self.ssh_client = ssh_client

    def test_root(self):

        data = self.ssh_client.exec_cmd('echo centos | sudo -S cat /var/log/messages ')
        assert not(data.find('centos') == -1)


    def test_nginx_ssh(self):

        command = 'echo centos | sudo -S systemctl status nginx.service'
        data = self.ssh_client.exec_cmd(command)
        status = data.find('running')
        assert not(status == -1)

    def test_nginx_http(self):

        command = 'echo centos | sudo -S firewall-cmd --list-all'
        data = self.ssh_client.exec_cmd(command)

        if data.find('http') == -1:
            command = 'echo centos | sudo -S firewall-cmd --zone=public --add-service=http '
            self.ssh_client.exec_cmd(command)

        request = requests.get('http://127.0.0.1:8080')
        assert request.status_code == 200

    def test_check_nginx_log(self):

        command = 'echo centos | sudo -S firewall-cmd --list-all'
        data = self.ssh_client.exec_cmd(command)

        if data.find('http') == -1:
            command = 'echo centos | sudo -S firewall-cmd --zone=public --add-service=http '
            self.ssh_client.exec_cmd(command)

        requests.get('http://127.0.0.1:8080')
        command = 'echo centos | sudo -S cat /var/log/nginx/access.log | tail -n 1'
        self.ssh_client.exec_cmd(command)
        data = self.ssh_client.exec_cmd(command)
        request = data.find('python-requests')

        assert not(request == -1)

    def test_refuce_http_through_firewall(self):

        command = 'echo centos | sudo -S firewall-cmd --list-all'
        data = self.ssh_client.exec_cmd(command)

        if data.find('http') != -1:
            command = 'echo centos | sudo -S firewall-cmd --zone=public --remove-service=http '
            self.ssh_client.exec_cmd(command)

        command = 'echo centos | sudo -S systemctl status nginx.service'

        data = self.ssh_client.exec_cmd(command)
        status = data.find('running')

        try:
            request = requests.get('http://127.0.0.1:8080', time=0.1)
            assert not(request.status_code == 200)
        except:
            assert not(status == -1)
