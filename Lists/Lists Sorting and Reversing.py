numbers = [4,0,7,1,2,3]

print(numbers)        #1st output              

numbers.sort()                         # Soriting the numbers according to ascending order

print(numbers)        # 2nd output

numbers.sort(reverse=True)             # Sorting and reversing the numbers 

print(numbers)        # 3rd output

numbers.reverse()                      # Reversing the given number

print(numbers)         # 4th output


reverse_numbers =numbers[::-1]

print(reverse_numbers)    # 5th output

# Optional 

fruits = ["banana","Orange","apple","KIWI","PINEapple"]  # Sorting the list according to Alphabetical order where Capital
                                                         # letters first and then small letters

fruits.sort()

print(fruits)
