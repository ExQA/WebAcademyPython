


user_password = input('Enter Password  >>> ')
user_password_confirm = input('Enter Password confirm >>> ')



def is_auth( user_password):
    if  user_password == user_password_confirm:
        return True
    else:
        return False


if is_auth(user_login, user_password):
    print('OK')
else:
    print('NE ok')