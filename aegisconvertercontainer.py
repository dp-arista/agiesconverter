#! /usr/bin/env python3
#SHEBANG
import re
#read this prgram from bottom to top for understanding

def aclinitial():
    with open("eosaclconf.csv","a") as eos:
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

def aegisaction():
    try:
        with open("eosaegisconf.csv","a") as eos:
            eos.write("actions\n")
            print("actions")
            if count != 0:
                eos.write("count\n")
                print("count")
            if deci == "deny":
                eos.write("drop\n")
                print("drop")
            eos.write("\n")
    except:
        end = 1

def aegisprotocol():
    with open("eosaegisconf.csv","a") as eos:
        try:
            if srcport != 0 and destiport != 0:
                eos.write(f"protocol tcp source port {srcport} destination port {destiport}\n")
                eos.write(f"protocol udp source port {srcport} destination port {destiport}\n")
                print(f"protocol tcp source port {srcport} destination port {destiport}")
                print(f"protocol udp source port {srcport} destination port {destiport}")
        except:
            end = 1
        try:        
            if destiport != 0 and srcport == 0:
                eos.write(f"protocol tcp destination port {destiport}\n")
                eos.write(f"protocol udp destination port {destiport}\n")
                print(f"protocol tcp destination port {destiport}")
                print(f"protocol udp destination port {destiport}")
        except:
            end = 1
        try:        
            if destiport == 0 and srcport != 0:
                eos.write(f"protocol tcp source port {srcport}\n")
                eos.write(f"protocol udp source port {srcport}\n")
                print(f"protocol tcp source port {srcport}")
                print(f"protocol udp source port {srcport}")
        except:
            end = 1
        try:
            if protocol != 0 and port != 0:
                rowcount  = 0
                destrow = 0
                for row in open(filename):
                    #print(row)
                    if (filtername in row) and (comment in row) and ("port" in row):
                        portrow=rowcount    
                    rowcount+= 1
                #print(portrow)
                rowcount  = 0
                for row in open(filename):
                    if (filtername in row) and (comment in row) and ("destination" or "source" in row):
                        destrow=rowcount 
                    rowcount+= 1
                #print(destrow) 
                if portrow > destrow:
                    for protoco in protocols:
                        eos.write(f"protocol {protoco} source port {port}\n")
                        print(f"protocol {protoco} source port {port}")   
                else:
                    for protoco in protocols:
                        eos.write(f"protocol {protoco} destination port {port}\n")
                        print(f"protocol {protoco} destination port {port}")                
        except:
            end = 1            


def aegisprefix():
    with open("eosaegisconf.csv","a") as eos:
        try:
            if srcprelist != 0:
                eos.write(f"source prefix field-set {srcprelist}\n")
                print(f"source prefix field-set {srcprelist}")
        except:
            end = 1
        try:
            if destprelist != 0:
                eos.write(f"destination prefix field-set {destprelist}\n")
                print(f"destination prefix field-set {destprelist}")
        except:
            end = 1;
        try:
            if srcadd != 0:
                eos.write(f"source prefix field-set {filtername}-source\n")
                print(f"source prefix field-set {filtername}-source")
        except:
            end = 1
        try:
            if destadd != 0:
                eos.write(f"destination prefix field-set {filtername}-destination\n")
                print(f"destination prefix field-set {filtername}-destination")
        except:
            end = 1

def aegistrafficpolicy():
    with open("eosaegisconf.csv","a") as eos:
        eos.write("traffic-policies\n")
        print("traffic-policies")
        eos.write(f"traffic-policy {filtername}\n")
        print(f"traffic-policy {filtername}")
        localend = 1
        try:
            if ('.' in srcadd) and localend != 0:
                eos.write(f"match {comment} ipv4\n")
                print(f"match {comment} ipv4")
            elif ':' in srcadd:
                eos.write(f"match {comment} ipv6\n")
                print(f"match {comment} ipv6")
            localend = 0
        except:
            end = 1
        try:
            if ('.' in destadd) and localend != 0:
                eos.write(f"match {comment} ipv4\n")
                print(f"match {comment} ipv4")
            elif ':' in destadd:
                eos.write(f"match {comment} ipv6\n")
                print(f"match {comment} ipv6")
            localend = 0
        except:
            end = 1
        try:
            if '.' in src and localend != 0:
                eos.write(f"match {comment} ipv4\n")
                print(f"match {comment} ipv4")
            elif ':' in src:
                eos.write(f"match {comment} ipv6\n")
                print(f"match {comment} ipv6")
            localend = 0
        except:
            end = 1
        try:
            if '.' in dest and localend != 0:
                eos.write(f"match {comment} ipv4\n")
                print(f"match {comment} ipv4")
            elif ':' in dest:
                eos.write(f"match {comment} ipv6\n")
                print(f"match {comment} ipv6")
            localend = 0
        except:
            end = 1
        if localend != 0:
            eos.write(f"!!Not able to find match {comment} ipv4 or ipv6\n")
            print(f"!!Not able to find match {comment} ipv4 or ipv6")
        
def aegisfieldset():
    if srcadd != 0:
        with open("eosaegisconf.csv","a") as eos:
            eos.write(f"field-set ipv4 prefix {filtername}-source\n")
            print(f"field-set ipv4 prefix {filtername}-source")
            for srcad in srcadds:
                eos.write(f"{srcad}\n")
                print(f"{srcad}")
    if destadd != 0:
        with open("eosaegisconf.csv","a") as eos:
            eos.write(f"field-set ipv4 prefix {filtername}-destination\n")
            print(f"field-set ipv4 prefix {filtername}-destination")              
            for destad in destadds:
                eos.write(f"{destad}\n")
                print(f"{destad}")  
    if destprelist != 0:
        destas = []
        with open(filename,"r") as file2:
            n2 = file2.readlines();
            for r2 in n2:
                #print(r2)
                try:
                    if destprelist in r2:
                        a = re.search(rf'\b( prefix-list {destprelist})\b',r2)
                        fi = a.end()+1; 
                        l = len(r2)
                        o = r2[fi:l]
                        g = o.split(' ')
                        desta = g[0].strip()
                        destas.append(desta)
                except:
                        end=1;
        with open("eosaegisconf.csv","a") as eos:
            eos.write(f"field-set ipv4 prefix {destprelist}\n")
            print(f"field-set ipv4 prefix {destprelist}")
            global dest              
            for dest in destas:
                eos.write(f"{dest}\n")
                print(f"{dest}")
    if srcprelist != 0:
        srcas = []
        with open(filename,"r") as file2:
            n2 = file2.readlines();
            for r2 in n2:
                #print(r2)
                try:
                    if srcprelist in r2:
                        a = re.search(rf'\b( prefix-list {srcprelist})\b',r2)
                        fi = a.end()+1; 
                        l = len(r2)
                        o = r2[fi:l]
                        g = o.split(' ')
                        srca = g[0].strip()
                        srcas.append(srca)
                except:
                        end=1;
        with open("eosaegisconf.csv","a") as eos:
            eos.write(f"field-set ipv4 prefix {srcprelist}\n")
            print(f"field-set ipv4 prefix {srcprelist}")
            global src              
            for src in srcas:
                eos.write(f"\n{src}")
                print(f"{src}")  

#remember majority conditions goes first
def aclconvert():
    end = 1
    localend = 1
    try:
        if (srcprelist != 0 or destprelist !=0) and count != 0 and deci != 0 and localend != 0:
            print("\nNot Generating ACL Conf....")
            localend = 0     
    except:
        end = 1
    try:
        #remember majority conditions goes first
        if srcadd != 0 and destadd != 0 and protocol != 0 and port != 0 and count != 0 and deci != 0 and localend != 0:
            print("\nGenerating ACL....")     
            aclinitial()
            aclprosrcdestport()
            aclcount()
            print("\n Completed configuration generation.... \n")
            localend = 0   
    except:
        end = 1
    try:
        if srcadd != 0 and destadd != 0 and protocol != 0 and count != 0 and deci != 0 and localend != 0:
            print("\nGenerating ACL....")     
            aclinitial()
            aclprosrcdest()
            aclcount()
            print("\n Completed configuration generation.... \n")
            #end = 0 
    except: 
        end = 1


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
        global srcprelist
        srcprelist = 0
        global destprelist
        destprelist = 0
        global destiport
        destiport = 0
        global srcport
        srcport = 0
        global deci
        deci = 0
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
                                print(f"Found protocol: {protocols}")
                        except:
                                end=1;
                        try:
                            if " port" in r1:
                                a = re.search(rf'\b( port)\b', r1)
                                fi = a.end()+1; 
                                l = len(r1)
                                o = r1[fi:l]
                                g = o.split(' ')
                                port = g[0].strip()
                                print(f"Found port: {port}")
                        except:
                                end=1;
                        try:
                            if "count" in r1:
                                a = re.search(rf'\b(count)\b', r1)
                                fi = a.end()+1; 
                                l = len(r1)
                                o = r1[fi:l]
                                g = o.split(' ')
                                count = g[0].strip()
                                print(f"Found count: {count}")
                        except:
                                end = 1
                        try:
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
                        try:
                            if "destination-port" in r1:
                                a = re.search(rf'\b(destination-port)\b', r1)
                                fi = a.end()+1; 
                                l = len(r1)
                                o = r1[fi:l]
                                g = o.split(' ')
                                destiport = g[0].strip()
                                print(f"Found destination-port: {destiport}")
                        except:
                                end=1;
                        try:
                            if "source-port" in r1:
                                a = re.search(rf'\b(source-port)\b', r1)
                                fi = a.end()+1; 
                                l = len(r1)
                                o = r1[fi:l]
                                g = o.split(' ')
                                srcport = g[0].strip()
                                print(f"Found source-port: {srcport}")
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
        open("eosaegisconf.csv","w")
        global filename
        global end
        print("Reading file 'junosconftest.csv' for inputs")
        print("outputs in 'eosaclconf.csv' & 'eosaegisconf.csv'")
        filename = "junosconftest.csv"
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
    choose = input("Output needed is aegis or acl[aegis/acl]:")
    choose = choose.strip()
    #print(choose)
    if choose != "aegis" and choose != "acl":
        print("Please type only aegis or acl")
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
        print(f"\nFound filtername:{filtername}")
        print(f"Found Term:{comment}")
        parse()
        if choose == "aegis":
            print("\nAegis Conversion started...")
            print("Generating aegis Conf....")   
            aegisfieldset()  
            aegistrafficpolicy()
            aegisprefix()
            aegisprotocol()
            aegisaction()
            print("\n Completed configuration generation....")
        elif choose == "acl":
            print("ACL Conversion started....")
            aclconvert()

if __name__=='__main__':
       main()