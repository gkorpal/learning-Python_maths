''' a function with numberical parameters '''


def quotientString(x, y):
    q = x//y
    r = x % y
    return ('The quotient of {0} and {1} is {2} with the '
            'remainder {3}.').format(x, y, q, r)


def main():
    print(quotientString(2, 3))
    print(quotientString(1234567890123, 5350571245678))
    a = int(input("Enter the first integer: "))
    b = int(input("Enter the second integer: "))
    print(quotientString(a, b))


main()
