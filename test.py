#! /usr/bin/env python3
#SHEBANG
import re
import json
#read this prgrom from bottom to top for understanding

#read the next filtername
def nextiteration():
    value = count+1
    with open("junosconftest.csv","r") as file1:
        n1 = file1.readlines();
        global r1
        for r1 in n1:
            if filtername and comment in r1:
                continue
            else:
                a = re.search(r'\b(filter)\b', r1)
                #print(a.end())
                #print(f)
                fi = a.end()+1;
                #print(fi)
                #print(r)
                l = len(r1)
                #print(l)
                o = r1[fi:l]
                g = o.split(' ')
                global filtername1
                filtername1 = g[0]
                #print(f"Filtername: {filtername1}")
                try:
                    a = re.search(r'\b(term)\b', r1)
                    #print(a.end())
                    #print(f)
                    fi = a.end()+1; 
                    l = len(r1)
                    o = r1[fi:l]
                    g = o.split(' ')
                    global comment1
                    comment1 = g[0].strip()
                    #print(f"Term: {comment1}")
                except:
                    #print("No term")
                    i=0;
                check()

def check():
    try:
        if filtername1 != 0:
            filtername = filtername1
            parse()
    except:
        i=0;
    

def main():
    global srcadds
    global destadds
    global inputs
    global count
    global value
    global filtername
    global comment
    count = 0
    value = 0
    inputs = []
    srcadds = []
    destadds = []
    filtername = "EDGE-L3MOSS-IN"
    comment = "10"
    term = []
    open("eosaclconf.csv","w")
    open("eosagiesconf.csv","w")
    parse()


if __name__=='__main__':
       main()