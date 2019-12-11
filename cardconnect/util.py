 # noqa

import logging
import sys
import re

import cardconnect


logger = logging.getLogger('cardconnect')

__all__ = [
    'StringIO',
    'parse_qsl',
    'json',
    'jsonpickle',
    'utf8',
    'log_debug',
    'format_log_message',
]

try:
    import io as StringIO
except ImportError:
    import io

try:
    from urllib.parse import parse_qsl
except ImportError:
    from cgi import parse_qsl

try:
    import json
except ImportError:
    raise ImportError(
        "The CardConnect SDK requires the json library.")

try:
    import jsonpickle
except ImportError:
    raise ImportError(
        "The CardConnect SDK requires the jsonpickle library.")


def utf8(value): # noqa
    if sys.version_info < (3, 0) and isinstance(value, str):
        return value.encode('utf-8')
    else:
        return value


def log_debug(message, **params): # noqa
    msg = format_log_message(dict(message=message, **params))
    if cardconnect.debug:
        print(msg, file=sys.stderr)
    logger.debug(msg)


def format_log_message(props): # noqa
    def fmt(key, val):
        if not isinstance(val, str):
            val = str(val)
        if re.search(r'\s', val):
            val = repr(val)
        if re.search(r'\s', key):
            key = repr(key)
        return '{key}={val}'.format(key=key, val=val)
    return ' '.join([fmt(key, val) for key, val in sorted(props.items())])
