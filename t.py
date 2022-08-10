
def foo(bar: list) -> None:
    print(id(bar))
    bar[0] = 2
    print(id(bar))


a = [1, 2, 3]
print(id(a))
foo(a)
print(a)
int()