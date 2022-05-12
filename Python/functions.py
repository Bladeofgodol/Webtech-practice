def example(parameter:str, arg:int): #defining a function and converting global variable to local
    print(parameter)
    print(type(parameter))

    parameter = int(parameter) #explicit type casting
    print(parameter+12)
    print(type(parameter))
    return parameter


example("12",48) #we must call the function for it to work