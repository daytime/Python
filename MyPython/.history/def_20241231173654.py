from multiprocessing import Value


def say_hello(greeting):
    print(greeting)

say = ["good morning","good afternoon","good evening"]


for i in Val(3):
    say_hello(say[i])
