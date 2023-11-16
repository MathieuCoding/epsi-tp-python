# Exo 4
# def print_hi():
#     print('Hi, what\'s your name?')
#     name = input()
#     print(f'Hi, {name}')
# print_hi()

# Exo 5
# factorial = 1*2*3
# print(factorial)

# Exo 6
# print('Enter a first number')
# first_number = int(input())
# print('Enter a second number')
# second_number = int(input())
# print('Enter a third number')
# third_number = int(input())
# print('The average of the three numbers is ', (first_number + second_number + third_number)/3)

# Exo 8
# print('Enter a number')
# number = int(input())
# print('Enter a second number')
# second_number = int(input())
# if number > second_number:
#     print('The first number is greater than the second')
# elif number < second_number:
#     print('The second number is greater than the first')

# Exo 9
# print('Give me the value of the first side of a triangle')
# first_side = int(input())
# print('Give me the value of the second side of a triangle')
# second_side = int(input())
# print('Give me the value of the third side of a triangle')
# third_side = int(input())
# if first_side ** 2 + second_side ** 2 == third_side ** 2:
#     print('This is a right triangle')
# else:
#     print('This is not a right triangle')

# Exo 10
print('Give me a first number')
first_number = int(input())
print('Give me a second number')
second_number = int(input())
print('What would you like to do with them: +, -, *, /')
operator = input()
if operator == '+':
    print(first_number + second_number)
elif operator == '-':
    print(first_number - second_number)
elif operator == '*':
    print(first_number * second_number)
elif operator == '/':
    print(first_number / second_number)

