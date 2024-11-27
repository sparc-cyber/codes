# Strings
print("Hello World!")
print('Hello World!')

print("""Diplays text in 
      Multi-line Format.""") # triple double-quotes for multi-line output printing

print('This is a '+'single string') # string concatenation

print('\n') # new line

print("To test the new line")

print('\n')

### Varibales
greetings = ('Hello, Good Morning')
print(greetings)

### FUNCTIONS ###

### String Length - len()
print(len(greetings))

numbers = {1,2,3,4,5,6,7,8}
length = len(numbers)
print(length)

### String Slicing
substring = greetings[7:]
print(substring)

substring2 =greetings[7:12]
print(substring2)

### upper() function
upper = greetings.upper()
print(upper)

### lower() function
lower = greetings.lower()
print(lower)

### strip() function
whoami = "      I am an Ethical Hacker    "
strip = whoami.strip()
print(strip) # Removes leading and trailing whitespaces (or specified characters) from a string.

### split() function
split = greetings.split()
print(split)

### replace() function
replace = greetings.replace("Morning","Evening")
print(replace) # replaces words in a text file accordingly

### title() function
quote = "have a nice day !!!"
title = quote.title()
print(title) #captilaize the first letters in every words in a string