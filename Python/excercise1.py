first_value = float(input('please insert the first value: '))
second_value = float(input('please insert the second value: '))
operation = input('1 = + \n 2 = - \n 3 = x \n 4 = / \n')
if operation == 1:
    print(f'the sum is{first_value + second_value}')
elif operation == 2:
    print(f'the diffrence is{first_value - second_value}')
elif operation == 3:
    print(f'the product is{first_value * second_value}')
elif operation == 4:
    print(f'the quotiont is{first_value / second_value}')
else:
    pass