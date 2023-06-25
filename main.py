import name_search
import os
from os import listdir
from os.path import isfile, join


def pdflist():
    mypath=""

    mypath=os.path.abspath(__file__)

    while mypath[len(mypath)-1]!='\\':
        mypath=mypath[:-1]

    onlypdf = [f for f in listdir(mypath) if isfile(join(mypath, f))]

    i=0
    while True:
        if i>=len(onlypdf):
            break
        if onlypdf[i][-4:]!='.pdf':
            onlypdf.remove(onlypdf[i])
            i-=1
        i+=1

    return onlypdf

def main(name):
    List_of_pdf = pdflist()

    for i in List_of_pdf:
        print("В файле " + i + " название ОКС\n")
        print(name)
        print("\nНазвания ОКС внутри файла:\n")
        Name_in_file=name_search.main(i,name)
        print(Name_in_file)
        os.remove(i)
    return 0


