def factorial(n):
    assert n >= 0 and int(n) == n, 'n must be a positive integer'
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

print('its factorial is: ', factorial(int(input('enter a number: '))))

def fibonacci(n):
    assert n >= 0 and int(n) == n, 'n must be a positive integer'
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

num = int(input('enter a number: '))
print('the #', num, ' fibonnaci number is: ', fibonacci(num-1), sep='')
