def multiply(*args):
    total = 1
    for number in args:
        total *= number
    return total

multiplication = multiply(10, 2, 3, 4, 5)
print(multiplication)
def pair_odd(number):
    multiple_of_two = number % 2 == 0
    if multiple_of_two:
        return f'{number} é par'
    # else:
    return f'{number} é ímpar' 

print(pair_odd(2))
print(pair_odd(3))
print(pair_odd(15))
print(pair_odd(16))