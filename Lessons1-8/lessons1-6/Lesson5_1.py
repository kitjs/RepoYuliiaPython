# set змінний,не індексований, інтегрований

s = {1, 2, 3, 4, 5, 6, 4, 3, 2, 1, 3, 4, 2}
print(3 in s)
print(s)

s2 = frozenset(s)
print(s2)

d = {'a': 1, "b": 2, "c": 3, "d": 4}
print(d)
print(d["b"])

for k in d:
    print(k, d[k])

print(d.items())

for k, v in d.items():
    print(k, v)

colors = {(255, 0, 0): "red", (0, 255, 0): "green", (0, 0, 255): "blue", (103, 78, 167): "purple",
          (212, 224, 54): "mustard",
          "red": (255, 0, 0), "green": (0, 255, 0), "blue": (0, 0, 255)}
while True:
    command = str(input("Enter command: [c],[r],[u],[d]:"))
    # crud
    # #create
    if command.lower() == 'c':
        key = str(input("Enter color name: "))
        value = str(input("Enter color value: "))
        colors[key] = value
    # #read
    elif command.lower() == "r":
        for key, value in colors.items():
            print(key, value)
    # #update
    elif command.lower() == "u":
        key = str(input("Enter color name: "))
        new_value = str(input("Enter color value: "))
        if key not in colors:
            way = str(input("This color is not present in colors. Are you want to add it?: [y] or [no]"))
            if way == "y":
                colors[key] = new_value
        elif key in colors:
            colors[key] = new_value
    # #delete
    elif command.lower() == "d":
        key = str(input("Enter color name: "))
        result = colors.pop(key, "Not present")
        print(f"Color {key} is deletes with result {result}")
