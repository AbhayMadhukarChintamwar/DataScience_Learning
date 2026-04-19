
def greater_first(func): #decorator
    def wrap(a,b):
        if a<b:
            a,b = b,a #swap the values of a and b if a is less than b
        return func(a,b) #call the original function
    return wrap  #return the wrapper function

@greater_first #decorator
def divide(a,b):
    return a/b

@greater_first #decorator
def subtract(a,b):
    return a-b

result1 = divide(4,2)
print(result1)

result2 = subtract(4,2)
print(result2)
