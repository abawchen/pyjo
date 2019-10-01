import json
import sys
from pyjo.parse import parse, parse_key_value_pairs

def cli():
    print('Welcome')
    args = sys.argv[1:]
    print(args)
    obj = parse_key_value_pairs(args)
    print(json.dumps(obj, indent=2))


if __name__ == '__main__':
    cli()
