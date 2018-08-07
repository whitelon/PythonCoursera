import os
import tempfile
import json
import argparse

argsparser = argparse.ArgumentParser()
argsparser.add_argument('--key')
argsparser.add_argument('--val')

args = argsparser.parse_args()

key = args.key
value = args.val

data = {}

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')

if os.path.isfile(storage_path):
    with open(storage_path, 'r') as f:
        if f.readable():
            filedata = f.read()
            if filedata:
                data = json.loads(filedata)

if value is None:
    value = data.get(key)
    if value is None:
        print(value)
    else:
        print(', '.join(data.get(key)))
else:
    if key not in data:
        data[key] = []
    data[key].append(value)

    with open(storage_path, 'w') as f:
        json.dump(data, f)
