# ask student size
size = int(input("how many students do you have? "))

# ask name and capitalize the first letter
def capital(id):
    name = str(input(f"whats student #{id+1} name? "))
    namelist = list(name)
    namelist[0] = namelist[0].upper()
    Name = ""
    for i in range(len(namelist)):
        Name = Name + namelist[i]
    return Name

    # age confirmation


def Age(name):
    age = int(input(f"what is {name}'s age? "))
    if age < 18:
        print(f"{name} is under age")
    else:
        print(f"{name} is not under age")

    # subject size and name asker


def subjectenquery():
    num = int(input("how many subjects are there? "))
    subjects = [""] * num
    for i in range(0, num):
        subjects[i] = str(input(f"what is subject #{i+1} ? "))
    return subjects

    # average calculator


def Avg(name, subjects):

    grade = [""] * len(subjects)
    for i in range(len(subjects)):
        grade[i] = int(input(f"what is {name}'s grade in {subjects[i]}? "))

    sum = 0
    for i in range(len(grade)):
        sum = sum + grade[i]
    if len(grade) > 0:
        average = sum / len(grade)
    else:
        print("there are no subjects listed")
        quit()
    print(f"{name}'s average is {average}")
    return average

    # pass fail checker


def passfail(avg, name):
    if avg < 60:
        print(f"{name} has failed")
    else:
        print(f"{name} have passed")


if size > 0:  # comfirm size of students is greater than 0

    # subject enquery call
    subjects = subjectenquery()

    # name
    name = [""] * size
    for i in range(size):
        name[i] = capital(i)

    # age
    for i in range(size):
        Age(name[i])

    # average
    
    avg = [""] * size
    for i in range(size):
        avg[i] = Avg(name[i], subjects)
    for i in range(size):
        print(f"{name[i]}'s average is {avg[i]}")

    # pass or fail
    for i in range(size):
        passfail(avg[i], name[i])

else:
    print("there are no students listed")