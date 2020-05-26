from tlr.utils import get_value_or_none


def format_as_str(data, format_template='{:.2f}'):
    return [format_template.format(d) for d in data]


def list_to_dict(data, keys):
    return dict([
        (k, get_value_or_none(data, i)) for i, k in enumerate(keys)
    ])


def stringify_dict(data, format_template='{:.2f}', keys=None):
    if not data:
        if keys:
            return list_to_dict([], keys)
        return {}
    return {k: format_template.format(v) for k, v in data.items()}
