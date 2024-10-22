x = [1,2,3,4]
y = [2,4,7,8]

z = []

for elements in x:
    if elements in y:
        z.append(elements)

print(z)        
