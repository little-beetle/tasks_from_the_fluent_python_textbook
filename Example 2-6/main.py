# Cartesian product in a generator expression

colors = ['black', 'white']
sizes = ['S', 'M', 'L']
for t_shirt in (f'{c} {s}' for c in colors for s in sizes):
    print(t_shirt)