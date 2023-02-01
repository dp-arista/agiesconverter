from convert import *
from agiesconverter import *

def aclinitial():
    with open("eosaclconf.csv","a") as eos:
        eos.write(f"ip access-list {filtername}")
        eos.write(f"\n")
        eos.write(f"!!{comment}")
        print(f"ip access-list {filtername}")
        print(f"!!{comment}")

def aclprosrcdestport():
    with open("eosaclconf.csv","a") as eos:
        rowcount  = 0
        for srcad in srcadds:
            for destad in destadds:
                eos.write(f"\n")
                #Setting initial value of the counter to zero
                rowcount  = 0
                #iterating through the whole file
                for row in open("/Users/dp/Desktop/dp/agiesconverter/junosconftest.csv"):
                    #print(row)
                    if "port" in row:
                        portrow=rowcount
                    rowcount+= 1
                #print(portrow)
                rowcount  = 0
                for row in open("/Users/dp/Desktop/dp/agiesconverter/junosconftest.csv"):
                    if "destination" in row:
                        destrow=rowcount  
                    rowcount+= 1
                #print(destrow) 
                if portrow > destrow:
                    eos.write(f"{deci} {protocol} {srcad} {destad} eq {port}")
                    print(f"{deci} {protocol} {srcad} {destad} eq {port}")
                else:
                    eos.write(f"{deci} {protocol} {srcad} eq {port} {destad} ")
                    print(f"{deci} {protocol} {srcad} eq {port} {destad} ")               

def aclprosrcdest():
    with open("eosaclconf.csv","a") as eos:
        for srcad in srcadds:
            for destad in destadds:
                eos.write(f"\n")
                eos.write(f"{deci} {protocol} {srcad} {destad}")
                print(f"{deci} {protocol} {srcad} {destad}")

def aclcount():
    with open("eosaclconf.csv","a") as eos:
        eos.write("\n")
        eos.write("counter per-entry")
        print("counter per-entry")

def agiesinitial():
    with open("eosagiesconf.csv","a") as eos:
        eos.write("traffic-policies")
        eos.write("\n")

def agiessource():
    with open("eosagiesconf.csv","a") as eos:
        eos.write(f"field-set ipv4 prefix {filtername}-source")
        for srcad in srcadds:
            eos.write(f"\n")
            eos.write(f"{srcadd}")  

def agiesdst():
    with open("eosagiesconf.csv","a") as eos:
        eos.write(f"\n")
        eos.write(f"field-set ipv4 prefix {filtername}-destination")              
        for destad in destadds:
            eos.write(f"\n")
            eos.write(f"{destadd}")          

def agiesprosrcdestport():
    with open("eosagiesconf.csv","a") as eos:
        eos.write("\n")
        eos.write(f"traffic-policy {comment}\n")
        eos.write(f"match {comment} ipv4\n")
        eos.write(f"source prefix field-set {filtername}-source\n")
        eos.write(f"destination prefix field-set {filtername}-destination\n")
        for protoco in protocols:
            eos.write(f"protocol {protoco} destination port {port}")
        print("traffic-policies")
        print(f"field-set ipv4 prefix {filtername}-source")
        for srcad in srcadds:
            print(f"{srcadd}")  
        print(f"field-set ipv4 prefix {filtername}-destination")              
        for destad in destadds:
            print(f"{destadd}")
        print(f"traffic-policy {comment}")
        print(f"match {comment} ipv4")
        print(f"source prefix field-set {filtername}-source")
        print(f"destination prefix field-set {filtername}-destination")
        for protoco in protocols:
            print(f"protocol {protoco} destination port {port}")

def agiesprosrcdest():
    with open("eosagiesconf.csv","a") as eos:
        eos.write("\n")
        eos.write(f"traffic-policy {comment}\n")
        eos.write(f"match {comment} ipv4\n")
        eos.write(f"source prefix field-set {filtername}-source\n")
        eos.write(f"destination prefix field-set {filtername}-destination\n")
        for protoco in protocols:
            eos.write(f"protocol {protoco}")
        print("traffic-policies")
        print(f"field-set ipv4 prefix {filtername}-source")
        for srcad in srcadds:
            print(f"{srcadd}")  
        print(f"field-set ipv4 prefix {filtername}-destination")              
        for destad in destadds:
            print(f"{destadd}")
        print(f"traffic-policy {comment}")
        print(f"match {comment} ipv4")
        print(f"source prefix field-set {filtername}-source")
        print(f"destination prefix field-set {filtername}-destination")
        for protoco in protocols:
            print(f"protocol {protoco}")

