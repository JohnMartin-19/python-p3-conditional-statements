#!/usr/bin/env python3

def admin_login(username, password):
    # your code here
    access='granted' if username == 'admin' & password == 12345 else 'denied'
    print(access)
admin_login('admin',12451)

def hows_the_weather(temperature):
    # your code here
    if temperature <= 40 :
        print('It is cold')
    elif temperature > 40 < 65:
        print('Too damn hot bro')
    else: 
        print('Perfect')
hows_the_weather(25)


def fizzbuzz(num):
    # your code here
    if num % 3 == 0:
        print('Fizz')
    elif num % 5 ==0:
        print('Buzz')
    else:
        print(num)

fizzbuzz(15)

def calculator(operation, num1, num2):
    # your code here
    if operation == "+" :
         print(num1 + num2)
    elif operation == '-' :
        print(num1 - num2)
    elif operation == "*":
        print(num1 * num2)
    elif operation == "/":
        print(num1/num2)
    else:
        print('Invalid Operation')
    
    calculator('+',10,5)