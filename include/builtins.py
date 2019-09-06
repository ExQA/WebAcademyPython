def outer_function():

    def inner_function():
        print('Inter function')

    print('Out function')
    inner_function()
outer_function()