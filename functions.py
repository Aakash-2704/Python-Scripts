def f():
    s = "I have started coding "
    print(s)
f()   

print("----------------------------------------------------------------------")

def f():
    print("Printing inside a function",s)  #Priting inside a function.

#Global scope
s = "I have started coding "
f()
print("Printing outside a function",s)    #Printing outside the function.

print("----------------------------------------------------------------------")

def f():
    s= "Printing a local variable"      # Local variable
    print(s)  

s = "Printing a global variable" # Global Variable 
f()
print(s)

print("----------------------------------------------------------------------")

#loop a statement 