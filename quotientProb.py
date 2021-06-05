''' a function with numberical parameters '''


def quotientProblem(x, y):
    q = x//y
    r = x % y
    s = ('The quotient of {0} and {1} is {2} with the '
         'remainder {3}.').format(x, y, q, r)
    print(s)


def main():
    quotientProblem(2, 3)
    quotientProblem(1234567890123, 5350571245678)
    a = int(input("Enter the first integer: "))
    b = int(input("Enter the second integer: "))
    quotientProblem(a, b)


main()
