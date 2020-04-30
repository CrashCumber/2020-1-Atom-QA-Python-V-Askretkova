from logger_client import LoggerConnection


class LoggerBuilder:

    def __init__(self, connection: LoggerConnection):
        self.connection = connection
        self.create_table('logs')

    def create_table(self, table):
        new_table = f"""
               CREATE TABLE if not exists `{table}` (
                 `id` smallint(6) NOT NULL AUTO_INCREMENT,
                 remote_addr char(20) NOT NULL,
                 remote_user char(20) NOT NULL,
                 time_local char(50) NOT NULL,
                 method char(20) NOT NULL,
                 url char(20) NOT NULL,
                 protocol char(20) NOT NULL,
                 status integer NOT NULL,
                 body_bytes_sent integer NOT NULL,
                 http_referer char(20) NOT NULL,
                 http_user_agent char(200) NOT NULL,
                 PRIMARY KEY (`id`)
               ) CHARSET=utf8
           """
        self.connection.execute_query(new_table)

    def add_log(self, data, table):
        insert = f"""
               INSERT INTO `{table}`(`remote_addr` ,
                 remote_user,
                 time_local,
                 method,
                 url,
                 protocol,
                 status,
                 body_bytes_sent,
                 http_referer,
                 http_user_agent) 
               
               VALUES(
                 '{data["remote_addr"]}',
                 '{data["remote_user"]}',
                 '{data["time_local"]}',
                 '{data["method"]}',
                 '{data["url"]}',
                 '{data["protocol"]}',
                 '{int(data["status"])}',
                 '{int(data["body_bytes_sent"])}',
                 '{data["http_referer"]}',
                 '{data["http_user_agent"]}'
                 )
           """
        self.connection.execute_query(insert)

    def parse_log(self, line):
        line = line.split()
        remote_addr = line[0]
        remote_user = line[2]
        time_local = ' '.join(line[3:5]).replace("[",'').replace("[",'')

        method = line[5].replace('"', '')
        url = line[6].replace('"', '')
        protocol = line[7].replace('"', '')

        status = line[8]
        body_bytes_sent = line[9].replace('"', '')

        http_referer = line[10].replace('"', '')
        http_user_agent = ' '.join(line[12:len(line)]).replace('"', '')

        parse_log = {"remote_addr" : remote_addr,
                     "remote_user": remote_user,
                     "time_local":time_local,
                     "method": method,
                     "url": url,
                     "protocol": protocol,
                     "status": status,
                     "body_bytes_sent": body_bytes_sent,
                     "http_referer" : http_referer,
                     "http_user_agent" : http_user_agent
                     }
        return parse_log

    def add_logs(self, data, table, parsed=False):
        if not parsed:
            for request in data:
                parsed_log = self.parse_log(request)
                self.add_log(parsed_log, table)
        else:
            for parsed_log in data:
                self.add_log(parsed_log, table)

    def num_requests(self):
        number = 'SELECT id FROM logs ORDER BY id DESC limit 1;'
        self.connection.execute_query(number)
        return self.connection.execute_query(number)

    def num_requests_by_method(self):
        new_table = f"""
                      CREATE TABLE if not exists num_method (
                        method char(20) NOT NULL,
                        num integer NOT NULL,
                        PRIMARY KEY (`method`)
                      ) CHARSET=utf8
                  """
        self.connection.execute_query(new_table)

        data = "SELECT method, count(*) FROM logs GROUP BY method;"
        res = self.connection.execute_query(data)

        for i in res:
            insert = f"INSERT INTO num_method VALUES {i};"
            self.connection.execute_query(insert)

    def top_size(self):
        self.create_table('big_logs')
        data = "SELECT * FROM logs ORDER BY body_bytes_sent DESC limit 10;"

        res = self.connection.execute_query(data)
        for i in res:
            insert = f"INSERT INTO big_logs VALUES {i};"
            self.connection.execute_query(insert)

    def top_requests_client_error(self):
        new_table = f"""
                              CREATE TABLE if not exists top_client_error (
                                `id` smallint(6) NOT NULL AUTO_INCREMENT,
                                remote_addr char(20) NOT NULL,
                                url char(20) NOT NULL,
                                status integer NOT NULL,
                                num integer NOT NULL,
                                PRIMARY KEY (`id`)
                              ) CHARSET=utf8
                     """
        self.connection.execute_query(new_table)

        data = """
                    SELECT remote_addr, url, status, count(*) FROM logs WHERE status LIKE '4%' 
                    GROUP BY remote_addr, url, status ORDER BY count(*) DESC limit 10;
                 """
        res = self.connection.execute_query(data)

        for i in res:
            insert = f"INSERT INTO top_client_error(remote_addr, url, status, num) VALUES {i};"
            self.connection.execute_query(insert)

    def top_requests_server_error(self):
        new_table = f"""
                              CREATE TABLE if not exists top_server_error (
                                `id` smallint(6) NOT NULL AUTO_INCREMENT,
                                remote_addr char(20) NOT NULL,
                                url char(20) NOT NULL,
                                status integer NOT NULL,
                                num integer NOT NULL,
                                PRIMARY KEY (`id`)
                              ) CHARSET=utf8
                     """
        self.connection.execute_query(new_table)

        data = """
                    SELECT remote_addr, url, status, count(*) FROM logs WHERE status LIKE '5%' 
                    GROUP BY remote_addr, url, status ORDER BY count(*) DESC limit 10;
                 """
        res = self.connection.execute_query(data)

        for i in res:
            insert = f"INSERT INTO top_server_error(remote_addr, url, status, num) VALUES {i};"
            self.connection.execute_query(insert)


def write_in_db(data):
    connection = LoggerConnection()
    client = LoggerBuilder(connection)
    client.add_logs(data, 'logs')
    client.top_requests_client_error()
    client.top_requests_server_error()
    client.num_requests_by_method()
    print('number of logs ', client.num_requests()[0][0])
    client.top_size()


if __name__ == '__main__':
    path = input()

    if not path:
        path = './access.log'
    elif path[-1] == '/':
        path += 'access.log'
    else:
        path += '/access.log'

    with open(path) as file:
        logs = file.readlines()
        write_in_db(logs)



