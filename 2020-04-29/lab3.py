import os
import json
import pickle
from parser1 import create_parser

FILENAME = "test.txt"


def ar(start=1, step=1):
    while True:
        yield start
        start += step


def test():
    pass


def to_json_file(obj, filename='test.json', indent=4):
    with open(filename, 'w') as f:
        json.dump(obj, f, indent=indent)


def from_json_file(filename='test.json'):
    with open(filename, 'r') as f:
        s = json.load(f,)
    return s


def to_pickle_file(obj, filename="test"):
    print(pickle.dumps(obj))
    with open(".".join([filename, 'picle']), 'wb') as f:
        pickle.dump(obj, f)


def from_picle_file(filename="test"):
    with open(".".join([filename, 'picle']), 'rb') as f:
        return pickle.load(f)


def check(filename):
    # list_access = (os.F_OK, os.R_OK, os.W_OK, os.X_OK​)
    print(os.access(filename, os.F_OK))
    print(os.access(filename, os.R_OK))
    print(os.access(filename, os.W_OK))


def get_num(start, step, count):
    gen = ar(start, step)
    for _ in range(count):
        yield next(gen)
    gen.close()


def main():
    parser = create_parser()
    namespace = parser.parse_args()

    if namespace.command == 'show':
        for num in get_num(namespace.start, namespace.step, namespace.count):
            print(num)
    elif namespace.command == 'save':
        for num in get_num(namespace.start, namespace.step, namespace.count):
            with open(namespace.filename, 'a') as f:
                f.write(str(num))
                f.write('\n')


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit()
