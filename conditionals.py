#Break
#Continue
#Pass


#Break statements

# Simple break statement

for i in range(10): 
    print(i)
    if i == 2:
        break

print("------------------------------------------------")

# Using While 

i = 0
while True:
    print(i)
    if i == 2:
        break
    i += 1


print("---------------------------------------------------------")

# Continue Statement

# Using For loop

for i in range(5):
    if i == 2:       # 2 will be removed from printing 1 to 5 
        continue     # It removes the given integer, from the following range
    print(i)

# Using while loop

i = 0
while i<5:
    if i == 2:
        i += 1
        continue
    print(i)
    i += 1
        
# Using Pass 