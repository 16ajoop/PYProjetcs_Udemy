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

