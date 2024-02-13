#Files


# f=open("text.txt","wt")
# f.write("Hello! world!\n")
# f.write("My name is Yulia")
# f.close()

# #Read
# f=open("text.txt","rt")
# a=f.read()
# print(a)
# f.close()
#
# f=open("text.txt","at")
# f.write("Run test\n")
# f.close()


#
# calc=open("test2.txt","rt")
# l=calc.readlines()
# l.sort()
# for line in l:
#     print(line[:-1])
# calc.close()

#
# #print numbers in ASC
calc=open("test2.txt","rt")
l=calc.readlines()
l=set()
l=list(l)
l.sort()
for line in l:
    print(line[:-1])
calc.close()

# book=open("example.html", "rt")
# a=book.readlines()
# for line in a:
#     if "href=" in line:
#         b=line[line.find("http"):line.find("hreflang=")]
#         print(b)
# book.close()