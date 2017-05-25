names = ['Chris', 'Katie']

names.append('Chelsea')

# pop will remove the last item from the list and return it to a variable

first_popped = names.pop()

print(first_popped)

# if we just want to delete we can can use del

del names[0]

print(names)
