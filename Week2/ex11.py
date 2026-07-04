def c_to_f(C):
    F=(C*(9/5))+32
    return F

temp=float(input("Enter temperature in celcius:"))
temp_f=c_to_f(temp)
print("Temperature in Fahrenheit:",temp_f)