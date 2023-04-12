# Examples of write activities with file
# append mode 
# myfile = open("sample_file2.txt", "a")
# myfile.write("\nThis line added by python program")
# myfile.close()

#just read the recently added line
# f = open("sample_file2.txt", "r")
# print("Contnet of the file after write ---> /n", f.read())
# print(f.read())
# f.close()


#file write mode example
f = open("sample_file3.txt", "w")
f.write("This is a line just overwritten the existing file\n")
f.close()
f = open("sample_file3.txt", "r")
print(f.read())
f.close()