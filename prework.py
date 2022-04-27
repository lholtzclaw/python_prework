# Question 1
# Write a function to print "hello_USERNAME!" 
# USERNAME is the input of the function.
# The first line of the code has been defined as below.

def hello_name(user_name):
    print("hello_" + user_name.upper() + "!")
user_name = input("Please enter your username: ")

hello_name(user_name)

# Question 2
# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing

def first_odds():
    first_odds = list(range(1,100,2))
    print(first_odds)

print(first_odds())

# Question 3
# Please write a Python function, max_num_in_list to return the max number of a given list.
# The first line of the code has been defined as below.

def max_number_in_list(a_list):
    print(max(a_list))
a_list = [63, 58, 1498, 2, 36]

max_number_in_list(a_list)

# Question 4
# Write a function to return if the given year is a leap year.
# A leap year is divisible dy 4, but not divisible by 100, unless it is also devisible by 400.
# The return should be boolean Type (true/false)

def is_leap_year(a_year):
    if a_year % 400 == 0:
        return True
    if a_year % 100 == 0:
        return False
    if a_year % 4 == 0:
        return True
    return False

print(is_leap_year(2008)) 

# Question 5
# Write a function to check to see if all numbers in list are consecutive numbers. 
# For example, [2,3,4,5,6,7] are consectuvive numbers, but [1,2,4,5] are not consecutive numbers. 
# The return should be Boolean type.

def is_consecutive(a_list):
    if len(set(a_list)) == len(a_list) and max(a_list) - min(a_list) == len(a_list) - 1:
        return True
    else:
        return False

a_list = [5, 6, 8]
print(is_consecutive(a_list))





