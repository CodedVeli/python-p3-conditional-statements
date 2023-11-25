#!/usr/bin/env python3

def admin_login(username, password):
        if username == 'admin' or password == '12345':
            return "Access granted"
        else:
            return "Access denied"   
pass    
    

def hows_the_weather(temperature):
    
    if temperature < 40:
        return "It's super cold today. Wear layers!"
    elif temperature < 70:
        return "It's pretty cold today. Wear a jacket!"
    elif temperature < 100:
        return "It's a bit hot today. Be careful!"
    else:
        return "It's super hot today. Don't go outside!"

    pass

def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 5 == 0:
        return "Buzz"
    elif num % 3 == 0:
        return "Fizz"
    else:
        return num
    pass

def calculator(operation, num1, num2):  
    if operation == "add":
        return num1 + num2
    elif  operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            print("Error: Cannot divide by 0")
        else:
            return num1 / num2
    else:
        print("Invalid operation")  
    pass
    
