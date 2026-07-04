def divide(a,b):
    try:
         return a/b
    except ZeroDivisionError:
        return "Division by zero is not allowed"

a=int(input("Enter a number:"))
b=int(input("Enter another number:"))

print(divide(a,b))