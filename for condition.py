n = int(input("Enter an integer: "))  # Input integer n
y = input("Enter a list of words (e.g., [big,brown,bat]): ")  # Input list-like string [big,brown,bat]
y = y.strip('[]')  # Remove the square brackets
y1 = y.split(',')  # Split the string by commas
for i in y1:
    print(i)

print("----------------------------------------")

fruits = ["apple", "banana", "cherry"]

#for loop
for x in fruits:
  print(x)