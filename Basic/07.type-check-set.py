simpleSet = {4,2,5,8,1}
print(type(simpleSet))

#we can run for loop on set
for x in simpleSet:
  print(x)

#we can add or remove values
simpleSet.add(10)
print(" After adding 10 ", simpleSet)

simpleSet.remove(10)
print("After removing 10  ", simpleSet)

#eliminate duplicates
simpleSet2 = {1, 2,2, 3, 3, 3, 4, 4, 4,4, 5,5,5,5,5 }
print("Set eliminates Duplicate values in the set ",simpleSet2)
print('Math Operations ------------------>')
#set can be used for mathematic set operations
print("Set is being used for Mathametical Operatioins such as union, intersection, difference")
#uninon
setA = {1, 2, 3, 4, 5, 6}
setB = {4, 5, 6, 7, 8, 9}
print("Example of Union", setA.union(setB))
print(setB.union(setA))
#intersection
print("Example of Intersection", setA.intersection(setB))
print(setB.intersection(setA))
#differece
print("Example of Difference", setA.difference(setB))
print(setB.difference(setA))
#Symmetric difference 
print("Example of Symmetric difference ",setA.symmetric_difference(setB))
print(setB.symmetric_difference(setA))