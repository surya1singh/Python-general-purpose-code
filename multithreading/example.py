
a = 1

def foo():
    global a
    a = 2
    print(a)


def foo1():
    a = 3
    print(a)

foo()
foo1()
print(a)
