#normal module useage example
print("Normal module usage")
import mycustom_module    #importing the custom module

mycustom_module.greet_person("Partha")    #call the method in custom module with passing parameter

#Using alias and accessig variable
print("Using alias and accessig variable")
import mycustom_module as mymodule

x = mymodule.personExample["age"]
print("Called my module to get the value from dictionary ", x)

# use dir() function to get all the variables and functions
print("Using dir() function to get all the variables and functions of custom_module_example")
import mycustom_module
x = dir(mycustom_module)
print(x)
