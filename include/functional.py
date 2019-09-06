LOGIN = "admin"
PASSWORD = 'admin'

user_login = input('Enter Login ')
user_password = input('Enter Password')


def is_auth(user_login, user_password):
    if user_login == LOGIN and user_password == PASSWORD:
        return True
    else:
        return False


if is_auth(user_login, user_password):
    print('OK')
else:
    print('NE ok')
