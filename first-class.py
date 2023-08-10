# list_input=input('enter your numbers here separated by spaces: ')
# print (f'numbers entered are {list_input}')
# list_numbers = list(map(int, list_input.split()))
# # for i in list:
# #     total = list.sum()
# total = sum(list_numbers)
# print("sum:", total)



#What will be printed as the output?

def outer_function(a, b):
    def inner_function(c, d):
        return c + d
    return inner_function(a, b)
 
result = outer_function(5, 10)
print(result)