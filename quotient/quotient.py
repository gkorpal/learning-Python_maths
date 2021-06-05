''' prompts for two integers and then prints them out in a sentence with an
    integer division'''

x = int(input("Enter the first integer: "))
y = int(input("Enter the second integer: "))
z = x//y
w = x % y
print('The quotient of ', x, ' and ', y, ' is ', z, ' with a remainder of ', w,
      sep='')
