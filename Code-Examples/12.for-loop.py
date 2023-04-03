#normal loop example in python
print("normal example")
colors = ["red", "green", "blue"]
for x in colors:
  print(x)

#we can loop though a strig
print("Loop through string")
str = "Hello World"
for x in str:
  print(x)

# loop break statement example in python
print("break statement example")
colors = ["red", "green", "blue"]
for x in colors:
    if(x == "green"):
        break
    print(x)

#loop continue statement example in python
print("continue statemet example")
colors = ["red", "green", "blue"]
for x in colors:
    if(x == "green"):
        continue
    print(x)

# else block loop example in python
print("else block example")
colors = ["red", "green", "blue"]
for x in colors:
    print(x)
else:
    print("All Items processed")

# # Range function loop example in python
print("Range function example")
for x in range(10):
  print(x)

n=0
for i in colors:
    print(n)
    if(n>0):
        print(colors[n])
    n = n+1
