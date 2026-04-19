
# def func(num):
#     return num * num

func = lambda num: num * num # lambda is an anonymous function, it can take any number of arguments but can only have one expression. The expression is evaluated and returned.
add = lambda x, y : x + y # lambda can also be used to create simple functions that can be used in higher-order functions like map, filter, and reduce.

result = func(5)
print(result)

result = add(3, 4)
print(result)