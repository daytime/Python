def average(a, b, c):
    ave= (a + b + c) / 3
    return ave


a = [3, 6, 18]

result = average(*a)
print(result)
