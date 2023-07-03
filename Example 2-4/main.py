# Cartesian product using a list comprehension

colors = ['black', 'white']
sizes = ['S', 'M', 'L']

# the first way
t_shirts_1 = [(color, size) for color in colors for size in sizes]
print(t_shirts_1)

# the second way
for color in colors:
    for size in sizes:
        print((color, size))

# the third way
t_shirts_2 = [(color, size) for size in sizes for color in colors]
print(t_shirts_2)


