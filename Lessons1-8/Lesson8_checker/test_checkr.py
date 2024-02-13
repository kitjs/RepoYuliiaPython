import pytest
import os
import checker_funk

def test_split_positive():
    #precondition
    f=open("split/test0.txt","wt")
    f.write("hello world\n")
    f.write("!@#$%^&*()\n")
    f.write("Finish\n")
    f.close()
    #test
    checker_funk.splitter("split/test0")
    f1=open("split/test01.txt")
    assert f1.readline()=="hello world\n"
    assert f1.readline()=="Finish\n"
    f2=open("split/test02.txt")
    assert f2.readline()=="!@#$%^&*()\n"
    f1.close()
    f2.close()
    #postconditions

    os.remove("split/test0.txt")
    os.remove("split/test01.txt")
    os.remove("split/test02.txt")

