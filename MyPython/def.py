from multiprocessing import Value
from optparse import Values


def say_hello(greeting):
    print(greeting)


say = ["good morning", "good afternoon", "good evening"]


for i in Values(3):
    say_hello(say[i])
