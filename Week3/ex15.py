molecule_weights={
    "water":18,
    "carbon dioxide":44
}


print(molecule_weights["water"])

molecule_weights["acetone"] = 58

print(molecule_weights)
print("water" in molecule_weights)
print("ethanol" in molecule_weights)