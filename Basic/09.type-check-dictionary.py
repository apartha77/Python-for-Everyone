# Dictionary Data Types
person = {
"name": "Partha",
"age": 43,
"location" : "Kolkata"
}
print(type(person))
print(type(person['name']))
print(type(person["age"]))

#get values in disctionary by key
print("Value by key ", person["name"])

# We can check key of a dictionary using the in keyword
print("Check by keyword - name ", "name" in person)

#chage value of a dictionary
person["age"] = 44
print("Age value changed ",person["age"])

person.update({"age": 45})
print("Value of Age changed by using dictionary.update ",person["age"])

#addig value of a dictionary
person["eye_color"] = "brown"
print("Added key eye-colour and value as brown ", person)

person.update({"hair_color": "black"})
print("Added key hari-colour and value as black ",person)

#delete particular key from dictionary
person.pop("hair_color")
print("after deleting hair-colour using pop", person)

#delete last item from dictionary
person.popitem()
print("after deleting last item using popitem", person)

#delete particular key from dictionary usig del keyword
del person["age"]
print("deleting age directly by key", person)

#Loop dictionary
for x in person:
  print("key: ",x)
  print("value: ",person[x])

#Loop dictionary key 
for x in person.keys():
  print("Key",x)

#Loop dictionary value
for x in person.values():
  print("Value",x)
#print('check here ------------------->')
#Loop dictionary key and value
for x,y in person.items():
  print(x,y)
#print('check here ------------------->')
print(person)
#empty dictionary usig clear method
person.clear()
print(person)
