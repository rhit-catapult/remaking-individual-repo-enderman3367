###############################################################################
# DONE 1: Smile
###############################################################################
print("😊")

###############################################################################
# DONE 2:
#   With your instructor, read the code below. Try to predict what you will be
#   seeing on the console, then run the program and check your understanding.
###############################################################################

###############################################################################
# Part 1: Sequences
###############################################################################

# This is an empty sequence (or list):
#   A sequence is an ORDERED collection of items. The order in which you add things
#   the list matters.
my_list = []
print(my_list)

# Let's add a number to our sequence
# append is a METHOD inside of a list
my_list.append(123)

###############################################################################
# DONE 3:
#   Add a statement that print the list here
###############################################################################
print(my_list)

###############################################################################
# DONE 4:
#   Add a string to the list, can this be done?
#   To confirm, print the list after you add the string.
###############################################################################
my_list.append("Hello, World!")
print(my_list)

###############################################################################
# DONE 5: Indexing
#   What is we want to access the second element in the list? How can we do
#   that?
#   ALWAYS keep in mind that lists are indexed starting from 0.
#   Uncomment the following line of code.
###############################################################################
print(my_list[1])

###############################################################################
# DONE 6:
#   Add an additional integer to the sequence and then print the first element
#   followed by the THIRD element, but not the second.
###############################################################################
my_list.append(456)
print(my_list[0])
print(my_list[2])

###############################################################################
# DONE 7:
#   Try to print the fourth element, what do you think is going to happen?
###############################################################################
# print(my_list[3])  # This would cause an IndexError

###############################################################################
# Part 2: Loops
###############################################################################

###############################################################################
# DONE 8:
#   What if we want to print all numbers from 0 to 99? Do we insert 100
#   print statements? That would be horrible.
#   Luckily we can use for loops and while loops
#   Uncomment the following code.
###############################################################################
for i in range(0, 100):
    print(i)

###############################################################################
# DONE 9:
#   We can also do this using a while loop
###############################################################################
j = 0
while j < 100:
    print(j)
    j = j + 1

###############################################################################
# Part 3: Loop over sequences
###############################################################################

###############################################################################
# DONE 10:
#   What is we would like to go over the entries of a list one by one?
#   Uncomment the following code.
###############################################################################
for element in my_list:
    print(element)

###############################################################################
# DONE 11:
#   Can you do the above using a while loop?
#   Hint: Use indexing!
###############################################################################
k = 0
while k < len(my_list):
    print(my_list[k])
    k = k + 1
