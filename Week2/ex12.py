def is_even(x):
    if x%2==0:
        return True
    else:
        return False
    
n=int(input("Enter a number:"))
ans=is_even(n)
if ans==True:
    print("The number is even")
else:
    print("The number is odd")