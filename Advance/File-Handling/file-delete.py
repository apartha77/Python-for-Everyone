# We can remove file by usnig inbuild os module
# import os
# os.remove("sample_file4.txt")

# delete file if exist
import os
if os.path.exists("sample_file4.txt"):
  os.remove("sample_file4.txt")
else:
  print("The file does not exist")

f=open("sample_file4.txt","w")
f.write("Create and Test the file")
f.close()
f=open("sample_file.txt", "r")
print(f.read())
f.close()
