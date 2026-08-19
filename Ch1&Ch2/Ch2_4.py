def hbd(age):
    if age%2 == 1: 
        return f"saimai is just 21, in base {(age//2):.0f}!"
    else: 
        return f"saimai is just 20, in base {age//2:.0f}!"

year = input("Enter year : ")

print(hbd(int(year)))