A=input("First word:")
B=input("Second word:")

if len(A)>len(B):
    print("The larger word is:", A)
elif len(A)==len(B):
    print("Both words are of equal length")
else:
    print("The larger word is:",B)