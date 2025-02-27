Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print("Numbers:", 10, 20, 30, 40, 50)
Numbers: 10 20 30 40 50
>>> print("Sum of 64 and 32:", 64 + 32)
Sum of 64 and 32: 96
>>> x = 64
>>> y = 32
>>> sum_result = x + y
>>> print("Sum using variables:", sum_result)
Sum using variables: 96
>>> s = "Lucky"
>>> print(s)
Lucky
>>> today = datetime.date.today()
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    today = datetime.date.today()
NameError: name 'datetime' is not defined. Did you forget to import 'datetime'?
>>> print(f"Today is {today.day}/{today.month}/{today.year}")
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    print(f"Today is {today.day}/{today.month}/{today.year}")
NameError: name 'today' is not defined
>>> phone_number = input("Enter your phone number: ")
Enter your phone number: 
>>> print(f"Your phone number is: {phone_number}")
Your phone number is: 
