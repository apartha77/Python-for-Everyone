# Loop through a word and print each letter - using index for each letter in a word
index = 0
word = input("Enter a word>")
while index < len(word):
    letter = word[index]
    #print("The letter at position :{0} is {1}".format(index,letter))
    print("The letter at position", index, "is", letter)
    index = index +1
print("Done")
#-------------------------------------------------------------------------------
