''' string format for quotient.py'''

x = int(input("Enter the first integer: "))
y = int(input("Enter the second integer: "))
print('The quotient of {} and {} is {} with the remainder {}.'
      .format(x, y, x//y, x % y))
