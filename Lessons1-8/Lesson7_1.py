# import random
#
# f = open("test1.txt", "wt")
#
# for i in range(200):
#     f.write(str(random.randint(100, 999)))
#
#     f.write('\n')
#
# f.close()
#
# test = open("test1.txt", "rt")
#
# word = test.readline()
#
# while word:
#     # Корисне навантаження
#
#     print(word)
#
#     word = test.readline()
#
# test.close()

#serialization-запаковка
import json
notes={"a":1,"b":2,"c": {"d":6,"f":2,"e":8}}
print(json.dumps(notes,sort_keys=True,indent=4))

with open("something.json","wt") as file:
    json.dump(notes, file)

#deseralization
a=json.dumps(notes,sort_keys=True, indent=4)
d_a=json.loads(a)
print(d_a["d"]["f"])
print(d_a)

with open("something.json","rt") as file:
    d_q = json.load(file)
print(d_q)