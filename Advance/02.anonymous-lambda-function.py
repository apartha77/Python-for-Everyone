# lambda when not creating any function, but generic use instead
# doSum = lambda a,b: a + b
# print(doSum(10,20))

# same in normal function
# def doSum(a,b):
#    return a + b
# print(doSum(10,20))

# list filter example to list values greater than 15
my_custom_list = [1, 2, 3, 4, 5, 6, 7, 8,  9, 10]

my_filtered_list = list(filter(lambda x: (x > 5) , my_custom_list))
print(my_filtered_list)

#use lambda to manipulate data set and do value doubler using map
my_custom_list = [1, 2, 3, 4, 5, 6, 7, 8,  9, 10]
my_manipulated_list = list(map(lambda x: x + x , my_custom_list))
print(my_manipulated_list)

mylist = list(filter(lambda x: (x > 2),my_custom_list))
print(mylist)