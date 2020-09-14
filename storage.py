import os
import tempfile
import argparse
import json


def load_info(key, value):
    storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
    if value == 'None':
        with open(storage_path, 'r') as f:
            ches = str(f.readlines()).replace("['", '{').replace(", ']", "}")
            print(json.loads(ches)[key])
    if value != 'None':
        with open(storage_path, 'a') as f:
            f.write(f'"{key}": "{value}", ')

parser = argparse.ArgumentParser()
parser.add_argument('--key', dest='key')
parser.add_argument('--value', dest='value', default='None')

args = parser.parse_args()
load_info(args.key, args.value)


