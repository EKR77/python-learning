atomic_weights={"H":1.008,"He":4.0026,"Li":6.94,"Be":9.0122,"B":10.81,"C":12.011,"N":14.007,"O":15.999,"F":18.998}

def calculate(formula):
    current_element=""
    current_count=""
    total_mw=0

    for char in formula:
        if char.isupper():
            if current_element != "":
               count=int(current_count) if current_count !="" else 1
               total_mw+= atomic_weights[current_element]*count
            current_element=char
            current_count=""
        elif char.isdigit():
            current_count += char

    
    if current_element != "":
        count = int(current_count) if current_count != "" else 1
        total_mw += atomic_weights[current_element] * count
        return total_mw

molecular_formula=input("Enter the molecular formula:")
mw=calculate(molecular_formula)
print("The molecular weight is:", mw)