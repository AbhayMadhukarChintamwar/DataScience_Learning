def square(num):
    return num * num

def cube(num):
    return num * num * num



# def operate(num, operation): # this is a higher order function because it takes another function as an argument
#     return operation(num)    # this will call the operation function with num as an argument and return the result


# value = 5
# result = operate(value,square)
# print(result)  # this will print the square of 5 which is 25



def operate(nums, operation):
    for i in nums:
        result = operation(i) # this will call the operation function with i as an argument and return the result
        print(result)

nums = [5,6,7,8,9]
operate(nums, square)  # this will print the square of each number in the nums list
operate(nums, cube)  # this will print the cube of each number in the nums list