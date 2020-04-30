import json
import threading
from faker import Faker
fake = Faker(locale='ru_RU')

from flask import Flask, request

app = Flask(__name__)

host = '127.0.0.1'
port = 5000


def run_mock():
    server = threading.Thread(target=app.run, kwargs={'host': host, 'port': port})
    server.start()
    return server


def shutdown_mock():
    terminate_func = request.environ.get('werkzeug.server.shutdown')
    if terminate_func:
        terminate_func()


client_data = {}
@app.route('/post_request', methods=['POST'])
def post_request():
    data = request.get_json()
    client_data.update(data)


server_data = {}
@app.route('/get_request')
def get_request():
    return json.dumps(server_data)


users = {}
@app.route('/all_data', methods=['GET', 'POST'])
def all_data():
    try:
        data = request.get_json()
        users.update(data)
    except :
        pass

    return json.dumps(users)


@app.route('/shutdown')
def shutdown():
    shutdown_mock()


@app.route('/socket',  methods=['POST'])
def socket_page():
    print('The connection with my socket is successful ')
    return 'The connection with my socket is successful '

if __name__ == '__main__':
    run_mock()