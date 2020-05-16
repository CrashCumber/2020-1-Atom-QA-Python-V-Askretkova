import json
import socket

target_host = "127.0.0.1"
target_port = 5000
params = '/socket'

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.settimeout(0.1)

client.connect((target_host, target_port))

request = f'POST {params} HTTP/1.1\r\nHost:{target_host}\r\n\r\n'
client.send(request.encode())

total_data = []

while True:
    data = client.recv(1024)
    if data:
        total_data.append(data.decode())
    else:
        break

data = ''.join(total_data).splitlines()
status = data[0].split()[1]
result = {"status": status, "headers": data[1:-1], "body": data[-1]}
result = json.dumps(result)
print(result)
