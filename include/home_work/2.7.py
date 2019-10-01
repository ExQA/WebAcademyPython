# Поменять местами самый большой и самый маленький элементы списка;
massiv = [1, 3, 5, 3, 1, 555, 6, 6, 6, 6, 555]

def max_min(l):

    maximum = max(l)
    minimum = min(l)

    for i in range(len(l)):
        if l[i] == maximum:
            l[i] = minimum
        elif l[i] == minimum:
            l[i] = maximum
    return l

print(max_min(massiv))