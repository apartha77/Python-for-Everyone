# Read a file and print its contents
print("Select file from drive")
#filename = input("Enter file name >")
try:
    fhandl = open("SampleText.txt")
except:
    print("File doesn't exists")
    #exit()

fhandl = open("SampleText.txt")
print(fhandl)
for line in fhandl:
    print(line.rstrip)

print("Done")
# -------------------------------------------------------------------------------
