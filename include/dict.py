


def sort(l):
    list_even = []
    list_odd = []
    for number in range(some):
        if number % 2 == 0:
            list_even.append(number)
        else:
            list_odd.append(number)

    # return {
    #     "even": [x for x in l if x % 2 == 0],
    #     "odd": [x for x in l if x % 2 == 1]
    # }

    return {
        "even": list_even,
        "odd": list_odd
    }