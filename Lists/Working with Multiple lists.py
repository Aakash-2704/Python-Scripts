
x = [1,2,3,4]
y = [5,6,7,8]

z = x+y
print(z)

x.extend(y)
print(x)

Name =["Aakash","Max","Murphy"]
Age=[27,30,35]
z = list(zip(Name,Age))
print(z)

name,age = zip(*z)
print(name)
print(age)
