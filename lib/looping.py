#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    n = 10
    while n >= 0:
        print('Happy New Year!') if n == 0 else print(n)
        n -= 1
    pass

happy_new_year()
def square_integers(int_list):
    # code goes here!
    sqr = [int_item ** 2 for int_item in int_list]
    print(f'The square root is: {sqr}')
    return sqr

square_integers([1, 2, 3, 4, 5])
def fizzbuzz():
    # code goes here!
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            
            print('FizzBuzz')
        else:
            if num % 3 == 0:
                print('Fizz')
            elif num % 5 == 0:
                print('Buzz')
            else:
                print(num)
            
        
    pass
fizzbuzz()