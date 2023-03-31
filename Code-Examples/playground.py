# Type check
simpleList = ("red", "green", "blue", 4, 5, 6)

print(simpleList[2])
print(type(simpleList))
print(type(simpleList[3]))
print(simpleList[0:4])

# simpleList[3:] = [4, 5, 6]
print("simpleList[3:] = ", simpleList[0:])

# get last value of list
print("simpleList[-1] = ", simpleList[-1])

print('check this one ------------------>')



#we can run for loop on list
for x in simpleList:
  print(x)
  