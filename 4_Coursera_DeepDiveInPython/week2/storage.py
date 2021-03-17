import argparse
import tempfile
import os
import json

parser = argparse.ArgumentParser(description='Utility to read and write some data')
parser.add_argument('--key', type=str, help='Key data to read or write')
parser.add_argument('--val', type=str, help='Value data to write or append')
args = parser.parse_args()

key = args.key
value = args.val


def work_with_data(dic, key, val):
    if val == None:
        if key in dic:
            print(*dic[key], sep=', ')
        else:
            print(None)
    elif key not in dic:
        dic[key] = [val]
    else:
        dic[key].append(val)


storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')

if not os.path.isfile(storage_path):
    with open(storage_path, mode='w') as f:
        my_data = dict()
        work_with_data(my_data, key, value)
        with open(storage_path, mode='w') as file:
            json.dump(my_data, file)
else:
    with open(storage_path, mode='r') as f:
        my_data = json.load(f)
        work_with_data(my_data, key, value)
    with open(storage_path, mode='w') as file:
        json.dump(my_data, file)
