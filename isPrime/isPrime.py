import math

def isPrime(num):
    if num == 2:
        return True
    elif num % 2 == 0 or num < 2: 
        return False
    else:
        for i in range(3, math.floor(math.sqrt(num))):
            if num % i == 0:
                return False   
        return True        


print(f'2:   {isPrime(2)}')
print(f'3:   {isPrime(3)}')
print(f'5:   {isPrime(5)}')
print(f'7:   {isPrime(7)}')
print(f'9:   {isPrime(9)}')
print(f'11:  {isPrime(11)}')
print(f'99:  {isPrime(99)}')
print(f'100: {isPrime(100)}')
print(f'101: {isPrime(101)}')
print(f'102: {isPrime(102)}')
print(f'103: {isPrime(103)}')