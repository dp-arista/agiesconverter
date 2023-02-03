#! /usr/bin/env python3
#SHEBANG
import re
import sys, os
#read this prgrom from bottom to top for understanding
#assign next filtername to filtername variable and start search
#end= 1-continue ; 0-stop
def check():
    try:
        if filtername1 != 0:
            filtername = filtername1
            comment = comment1
            print("Starting next config conversion....\n")
            print(f"Filter name: {filtername}")
            print(f"Term name: {comment}")
            print("Found different filternames and terms in csv we support only one filter set conversion at this time")
    except:
        end=1;
#read the next filtername
def nextiteration():
    with open(filename,"r") as file1:
        n1 = file1.readlines();
        global r1
        for r1 in n1:
            if filtername and comment in r1:
                continue
            else:
                a = re.search(r'\b(filter)\b', r1)
                fi = a.end()+1;
                l = len(r1)
                o = r1[fi:l]
                g = o.split(' ')
                global filtername1
                filtername1 = g[0]
                try:
                    a = re.search(r'\b(term)\b', r1)
                    fi = a.end()+1; 
                    l = len(r1)
                    o = r1[fi:l]
                    g = o.split(' ')
                    global comment1
                    comment1 = g[0].strip()
                except:
                    end=1;
                check()
                break

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
                rowcount  = 0
                for row in open(filename):
                    if "port" in row:
                        portrow=rowcount
                    rowcount+= 1
                rowcount  = 0
                for row in open(filename):
                    if "destination" in row:
                        destrow=rowcount  
                    rowcount+= 1
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
#conversion process
#remember majority conditions goes first
def convert():
    end = 1
    try:
        #remember majority conditions goes first
        if srcadd != 0 and destadd != 0 and protocol != 0 and port != 0 and count != 0 and deci != 0 and end != 0:
            print("\nGenerating ACL....")     
            aclinitial()
            aclprosrcdestport()
            aclcount()
            print("\nGenerating Agies Conf....")     
            agiesinitial()
            agiessource()
            agiesdst()
            agiesprosrcdestport()
            print("\n Completed configruation generation.... \n")
            nextiteration()
            end = 0
    except:
        end = 1
    try:
        if srcadd != 0 and destadd != 0 and protocol != 0 and count != 0 and deci != 0 and end != 0:
            print("\nGenerating ACL....")     
            aclinitial()
            aclprosrcdest()
            aclcount()
            print("\nGenerating Agies Conf....")     
            agiesinitial()
            agiessource()
            agiesdst()
            agiesprosrcdest()
            print("\n Completed configruation generation.... \n")
            nextiteration()
            end = 0   
    except: 
        end = 1
#parse junos command for filtername
def parse():
    with open(filename,"r") as file1:
        n1 = file1.readlines();
        global r1
        for r1 in n1:
            if filtername and comment in r1:
                    inputs.append(r1)
                    try:
                        if "source-address" in r1:
                            a = re.search(rf'\b(source-address)\b', r1)
                            fi = a.end()+1; 
                            l = len(r1)
                            o = r1[fi:l]
                            g = o.split(' ')
                            global srcadd
                            srcadd = g[0].strip()
                            srcadds.append(srcadd)
                            print(f"Found ipv4 source address: {srcadds}")
                    except:
                            end=1;
                    try:
                        if "destination-address" in r1:
                            a = re.search(rf'\b(destination-address)\b', r1)
                            fi = a.end()+1; 
                            l = len(r1)
                            o = r1[fi:l]
                            g = o.split(' ')
                            global destadd
                            destadd = g[0].strip()
                            destadds.append(destadd)
                            print(f"Found ipv4 destination address: {destadds}")
                    except:
                            end=1;
                    try:
                        if "protocol" in r1:
                            a = re.search(rf'\b(protocol)\b', r1)
                            fi = a.end()+1; 
                            l = len(r1)
                            o = r1[fi:l]
                            g = o.split(' ')
                            global protocol
                            protocol = g[0].strip()
                            protocols.append(protocol)
                            print(f"Found protocol: {protocol}")
                    except:
                            end=1;
                    try:
                        if "port" in r1:
                            a = re.search(rf'\b(port)\b', r1)
                            fi = a.end()+1; 
                            l = len(r1)
                            o = r1[fi:l]
                            g = o.split(' ')
                            global port
                            port = g[0].strip()
                            print(f"Found port: {port}")
                    except Exception as e: 
                            print(e)
                    try:
                        if "count" in r1:
                            a = re.search(rf'\b(count)\b', r1)
                            fi = a.end()+1; 
                            l = len(r1)
                            o = r1[fi:l]
                            g = o.split(' ')
                            global count
                            count = g[0].strip()
                            print(f"Found count: {count}")
                    except Exception as e: 
                            print(e)
                    try:
                        global deci
                        if "accept" in r1:
                            deci = "permit"
                        elif "discard" in r1:
                            deci = "deny"
                        print(f"Found decision: {deci}")
                    except:
                            end=1;
    print(f"\nComplete Input: \n{inputs}")
    print("\nStarting conversion process...")
    convert()     
#parse junos command for filtername
def getfiltername():
    #find the group name
    f = r.index("filter")
    a = re.search(r'\b(filter)\b', r)
    fi = a.end()+1;
    l = len(r)
    o = r[fi:l]
    g = o.split(' ')
    global filtername
    filtername = g[0]
    filternames.append(filtername)
    print(f"Filtername: {filtername}")
    try:
        a = re.search(r'\b(term)\b', r)
        fi = a.end()+1; 
        l = len(r)
        o = r[fi:l]
        g = o.split(' ')
        global comment
        comment = g[0].strip()
        print(f"Term: {comment}")
        parse()
    except Exception as ex:
        trace = []
        tb = ex.__traceback__
        while tb is not None:
            trace.append({
                "filename": tb.tb_frame.f_code.co_filename,
                "name": tb.tb_frame.f_code.co_name,
                "lineno": tb.tb_lineno
            })
            tb = tb.tb_next
        print(str({
            'type': type(ex).__name__,
            'message': str(ex),
            'trace': trace
        }))

#do the precheck
def precheck():
    if "set firewall" in r:
        if "filter" in r:
            getfiltername()
    else:
        end=1;

#read the csv
def readcsv():
    with open(filename,"r") as file:
        n = file.readlines();
        global r
        r = n[0]
        precheck()
            
#choose to read from csv or from manual command
def choose():
    global filename
    filename = "junosconftest.csv"
    readcsv();
    
def main():
    global srcadds
    global destadds
    global inputs
    global count
    global value
    global filternames
    global protocols
    count = 0
    value = 0
    inputs = []
    srcadds = []
    destadds = []
    protocols = []
    filternames = []
    term = []
    open("eosaclconf.csv","w")
    open("eosagiesconf.csv","w")
    choose()

if __name__=='__main__':
       main()