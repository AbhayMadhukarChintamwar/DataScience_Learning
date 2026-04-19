from functools import reduce

nums = [1,2,3,4,5,6,7,8,9]

evens = list(filter(lambda n: n % 2 == 0, nums))  # filter takes a function and an iterable and returns an iterator that produces those items of the iterable for which the function returns true. In this case, we are using the is_even function to filter out the even numbers from the nums list.
doubles = list(map(lambda n: n * 2 , evens)) # map takes a function and an iterable and returns an iterator that applies the function to every item of the iterable, yielding the results. In this case, we are using a lambda function to double the even numbers from the evens list.
sum = reduce(lambda a,b: a + b, doubles) # reduce takes a function and an iterable and returns a single value that is the result of applying the function cumulatively to the items of the iterable, from left to right. In this case, we are using a lambda function to sum up all the doubled even numbers from the doubles list.

print('Evens ',evens)
print('Doubles ', doubles)
print('Sum ', sum)