user_name = input('Enter your name >>> ')

def get_name(user_name):
    my_name = 'Denis'
    if user_name is not None:
        return 'Hello, ' + user_name + '!!!!'
    else:
        return 'Hello, ' + my_name + '!!!!'

print(get_name(user_name))