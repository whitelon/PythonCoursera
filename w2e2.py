import json

def to_json(func):
    def wrapped(*args, **kwargs):
        return json.dumps(func(*args, **kwargs))
    return wrapped
