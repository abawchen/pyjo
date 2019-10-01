def parse(value):
    if value == '':
        return ''
    elif value == 'null':
        return None
    else:
        return value

def parse_key_value_pairs(args):
    obj = {}
    pairs = map(lambda arg: arg.split('='), args)
    for (key, value) in pairs:
        print(key, value)
        obj[key] = parse(value)
    return obj
