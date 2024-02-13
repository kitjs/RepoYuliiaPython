def splitter(file_name, step=2):
    file_full_name=file_name+".txt"
    file1_full_name=file_name+"1.txt"
    file2_full_name=file_name+"2.txt"
    f=open(file_full_name, "rt")
    f1=open(file1_full_name, "wt")
    f2=open(file2_full_name, "wt")
    a=f.readline()
    while a:
        f1.write(a)
        a=f.readline()
        f2.write(a)
        a=f.readline()
    f.close()
    f1.close()
    f2.close()

if __name__=="__main__":
    splitter("split/test0")

