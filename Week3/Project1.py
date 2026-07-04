atomic_weights={"H": 1.008, "He": 4.0026, "Li": 6.94, "Be": 9.0122, "B": 10.81, "C": 12.01, "N": 14.01, "O": 16.00, "F": 19.00, "Ne": 20.18, "Na": 22.99, "Mg": 24.31, "Al": 26.98, "Si": 28.09, "P": 30.97, "S": 32.06, "Cl": 35.45, "Ar": 39.95, "K": 39.10, "Ca": 40.08, "Sc": 44.96, "Ti": 47.87, "V": 50.94, "Cr": 51.99, "Mn": 54.94, "Fe": 55.85, "Co": 58.93, "Ni": 58.69, "Cu": 63.55, "Zn": 65.38, "Ga": 69.72, "Ge": 72.63, "As": 74.92, "Se": 78.96, "Br": 79.90, "Kr": 83.80}

def calculate(formula):
    current_element = ""
    current_count = ""
    total_mw = 0

    for char in formula:
        if char.isupper():
            # new element starting — process the previous one first
            if current_element != "":
                count = int(current_count) if current_count != "" else 1
                total_mw += atomic_weights[current_element]*count
            current_element = char
            current_count = ""
        elif char.isdigit():
            current_count += char  # accumulate digit

    # process the last element after loop ends
    if current_element != "":
        count = int(current_count) if current_count != "" else 1
        total_mw += atomic_weights[current_element]*count
        return total_mw
    
molecular_formula=input("Enter the molecular formula:")
Total_mw=calculate(molecular_formula)
print("The molecular weight of", molecular_formula, "is:", Total_mw)