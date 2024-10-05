n = int(input("Enter an integer: "))  # Input integer n
y = ['big','brown','bat']   # Input list-like string [big,brown,bat]
y = y.strip('[]')  # Remove the square brackets
y1 = y.split(',')  # Split the string by commas
for i in y1:
    print(i)

print("----------------------------------------")

fruits = ["apple", "banana", "cherry"]


for x in fruits:
  print(x)


for i in range(10):
   print(i)
   if i == 2:
      break