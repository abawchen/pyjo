from base64 import b64encode


def is_number(f, value):
    try:
        v = f(value)
        return True
    except:
        return False

def is_file_reference(value):
    return value[0] in [':', '%', '@']


def read_file(value):
    if value[0] == '@':
        return open(value[1:], 'r').read()
    elif value[0] == '%':
        return b64encode(
            open(value[1:], 'rb').read()).decode('ascii')

def parse(value):
    if value == '':
        return ''
    elif value == 'null':
        return None
    elif value.lower() in ['true', 'false']:
        return value.lower() == 'true'
    elif is_number(int, value):
        return int(value)
    elif is_number(float, value):
        return float(value)
    elif is_file_reference(value):
        return read_file(value)
    else:
        return value


def parse_key_value_pairs(args):
    obj = {}
    pairs = map(lambda arg: arg.split('='), args)
    for (key, value) in pairs:
        print(key, value)
        obj[key] = parse(value)
    return obj
