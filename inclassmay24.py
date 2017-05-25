names = ['chris', 'katie', 'chelsea']

for name in names:
    print(name)

# what if we want to find the index of an element in the list?


names = ['chris', 'katie', 'chelsea', 'chris']

for name in names:
    print(names.index(name))

# ut this will only give us the first index of an item even if there are multiples

for i in list(range(len(names))):
    print('{}: {}'.format(i, names[i]))

# note: the expression range(x1,x2) is only an expression, it does not store the 
# values it represents in memory. To place those values in memory you must do something like

x = list(range(1, 101))

print(x)


# eval - eval will take a string and run it as python code. holy shit that's fucking # awsome...

def make_list_of_strings(*args):
    return ' '.join(list(args))


lst = make_list_of_strings('the', 'cat', 'in', 'the', 'hat')

print(lst)


# **kwargs

def flower_colors(**kwargs):
    print(kwargs.items())


flower_colors(Chrysanthemum='red', Merigold='yellow')
