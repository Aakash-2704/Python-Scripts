x = [1,2,3,4,5]

sqaure = [x**2 for x in range(1,6)]

print(sqaure)

even_square = [x**2 for x in range(1,6) if x%2 == 0]
print(even_square)