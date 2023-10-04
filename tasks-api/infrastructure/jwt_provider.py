from jose import jwt


def generate(input: str):
    payload = {'id': input}
    token = jwt.encode(payload, 'TASKS', algorithm='HS256')
    return token


def decode(token):
    payload = jwt.decode(token, 'TASKS', algorithms=['HS256'])
    return payload