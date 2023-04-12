#File read example - sample-file.txt
#Simple Read file example
myfile = open("sample_file.txt","r")
print(myfile.read())
myfile.close()

#read file by full path
# f = open("/Users/parthadas/Documents/Partha/01. Technical/Projects/Python/Python-for-Everyone/Advance/File-Handling/sample_file.txt", "r")
# print(f.read())
# f.close()

# We can read file with speific encding
# f = open("sample_file.txt", mode='r', encoding='utf-8')
# print(f.read())
# f.close()

#loop  through the file lines
# f = open("sample_file.txt", "r")
# i=1
# for x in f:
#   print("line:",i," ",x)
#   i+=1
#   for w in x:   # traverse the alphabets
#     print(w)
# f.close()

#read file is the file exists
# import os
# print("Check if the file exists")
# if os.path.exists("sample_file.txt"):
#     f=open("sample_file.txt")
#     print(f.read())
#     f.close()
# else:
#     print("The file does not exist")