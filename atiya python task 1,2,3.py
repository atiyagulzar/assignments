Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>>  num=int(input("Enter your number:"))
 
SyntaxError: unexpected indent
>>> num=int(input("enter your numbr:"))
enter your numbr:56
>>> if num > 0:
	print("number is positive")
elif num < 0:
	print("number is negative")
else:
	print("number is zero")

	
number is positive
>>> #task no 2
>>> year=int(input("enter a year"))
enter a year 2024
>>> if year%4==0:
	print("this is a leap year")
else:
	print("this is not leap year")

	
this is a leap year
>>> #no 3
>>>  num1=float(input("enter a first number:"))
 
SyntaxError: unexpected indent
>>> num1=float(input("enter a first number:"))
enter a first number:67
>>> num2=float(input("enter a second number:"))
enter a second number:35
>>> operator=input("enter an operator from +,-,*,/")
enter an operator from +,-,*,/ *
>>>  if operator == "+":
	 
SyntaxError: unexpected indent
>>> if operator == "+":
	results=num1+num2
	print("the result is",results)
elif operator == "-":
	results=num1-num2
	print("the result is",results)
elif operator == "*":
	results=num1*num2
	print("the result is",results)
elif operator == "/":
	results=num_1/num_2
	print("the result is",results)
else:
	print("error! use correct operator")

	
error! use correct operator
>>> 