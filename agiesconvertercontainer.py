#! /usr/bin/env python3
#SHEBANG
import re
#read this prgram from bottom to top for understanding

def aclinitial():
    with open("eosaclconf.csv","a") as eos:
        #eos.write("\n\n")
        eos.write(f"\n\nip access-list {filtername}")
        eos.write(f"\n!!{comment}")
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
                for row in open(filename):
                    #print(row)
                    if "port" in row:
                        portrow=rowcount
                    rowcount+= 1
                #print(portrow)
                rowcount  = 0
                for row in open(filename):
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
        eos.write("\ncounter per-entry")
        print("counter per-entry")

def agiesinitial():
    with open("eosagiesconf.csv","a") as eos:
        eos.write("\n\ntraffic-policies\n")

def agiessource():
    with open("eosagiesconf.csv","a") as eos:
        eos.write(f"field-set ipv4 prefix {filtername}-source")
        for srcad in srcadds:
            eos.write(f"\n{srcad}")  

def agiesdst():
    with open("eosagiesconf.csv","a") as eos:
        eos.write(f"\nfield-set ipv4 prefix {filtername}-destination")              
        for destad in destadds:
            eos.write(f"\n{destad}")          

def agiesprosrcdestport():
    with open("eosagiesconf.csv","a") as eos:
        eos.write(f"\ntraffic-policy {comment}\n")
        eos.write(f"match {comment} ipv4\n")
        eos.write(f"source prefix field-set {filtername}-source\n")
        eos.write(f"destination prefix field-set {filtername}-destination\n")
        for protoco in protocols:
            eos.write(f"protocol {protoco} destination port {port}")
        print("traffic-policies")
        print(f"field-set ipv4 prefix {filtername}-source")
        for srcad in srcadds:
            print(f"{srcad}")  
        print(f"field-set ipv4 prefix {filtername}-destination")              
        for destad in destadds:
            print(f"{destad}")
        print(f"traffic-policy {comment}")
        print(f"match {comment} ipv4")
        print(f"source prefix field-set {filtername}-source")
        print(f"destination prefix field-set {filtername}-destination")
        for protoco in protocols:
            print(f"protocol {protoco} destination port {port}")

def agiesprosrcdest():
    with open("eosagiesconf.csv","a") as eos:
        eos.write(f"\ntraffic-policy {comment}\n")
        eos.write(f"match {comment} ipv4\n")
        eos.write(f"source prefix field-set {filtername}-source\n")
        eos.write(f"destination prefix field-set {filtername}-destination\n")
        for protoco in protocols:
            eos.write(f"protocol {protoco}")
        print("traffic-policies")
        print(f"field-set ipv4 prefix {filtername}-source")
        for srcad in srcadds:
            print(f"{srcad}")  
        print(f"field-set ipv4 prefix {filtername}-destination")              
        for destad in destadds:
            print(f"{destad}")
        print(f"traffic-policy {comment}")
        print(f"match {comment} ipv4")
        print(f"source prefix field-set {filtername}-source")
        print(f"destination prefix field-set {filtername}-destination")
        for protoco in protocols:
            print(f"protocol {protoco}")
#remember majority conditions goes first
def aclconvert():
    end = 1
    localend = 1
    try:
        #remember majority conditions goes first
        if srcadd != 0 and destadd != 0 and protocol != 0 and port != 0 and count != 0 and deci != 0 and localend != 0:
            print("\nGenerating ACL....")     
            aclinitial()
            aclprosrcdestport()
            aclcount()
            print("\n Completed configruation generation.... \n")
            localend = 0 
            #nextiteration()
    except:
        end = 1
        localend = 1
    try:
        if srcadd != 0 and destadd != 0 and protocol != 0 and count != 0 and deci != 0 and localend != 0:
            print("\nGenerating ACL....")     
            aclinitial()
            aclprosrcdest()
            aclcount()
            print("\n Completed configruation generation.... \n")
            #end = 0 
            #nextiteration() 
    except: 
        end = 1
        localend = 1

#remember majority conditions goes first
def agiesconvert():
    end = 1
    localend = 1
    try:
        #remember majority conditions goes first
        if srcadd != 0 and destadd != 0 and protocol != 0 and port != 0 and count != 0 and deci != 0 and localend != 0:
            print("\nGenerating Agies Conf....")     
            agiesinitial()
            agiessource()
            agiesdst()
            agiesprosrcdestport()
            print("\n Completed configruation generation.... \n")
            localend = 0 
            #nextiteration()
    except:
        end = 1
        localend = 1
    try:
        if srcadd != 0 and destadd != 0 and protocol != 0 and count != 0 and deci != 0 and localend != 0:
            print("\nGenerating Agies Conf....")     
            agiesinitial()
            agiessource()
            agiesdst()
            agiesprosrcdest()
            print("\n Completed configruation generation.... \n")
            #end = 0 
            #nextiteration() 
    except: 
        end = 1
        localend = 1

#parse junos command for filtername
def parse():
    try:
        global port 
        port = 0
        global srcadd
        srcadd = 0
        global protocol
        protocol = 0
        global destadd
        destadd = 0
        global srcadds
        global destadds
        global inputs
        global value
        global protocols
        global count
        count = 0
        value = 0
        inputs = []
        srcadds = []
        destadds = []
        protocols = []
        with open(filename,"r") as file1:
            n1 = file1.readlines();
            global r1
            for r1 in n1:
                if filtername and comment in r1:
                        try:
                            if "source-address" in r1:
                                a = re.search(rf'\b(source-address)\b', r1)
                                fi = a.end()+1; 
                                l = len(r1)
                                o = r1[fi:l]
                                g = o.split(' ')
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
                                count = g[0].strip()
                                print(f"Found count: {count}")
                        except Exception as e: 
                                print(e)
                        try:
                            global deci
                            if "then" in r1:
                                a = re.search(rf'\b(then)\b', r1)
                                fi = a.end()+1; 
                                l = len(r1)
                                o = r1[fi:l]
                                g = o.split(' ')
                                decis = g[0].strip()
                                if decis == "accept":
                                    deci = "permit"
                                    print(f"Found decision: {deci}")
                                elif decis == "discard":
                                    deci = "deny"
                                    print(f"Found decision: {deci}")
                        except:
                                end=1;
                        try:
                            global srcprelist
                            if "source-prefix-list" in r1:
                                a = re.search(rf'\b(source-prefix-list)\b', r1)
                                fi = a.end()+1; 
                                l = len(r1)
                                o = r1[fi:l]
                                g = o.split(' ')
                                srcprelist = g[0].strip()
                                print(f"Found source-prefix-list: {srcprelist}")
                        except:
                                end=1;
                        try:
                            global destprelist
                            if "destination-prefix-list" in r1:
                                a = re.search(rf'\b(destination-prefix-list)\b', r1)
                                fi = a.end()+1; 
                                l = len(r1)
                                o = r1[fi:l]
                                g = o.split(' ')
                                destprelist = g[0].strip()
                                print(f"Found destination-prefix-list: {destprelist}")
                        except:
                                end=1;
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
                    
#parse junos command for filtername
def getfilternames():
    try:
        filternames = []
        with open(filename,"r") as file:
            n = file.readlines();
            for r in n:
                if "filter" and "term" in r:
                    f = r.index("filter")
                    a = re.search(r'\b(filter)\b', r)
                    fi = a.end()+1;
                    l = len(r)
                    o = r[fi:l]
                    g = o.split(' ')
                    filtername = g[0]
                    a = re.search(r'\b(term)\b', r)
                    fi = a.end()+1; 
                    l = len(r)
                    o = r[fi:l]
                    g = o.split(' ')
                    comment = g[0].strip()
                    filternames.append(f"{filtername};{comment}")
        global filterfinal
        filterfinal = []
        for filters in filternames:
            if filters not in filterfinal:
                filterfinal.append(filters)
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

#read the csv and do precheck
def precheck():
    try:
        open("eosaclconf.csv","w")
        open("eosagiesconf.csv","w")
        global filename
        global end
        print("Reading file 'junosconftest.csv' for inputs")
        print("outputs in 'eosaclconf.csv' & 'eosagiesconf.csv'")
        filename = "/Users/dp/Desktop/dp/testagiescoverter/junosconftest.csv"
        #filename = "junosconftest.csv"
        with open(filename,"r") as file:
            n = file.readlines();
            r = n[0]
            if "set firewall" in r:
                if "filter" in r:
                    end=1;
            else:
                end=0;
    except:
        print("Error: 'junosconftest.csv' must be in same folder or under '~/' if you run program from that location")
        exit()

def choice():
    global choose
    choose = input("Output needed is agies or acl[agies/acl]:")
    choose = choose.strip()
    #print(choose)
    if choose != "agies" and choose != "acl":
        print("Please type only agies or acl")
        choice()

def main():
    #just call functions in sequence order
    choice()
    precheck()
    #end= 1-continue ; 0-stop
    if end == 1:
        #get all filternames and terms
        getfilternames()
    else:
        print("Does not looks like a junos command. Please check the input")
        exit()
    for filters in filterfinal:
        sep = filters.split(';')
        global filtername
        global comment
        filtername = sep[0]
        comment = sep[1]
        print(f"Found filtername:{filtername}")
        print(f"Found Term:{comment}")
        parse()
        if choose == "agies":
            print("Agies Conversion started...")
            agiesconvert()
        elif choose == "acl":
            print("ACL Conversion started....")
            aclconvert()

if __name__=='__main__':
       main()