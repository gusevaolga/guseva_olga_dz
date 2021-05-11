import re

def email_parse(email):
    pattern = re.compile(r'[^@]+@[^@\.]+\.[^@\.]+')
    if pattern.fullmatch(email) is None:
        raise ValueError(f'Wrong email: {email}')
    else:
        data = email.split('@')
        address = {'username': data[0], 'domain': data[1]}
    return address


print(email_parse('olyaguseva2008@rambler.ru'))
