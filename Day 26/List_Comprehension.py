# LIST COMPREHENSION

number = [1,2,3]
new_numbers = [n + 1 for n in number]
print(new_numbers)

name  = "Pooja"
letters_list = [letter for letter in name]
print(letters_list)

# with RANGE
range_list = [ n*2 for n in range(1,5)]
print(range_list)



names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name.upper() for name in names if len(name) < 5]
print(short_names)




# 1.
# SQUARED NUMBERS
# create a new list called squared_numbers. This new list should contain every number in the list numbers but each number should be squared. 
# e.g. 4 * 4 = 16
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [i*i for i in numbers]
print(squared_numbers)



# 2.
# Filtering Even Numbers
# First, use list comprehension to convert the list_of_strings to a list of integers called numbers. 
list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
numbers = [int(i) for i in list_of_strings]
print(numbers)
# Then use list comprehension again to create a new list called result.
result = [i for i in numbers if i%2==0]
print(result)
