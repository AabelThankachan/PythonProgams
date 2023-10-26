alpha=input("Enter an alphabet to find whether its uppercase or not: ")
if alpha>='A' and alpha<='Z':
    print("Given alphabet is uppercase")
elif alpha>='a' and alpha<='z':
    print("Given alphabet is lowercase")
else:
    print(alpha,"is not an alphabetic character")    
