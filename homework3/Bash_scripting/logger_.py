import json
import os


def parse_log(line):
    line = line.split()
    remote_addr = line[0]
    remote_user = line[2]
    time_local = ' '.join(line[3:5]).replace("[", '').replace("[", '')

    method = line[5].replace('"', '')
    url = line[6].replace('"', '')
    protocol = line[7].replace('"', '')

    status = line[8]
    body_bytes_sent = line[9].replace('"', '')

    http_referer = line[10].replace('"', '')
    http_user_agent = ' '.join(line[12:len(line)]).replace('"', '')

    parse_log = {"remote_addr": remote_addr,
                 "remote_user": remote_user,
                 "time_local": time_local,
                 "method": method,
                 "url": url,
                 "protocol": protocol,
                 "status": status,
                 "body_bytes_sent": body_bytes_sent,
                 "http_referer": http_referer,
                 "http_user_agent": http_user_agent
                 }
    return parse_log


def num_requests(data):
    number = 0
    for line in data:
        if line.find(' - - ') != -1:
            number += 1
    return [number]


def num_requests_by_method(data):
    requests = {'POST': 0, 'GET': 0, 'HEAD': 0, 'DELETE': 0, 'PUT': 0, 'CONNECT': 0, 'TRACE': 0, 'PATCH': 0}
    for line in data:
        line = parse_log(line)
        method = line["method"]
        requests[method] += 1
    return requests


def top_size_requests(data):
        requests = []

        for line in data:
            line = parse_log(line)
            size = int(line["body_bytes_sent"])

            if len(requests) == 0:
                requests.append(line)
                continue

            min_ = min(requests, key=lambda tmp: int(tmp["body_bytes_sent"]))
            if len(requests) == 10 and size >= int(min_["body_bytes_sent"]):
                requests.remove(min_)
                requests.append(line)
            elif len(requests) < 10:
                requests.append(line)

        requests.sort(key=lambda tmp: int(tmp["body_bytes_sent"]))
        requests = requests[:10]
        requests.reverse()
        result = []
        for line in requests:
            new = {"url": line["url"],
                   "remote_addr": line["remote_addr"],
                   "method": line["method"],
                   "time": line["time_local"]
                   }
            result.append(new)

        return result


def top_requests_client_error(data):
    requests = []

    for line in data:
        line = parse_log(line)
        status = line["status"]

        if status[0] == '4':

            if len(requests) == 0:
                requests.append([line, 1])
                continue

            t = True
            for i in requests:
                if line["url"] == i[0]["url"] and line["remote_addr"] == i[0]["remote_addr"] and status==i[0]["status"]:
                    i[1] += 1
                    t = False
                    break

            if t:
                requests.append([line, 1])

    requests.sort(key=lambda tmp: tmp[1], reverse=True)
    requests = requests[:10]
    result = []
    for line in requests:
        new = {"url": line[0]["url"],
               "remote_addr": line[0]["remote_addr"],
               "status": line[0]["status"],
               "count": line[1]}
        result.append(new)

    return result


def top_requests_redirect(data):
    requests = []

    for line in data:
        line = parse_log(line)
        status = line["status"]

        if status[0] == '3':

            if len(requests) == 0:
                requests.append([line, 1])
                continue

            t = True
            for i in requests:
                if line["url"] == i[0]["url"] and line["remote_addr"] == i[0]["remote_addr"] and status == i[0]["status"]:
                    i[1] += 1
                    t = False
                    break

            if t:
                requests.append([line, 1])

    requests.sort(key=lambda tmp: tmp[1], reverse=True)
    requests = requests[:10]
    result = []
    for line in requests:
        new = {"url": line[0]["url"],
               "remote_addr": line[0]["remote_addr"],
               "status": line[0]["status"],
               "count": line[1]}
        result.append(new)

    return result


def write_in_record(data, file):
    if type(data) == type(list()):
        for line in data:
            print(line, file=file)
    else:
        print(data, file=file)



if __name__ == '__main__':

    path = input()

    if not path:
        path = ''
        listdir = os.listdir(path='./')
    elif path[-1] != '/':
        path += '/'
        listdir = os.listdir(path=path)
    else:
        listdir = os.listdir(path=path)

    list_logs_file = [path + i for i in listdir if i[-3: len(i)] == 'log']

    for path_file in list_logs_file:

        with open(path_file) as file:
            logs = file.readlines()

            name = f'{path_file[path_file.rfind("/")+1:len(path_file)-4]}_record'
            with open(f'{name}.py', 'w') as record:

                top_requests_client_error_mas = top_requests_client_error(logs)
                top_requests_server_mas = top_requests_redirect(logs)
                top_size_requests_mas = top_size_requests(logs)
                num_requests_mas = num_requests(logs)
                num_requests_by_method_mas = num_requests_by_method(logs)

                write_in_record(num_requests_mas, record)
                print("##############", file=record)

                write_in_record(num_requests_by_method_mas, record)
                print("##############", file=record)

                write_in_record(top_size_requests_mas, record)
                print("##############", file=record)

                write_in_record(top_requests_client_error_mas, record)
                print("##############", file=record)

                write_in_record(top_requests_server_mas, record)

                with open(f'{name}.json', 'w') as json_record:
                    num = {"count": num_requests_mas[0]}

                    json.dump(num, json_record, indent=3)

                    json.dump(num_requests_by_method_mas, json_record, indent=3)

                    json.dump(top_size_requests_mas, json_record, indent=3)

                    json.dump(top_requests_client_error_mas, json_record, indent=3)

                    json.dump(top_requests_server_mas, json_record, indent=3)


