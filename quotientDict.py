''' a function with numerical parameters '''


def quotientString(x, y):
    q = x//y
    r = x % y
    return ('The quotient of {x} and {y} is {q} with the '
            'remainder {r}.').format(**locals())


def main():
    print(quotientString(2, 3))
    print(quotientString(1234567890123, 5350571245678))
    a = int(input("Enter the first integer: "))
    b = int(input("Enter the second integer: "))
    print(quotientString(a, b))


main()
