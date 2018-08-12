from collections import defaultdict
from datetime import time
import socket


class ClientError(Exception):
    pass


class Client:
    def __init__(self, host, port, timeout=None):
        self.host = host
        self.port = port
        self.timeout = timeout

    def _send(self, data):
        data_string = ''
        with socket.create_connection((self.host, self.port),
                                      self.timeout) as sock:
            sock.sendall(data)
            data_string = sock.recv(1024).decode()
        data = data_string.split('\n')
        if data[0] == 'ok':
            return data[1:-2]
        else:
            raise ClientError(data[1])

    def _parse_get(self, data):
        result = defaultdict(list)
        for row in data:
            if row:
                metric = row.split(' ')
                metric_name = metric[0]
                metric_value = float(metric[1])
                metric_time = int(metric[2])
                result[metric_name].append((metric_time, metric_value))
        return dict(result)

    def get(self, key):
        request = f"get {key}\n".encode()
        data = self._send(request)
        return self._parse_get(data)

    def put(self, metric, value, timestamp=None):
        if not timestamp:
            timestamp = str(int(time.time()))
        self._send(f"put {metric} {value} {timestamp}\n".encode())
