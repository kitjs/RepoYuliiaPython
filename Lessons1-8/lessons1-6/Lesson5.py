#List змінний. індексований. інтерований

l=[1,2,3,4,5,"Hello",True, 3.6, "Hello", "Hello world", [1,2,3]]



world="Hello"
count=0
for elem in l:
    if type(elem)==type("something") and  world in elem:
        count=count+1
        #count+=1

print(f'Count of word {world} : {count}')

colors=["orange","gray","white","black","yellow"]
print(colors)
colors.append("red")
print(colors)
colors.pop()
print(colors)
colors.pop(2)
print(colors)
colors.insert(3,"violet")
print(colors)

print(l)
t1=tuple(l)
print(t1)