#Python is a dynamically typed language, meaning that variables are automatically assigned a type based on the value they are given.

var_int=1234567890123456789012345678901111111111111000000000022222222233333333 #Dynamically Sized

var_flot=1.12345678909876543210987654321 #Precision 15-16 decimal digits. Stored as 64-bit IEEE 754 floating-point numbers.

var_complex=3 + 4j #Complex Number. 3 is real Number and 4j is imaginary number.

var_str = "Easir Arafat Prime" #Dynamically allocated. Limited by system memory

print(f'{type(var_int)}: {var_int}')
print(f'{type(var_flot)}: {var_flot}')
print(f'{type(var_complex)}: {var_complex}')
print(f'{type(var_str)}: {var_str}')


#input Function
name=input('Enter Your Name')
print(f'Thanks :{name}')