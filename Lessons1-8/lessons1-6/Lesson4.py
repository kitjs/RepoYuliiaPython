
#строки - незмінний.ітерований. індексований тип данних
s= "Hello world"
print(s)
print(s[0], s[1], s[2])

# незмінний - можна тільки перезаписати
s=s+"New"

#ітерований
d= "Hello world"
for elem in d:
    print(elem)

h="yuliia\" onopriienko"
print(h[5],h[6],h[7],h[8], h[9:11], h[13:])
print(h[::-1]*2)

n="yuliia\" onopri\nienko"
print(n)

#task2
text="fghfgh676576567"
alphabet="abcdefgklmnoprstqwxyz"
digits="0123456789"
dig_count=0
alph_count=0
for elem in text:
    if elem in alphabet:
        alph_count=alph_count+1
    elif elem in digits:
        dig_count=dig_count+1
print(dig_count,alph_count)



for elem in text:
    if elem.isalpha():
        alph_count=alph_count+1
    elif elem.isdigit():
        dig_count=dig_count+1
print(dig_count,alph_count)

