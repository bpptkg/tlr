def decode_string(s):
    try:
        return s.decode('utf-8')
    except AttributeError:
        return s


def force_str(s, encoding='utf-8', errors='strict'):
    if issubclass(type(s), str):
        return s
    try:
        if isinstance(s, bytes):
            s = str(s, encoding, errors)
        else:
            s = str(s)
    except UnicodeDecodeError as e:
        raise e
    return s
