from http.client import HTTPSConnection
from json import dumps, loads
from random import sample

API_KEY = '516454d3-fd8b-49cb-8a0f-776eb3db50ed'


def true_random_generator(n_min, n_max):
    request = {
        "jsonrpc": "2.0",
        "method": "generateIntegers",
        "params": {
            "apiKey": API_KEY,
            "n": n_max - n_min,
            "min": n_min,
            "max": n_max - 1,
            "replacement": False,
            "base": 10,
            "pregeneratedRandomization": None
        },
        "id": 18179
    }
    request = dumps(request)
    header = {"Content-Type": "application/json"}
    server = HTTPSConnection('api.random.org')
    server.request('POST', '/json-rpc/4/invoke', request, header)
    response = server.getresponse()
    data = loads(response.read().decode())
    data = data['result']['random']['data']
    return data


def pseudo_random_generator(n_min, n_max):
    return sample(range(n_min, n_max), n_max - n_min)


def sorted_generator(n_min, n_max):
    return list(range(n_min, n_max))
