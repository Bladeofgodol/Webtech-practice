from datetime import date
name = str(input("whats your name? "))
#print(name.capitalize())#built in function
print(name.upper())
#custom function
namelist = list(name)
namelist[0] = namelist[0].upper()
Name = ""
#print(namelist)
for i in range(len(namelist)):
    Name = Name + namelist[i]


age = int(input(f'hello {Name} whats your age? '))
year = 2022 - age
print(f'you were born in {year} or {year - 1}')


def greet(* names):
    for name in names:
        print("hello",name)

greet("dan","jumua","abebe")