# normal while loop example
print("Normal While Loop example")
i = 0
while i < 5:
   print(i)
   i += 1

#break statement example for while loop
print("With break statement example for while loop")
i = 0
while i < 5:
  print(i)
  if i == 3:
    break
  i += 1

# #continue statement example for while loop
print("With continue statement example for while loop")
i = 0
while i < 5:
  i += 1
  if i == 4: # 4 will not be printed
    continue
  print(i)


# #else statement example for while loop
print("With else statement example for while loop")
i = 0
while i < 5:
  print(i)
  i += 1
else:
  print("i is no longer less than 5")