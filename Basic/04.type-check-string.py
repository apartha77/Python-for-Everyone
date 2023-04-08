#Type Check String
strName = "Partha Das"
print(type(strName)) 

# #check strig length
print(len(strName))


# # multilie string
a = """This is,
a 
multi line
strig 1"""
print(a)

#format variables in string

age = 45
txt = "My name is Partha, and I am {}"
print(txt.format(age))

quantity = 12
itemNo = 365
price = 299.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemNo, price))

#Using index
quantity = 12
itemNo = 365
price = 299.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemNo, price))