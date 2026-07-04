def parse_formula(x):
    new_formula=""
    for char in x:
        if not char.isdigit():
            new_formula += char
    return new_formula

name=input("Enter molecule name")
letters=parse_formula(name)
print("The letters are:",letters)


    