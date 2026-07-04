name = input("Enter molecular name:")
formula = input("Molecular Formula:")

letter_only = ""
for char in formula:
    if not char.isdigit():
        letter_only += char
print("Molecule:",name)
print("Formula:",formula)
print("Formula length:",len(formula))
print("letters only:",letter_only)
print("Element count:",len(letter_only))
