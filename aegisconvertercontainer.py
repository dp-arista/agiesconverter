#! /usr/bin/env python3
#SHEBANG

#All modules used in this code are default modules no pip instal _ needed
import re
import csv
import argparse

#read this prgram from bottom to top for understanding
#More infromation check: https://sites.google.com/arista.com/msft-team/interns-embark-portal-projects-and-trainings/dinesh-kumardp-2022/projects/moving-to-aegis-cli


#if count in decision on acl
def aclcount():
    if count != 0:
        with open(outputfilename,"a") as eos:
            eos.write("counter per-entry\n")
            print("counter per-entry")

#aclcondition contains all main conversion            
def aclcondition():
    with open(outputfilename,"a") as eos:
        #with protocol and source and destination prefixlist
        #if protocol, source prefix list, source-port(srcport), destination prefix list, destination-port(destiport) are present ; port after source(port), port after destination(port) are not present;
        if (protocol != 0) and (srcprelist != 0)  and (srcport != 0) and (destprelist != 0) and (destiport != 0) and (port == 0):
            for protoco in protocols:
                for src in srcas:
                    for dest in destas:
                        for srcportjoin in srcportjoinfinal:
                            for destasportjoin in destasportjoinfinal:
                                eos.write(f"{deci} {protoco} {src} {srcportjoin} {dest} {destasportjoin}\n")
                                print(f"{deci} {protoco} {src} {srcportjoin} {dest} {destasportjoin}")
        elif (protocol != 0) and (srcprelist == 0)  and (srcport == 0) and (destprelist != 0) and (destiport == 0) and (port != 0):
            for protoco in protocols:
                    for dest in destas:
                        for por in ports:
                            eos.write(f"{deci} {protoco} any {dest} {por}\n")
                            print(f"{deci} {protoco} any {dest} {por}")
                            eos.write(f"{deci} {protoco} any {por} {dest}\n")
                            print(f"{deci} {protoco} any {por} {dest}")
        elif (protocol != 0) and (srcprelist != 0)  and (srcport == 0) and (destprelist == 0) and (destiport == 0) and (port != 0):
            for protoco in protocols:
                for src in srcas:
                    for por in ports:
                        eos.write(f"{deci} {protoco} {src} any {por} \n")
                        print(f"{deci} {protoco} {src} any {por}")
                        eos.write(f"{deci} {protoco} {src} {por} any \n")
                        print(f"{deci} {protoco} {src} {por} any")
        elif (protocol != 0) and (srcprelist == 0)  and (srcport != 0) and (destprelist == 0) and (destiport == 0) and (port != 0):
            for protoco in protocols:
                for srcportjoin in srcportjoinfinal:
                    for por in ports:
                        eos.write(f"{deci} {protoco} any {srcportjoin} any {por}\n")
                        print(f"{deci} {protoco} any {srcportjoin} any {por}")
        elif (protocol != 0) and (srcprelist == 0)  and (srcport == 0) and (destprelist != 0) and (destiport == 0) and (port != 0):
            for protoco in protocols:
                for dest in destas:
                    for por in ports:
                        eos.write(f"{deci} {protoco} any {dest} {por} \n")
                        print(f"{deci} {protoco} any {dest} {por}")
                        eos.write(f"{deci} {protoco} any {por} {dest} \n")
                        print(f"{deci} {protoco} any {por} {dest}")
        elif (protocol != 0) and (srcprelist == 0)  and (srcport == 0) and (destprelist == 0) and (destiport != 0) and (port != 0):
            for protoco in protocols:
                for destasportjoin in destasportjoinfinal:
                    for por in ports:
                        eos.write(f"{deci} {protoco} any {por} any {destasportjoin}\n")
                        print(f"{deci} {protoco} any {por} any {destasportjoin}")
        elif (protocol != 0) and (srcprelist != 0)  and (srcport != 0) and (destprelist != 0) and (destiport == 0) and (port != 0):
            for protoco in protocols:
                for src in srcas:
                    for dest in destas:
                        for srcportjoin in srcportjoinfinal:
                            for por in ports:
                                eos.write(f"{deci} {protoco} {src} {dest} {por}\n")
                                print(f"{deci} {protoco} {src} {dest} {por}")
                                eos.write(f"{deci} {protoco} {src} {por} {dest}\n")
                                print(f"{deci} {protoco} {src} {por} {dest}")
                                eos.write(f"{deci} {protoco} {src} {srcportjoin} {dest} \n")
                                print(f"{deci} {protoco} {src} {srcportjoin} {dest}")
        elif (protocol != 0) and (srcprelist != 0)  and (srcport != 0) and (destprelist == 0) and (destiport == 0) and (port != 0):
            for protoco in protocols:
                for src in srcas:
                    for srcportjoin in srcportjoinfinal:
                        for por in ports:
                            eos.write(f"{deci} {protoco} {src} any {por}\n")
                            print(f"{deci} {protoco} {src} any {por}")
                            eos.write(f"{deci} {protoco} {src} {por} any\n")
                            print(f"{deci} {protoco} {src} {por} any")
                            eos.write(f"{deci} {protoco} {src} {srcportjoin} any\n")
                            print(f"{deci} {protoco} {src} {srcportjoin} any")
        elif (protocol != 0) and (srcprelist == 0)  and (srcport != 0) and (destprelist != 0) and (destiport == 0) and (port != 0):
            for protoco in protocols:
                for dest in destas:
                    for srcportjoin in srcportjoinfinal:
                        for por in ports:
                            eos.write(f"{deci} {protoco} {src} {dest} {por}\n")
                            print(f"{deci} {protoco} {src} {dest} {por}")
                            eos.write(f"{deci} {protoco} {src} {por} {dest}\n")
                            print(f"{deci} {protoco} {src} {por} {dest}")
                            eos.write(f"{deci} {protoco} any {srcportjoin} {dest} \n")
                            print(f"{deci} {protoco} any {srcportjoin} {dest}")
        elif (protocol != 0) and (srcprelist != 0)  and (srcport == 0) and (destprelist != 0) and (destiport == 0) and (port != 0):
            for protoco in protocols:
                for src in srcas:
                    for dest in destas:
                        for por in ports:
                            eos.write(f"{deci} {protoco} {src} {dest} {por}\n")
                            print(f"{deci} {protoco} {src} {dest} {por}")
                            eos.write(f"{deci} {protoco} {src} {por} {dest}\n")
                            print(f"{deci} {protoco} {src} {por} {dest}")
                            eos.write(f"{deci} {protoco} {src} {dest}\n")
                            print(f"{deci} {protoco} {src} {dest}")
        elif (protocol != 0) and (srcprelist == 0)  and (srcport == 0) and (destprelist == 0) and (destiport != 0) and (port != 0):
            for protoco in protocols:
                for destasportjoin in destasportjoinfinal:
                    for por in ports:
                        eos.write(f"{deci} {protoco} {src} {dest} {por}\n")
                        print(f"{deci} {protoco} {src} {dest} {por}")
                        eos.write(f"{deci} {protoco} {src} {por} {dest}\n")
                        print(f"{deci} {protoco} {src} {por} {dest}")
                        eos.write(f"{deci} {protoco} any any {destasportjoin} \n")
                        print(f"{deci} {protoco} any any {destasportjoin}")
        elif (protocol != 0) and (srcprelist != 0)  and (srcport == 0) and (destprelist == 0) and (destiport != 0) and (port != 0):
            for protoco in protocols:
                for src in srcas:
                    for destasportjoin in destasportjoinfinal:
                        for por in ports:
                            eos.write(f"{deci} {protoco} {src} {dest} {por}\n")
                            print(f"{deci} {protoco} {src} {dest} {por}")
                            eos.write(f"{deci} {protoco} {src} {por} {dest}\n")
                            print(f"{deci} {protoco} {src} {por} {dest}")
                            eos.write(f"{deci} {protoco} {src} any {destasportjoin} \n")
                            print(f"{deci} {protoco} {src} any {destasportjoin}")             
        elif (protocol != 0) and (srcprelist == 0)  and (srcport != 0) and (destprelist == 0) and (destiport == 0) and (port != 0):
            for protoco in protocols:
                for srcportjoin in srcportjoinfinal:
                    for por in ports:
                        eos.write(f"{deci} {protoco} {src} {dest} {por}\n")
                        print(f"{deci} {protoco} {src} {dest} {por}")
                        eos.write(f"{deci} {protoco} {src} {por} {dest}\n")
                        print(f"{deci} {protoco} {src} {por} {dest}")
                        eos.write(f"{deci} {protoco} any {srcportjoin} any\n")
                        print(f"{deci} {protoco} any {srcportjoin} any")
        elif (protocol != 0) and (srcprelist == 0)  and (srcport != 0) and (destprelist != 0) and (destiport != 0) and (port == 0):
            for protoco in protocols:
                for dest in destas:
                    for srcportjoin in srcportjoinfinal:
                        for destasportjoin in destasportjoinfinal:
                            eos.write(f"{deci} {protoco} any {srcportjoin} {dest} {destasportjoin} \n")
                            print(f"{deci} {protoco} any {srcportjoin} {dest} {destasportjoin} ") 
        elif (protocol != 0) and (srcprelist != 0)  and (srcport == 0) and (destprelist != 0) and (destiport != 0) and (port != 0):
            for protoco in protocols:
                for src in srcas:
                    for dest in destas:
                        for srcportjoin in srcportjoinfinal:
                            for destasportjoin in destasportjoinfinal:
                                for por in ports:
                                    eos.write(f"{deci} {protoco} {src} {dest} {por}\n")
                                    print(f"{deci} {protoco} {src} {dest} {por}")
                                    eos.write(f"{deci} {protoco} {src} {por} {dest}\n")
                                    print(f"{deci} {protoco} {src} {por} {dest}")
                                    eos.write(f"{deci} {protoco} {src} {dest} {destasportjoin}\n")
                                    print(f"{deci} {protoco} {src} {dest} {destasportjoin}")
        elif (protocol != 0) and (srcprelist != 0)  and (srcport != 0) and (destprelist == 0) and (destiport != 0) and (port == 0):
            for protoco in protocols:
                for src in srcas:
                    for srcportjoin in srcportjoinfinal:
                        for destasportjoin in destasportjoinfinal:
                            eos.write(f"{deci} {protoco} {src} {srcportjoin} any {destasportjoin}\n")
                            print(f"{deci} {protoco} {src} {srcportjoin} any {destasportjoin}")
        elif (protocol != 0) and (srcprelist == 0)  and (srcport != 0) and (destprelist == 0) and (destiport != 0) and (port == 0):
            for protoco in protocols:
                for src in srcas:
                    for srcportjoin in srcportjoinfinal:
                        for destasportjoin in destasportjoinfinal:
                            eos.write(f"{deci} {protoco} any {srcportjoin} any {destasportjoin}\n")
                            print(f"{deci} {protoco} any {srcportjoin} any {destasportjoin}")
        elif (protocol != 0) and (srcprelist == 0)  and (srcport == 0) and (destprelist == 0) and (destiport == 0) and (port != 0):
            for protoco in protocols:
                for por in ports:
                    eos.write(f"{deci} {protoco} any any {por}\n")
                    print(f"{deci} {protoco} any any {por}")
                    eos.write(f"{deci} {protoco} any {por} any\n")
                    print(f"{deci} {protoco} any {por} any")
        #without protocol with source and destination prefixlist
        elif (protocol == 0) and (srcprelist != 0)  and (srcport != 0) and (destprelist != 0) and (destiport != 0) and (port == 0):
            for src in srcas:
                for dest in destas:
                    for srcportjoin in srcportjoinfinal:
                        for destasportjoin in destasportjoinfinal:
                            eos.write(f"{deci} ip {src} {srcportjoin} {dest} {destasportjoin}\n")
                            print(f"{deci} ip {src} {srcportjoin} {dest} {destasportjoin}")
        elif (protocol == 0) and (srcprelist != 0)  and (srcport == 0) and (destprelist == 0) and (destiport == 0) and (port != 0):
            for src in srcas:
                eos.write(f"{deci} ip {src} any \n")
                print(f"{deci} ip {src} any ")
        elif (protocol == 0) and (srcprelist == 0)  and (srcport != 0) and (destprelist == 0) and (destiport == 0) and (port != 0):
            for srcportjoin in srcportjoinfinal:
                for por in ports:
                    eos.write(f"{deci} {protoco} any any {por}\n")
                    print(f"{deci} {protoco} any any {por}")
                    eos.write(f"{deci} {protoco} any {por} any\n")
                    print(f"{deci} {protoco} any {por} any")
                    eos.write(f"{deci} ip any {srcportjoin} any \n")
                    print(f"{deci} ip any {srcportjoin} any")
        elif (protocol == 0) and (srcprelist == 0)  and (srcport == 0) and (destprelist != 0) and (destiport == 0) and (port != 0):
            
                for dest in destas:
                    for por in ports:
                        eos.write(f"{deci} {protoco} any any {por}\n")
                        print(f"{deci} {protoco} any any {por}")
                        eos.write(f"{deci} {protoco} any {por} any\n")
                        print(f"{deci} {protoco} any {por} any")
                        eos.write(f"{deci} ip any {dest}\n")
                        print(f"{deci} ip any {dest}")
        elif (protocol == 0) and (srcprelist == 0)  and (srcport == 0) and (destprelist == 0) and (destiport != 0) and (port != 0):
            for destasportjoin in destasportjoinfinal:
                for por in ports:
                    eos.write(f"{deci} {protoco} any any {por}\n")
                    print(f"{deci} {protoco} any any {por}")
                    eos.write(f"{deci} {protoco} any {por} any\n")
                    print(f"{deci} {protoco} any {por} any")
                    eos.write(f"{deci} ip any any {destasportjoin} \n")
                    print(f"{deci} ip any any {destasportjoin}")
        elif (protocol == 0) and (srcprelist != 0)  and (srcport != 0) and (destprelist != 0) and (destiport == 0) and (port != 0):
            for srcportjoin in srcportjoinfinal:
                for src in srcas:
                    for dest in destas:
                        for por in ports:
                            eos.write(f"{deci} {protoco} any any {por}\n")
                            print(f"{deci} {protoco} any any {por}")
                            eos.write(f"{deci} {protoco} any {por} any\n")
                            print(f"{deci} {protoco} any {por} any")
                            eos.write(f"{deci} ip {src} {srcportjoin} {dest} \n")
                            print(f"{deci} ip {src} {srcportjoin} {dest} ")
        elif (protocol == 0) and (srcprelist != 0)  and (srcport != 0) and (destprelist == 0) and (destiport == 0) and (port != 0):
            for srcportjoin in srcportjoinfinal:
                for src in srcas:
                    eos.write(f"{deci} ip {src} {srcportjoin} any {port}\n")
                    print(f"{deci} ip {src} {srcportjoin} any {port}")
        elif (protocol == 0) and (srcprelist == 0)  and (srcport != 0) and (destprelist != 0) and (destiport == 0) and (port != 0):
                for dest in destas:
                    for por in ports:
                        eos.write(f"{deci} {protoco} any any {por}\n")
                        print(f"{deci} {protoco} any any {por}")
                        eos.write(f"{deci} {protoco} any {por} any\n")
                        print(f"{deci} {protoco} any {por} any")
                        eos.write(f"{deci} ip any {srcportjoin} {dest} \n")
                        print(f"{deci} ip any {srcportjoin} {dest}")
        elif (protocol == 0) and (srcprelist != 0)  and (srcport == 0) and (destprelist != 0) and (destiport == 0) and (port != 0):
                for src in srcas:
                    for dest in destas:
                        for por in ports:
                            eos.write(f"{deci} {protoco} any any {por}\n")
                            print(f"{deci} {protoco} any any {por}")
                            eos.write(f"{deci} {protoco} any {por} any\n")
                            print(f"{deci} {protoco} any {por} any")
                            eos.write(f"{deci} ip {src} {dest}\n")
                            print(f"{deci} ip {src} {dest}")
        elif (protocol == 0) and (srcprelist == 0)  and (srcport == 0) and (destprelist == 0) and (destiport != 0) and (port != 0):
            for destasportjoin in destasportjoinfinal:
                for por in ports:
                    eos.write(f"{deci} {protoco} any any {por}\n")
                    print(f"{deci} {protoco} any any {por}")
                    eos.write(f"{deci} {protoco} any {por} any\n")
                    print(f"{deci} {protoco} any {por} any")  
                    eos.write(f"{deci} ip any any {destasportjoin} \n")
                    print(f"{deci} ip any any {destasportjoin}")
        elif (protocol == 0) and (srcprelist != 0)  and (srcport == 0) and (destprelist == 0) and (destiport != 0) and (port != 0):
            for destasportjoin in destasportjoinfinal:
                for src in srcas:
                    for por in ports:
                        eos.write(f"{deci} {protoco} any any {por}\n")
                        print(f"{deci} {protoco} any any {por}")
                        eos.write(f"{deci} {protoco} any {por} any\n")
                        print(f"{deci} {protoco} any {por} any")
                        eos.write(f"{deci} ip {src} any {destasportjoin} \n")
                        print(f"{deci} ip {src} any {destasportjoin}")             
        elif (protocol == 0) and (srcprelist == 0)  and (srcport != 0) and (destprelist == 0) and (destiport == 0) and (port != 0):
            for srcportjoin in srcportjoinfinal:
                for por in ports:
                    eos.write(f"{deci} {protoco} any any {por}\n")
                    print(f"{deci} {protoco} any any {por}")
                    eos.write(f"{deci} {protoco} any {por} any\n")
                    print(f"{deci} {protoco} any {por} any")
                    eos.write(f"{deci} ip any {srcportjoin} any \n")
                    print(f"{deci} ip any {srcportjoin} any")
        elif (protocol == 0) and (srcprelist == 0)  and (srcport != 0) and (destprelist != 0) and (destiport != 0) and (port == 0):
            for srcportjoin in srcportjoinfinal:
                for destasportjoin in destasportjoinfinal:
                    for dest in destas:
                        eos.write(f"{deci} ip any {srcportjoin} {dest} {destasportjoin} \n")
                        print(f"{deci} ip any {srcportjoin} {dest} {destasportjoin} ") 
        elif (protocol == 0) and (srcprelist != 0)  and (srcport == 0) and (destprelist != 0) and (destiport != 0) and (port != 0):
            for destasportjoin in destasportjoinfinal:           
                for src in srcas:
                    for dest in destas:
                        for por in ports:
                            eos.write(f"{deci} {protoco} any any {por}\n")
                            print(f"{deci} {protoco} any any {por}")
                            eos.write(f"{deci} {protoco} any {por} any\n")
                            print(f"{deci} {protoco} any {por} any")
                            eos.write(f"{deci} ip {src} {dest} {destasportjoin}\n")
                            print(f"{deci} ip {src} {dest} {destasportjoin}")
        elif (protocol == 0) and (srcprelist != 0)  and (srcport != 0) and (destprelist == 0) and (destiport != 0) and (port == 0):
            for srcportjoin in srcportjoinfinal:
                for destasportjoin in destasportjoinfinal: 
                    for src in srcas:
                        eos.write(f"{deci} ip {src} {srcportjoin} any {destasportjoin}\n")
                        print(f"{deci} ip {src} {srcportjoin} any {destasportjoin}")
        elif (protocol == 0) and (srcprelist == 0)  and (srcport != 0) and (destprelist == 0) and (destiport != 0) and (port == 0):
            for srcportjoin in srcportjoinfinal:
                for destasportjoin in destasportjoinfinal:
                    for src in srcas:
                        eos.write(f"{deci} ip any {srcportjoin} any {destasportjoin}\n")
                        print(f"{deci} ip any {srcportjoin} any {destasportjoin}")
        elif (protocol == 0) and (srcprelist == 0)  and (srcport == 0) and (destprelist == 0) and (destiport == 0) and (port != 0):
                for src in srcas:
                    for dest in destas:
                        for por in ports:
                            eos.write(f"{deci} {protoco} any any {por}\n")
                            print(f"{deci} {protoco} any any {por}")
                            eos.write(f"{deci} {protoco} any {por} any\n")
                            print(f"{deci} {protoco} any {por} any")
                            eos.write(f"{deci} ip any any\n")
                            print(f"{deci} ip any any")
        #with only ports keyword not present
        elif (protocol != 0) and (srcprelist != 0)  and (srcport != 0) and (destprelist != 0) and (destiport != 0) and (port == 0):
            for protoco in protocols:
                for src in srcas:
                    for dest in destas:
                        for srcportjoin in srcportjoinfinal:
                            for destasportjoin in destasportjoinfinal:
                                eos.write(f"{deci} {protoco} {src} {srcportjoin} {dest} {destasportjoin}\n")
                                print(f"{deci} {protoco} {src} {srcportjoin} {dest} {destasportjoin}")
        elif (protocol != 0) and (srcprelist != 0)  and (srcport == 0) and (destprelist == 0) and (destiport == 0) and (port == 0):
            for protoco in protocols:
                for src in srcas:
                    eos.write(f"{deci} {protoco} {src} any \n")
                    print(f"{deci} {protoco} {src} any ")
        elif (protocol != 0) and (srcprelist == 0)  and (srcport != 0) and (destprelist == 0) and (destiport == 0) and (port == 0):
            for protoco in protocols:
                for srcportjoin in srcportjoinfinal:
                    eos.write(f"{deci} {protoco} any {srcportjoin} any \n")
                    print(f"{deci} {protoco} any {srcportjoin} any")
        elif (protocol != 0) and (srcprelist == 0)  and (srcport == 0) and (destprelist != 0) and (destiport == 0) and (port == 0):
            for protoco in protocols:
                for dest in destas:
                    eos.write(f"{deci} {protoco} any {dest} \n")
                    print(f"{deci} {protoco} any {dest}")
        elif (protocol != 0) and (srcprelist == 0)  and (srcport == 0) and (destprelist == 0) and (destiport != 0) and (port == 0):
            for protoco in protocols:
                for destasportjoin in destasportjoinfinal:
                    eos.write(f"{deci} {protoco} any any {destasportjoin} \n")
                    print(f"{deci} {protoco} any any {destasportjoin}")
        elif (protocol != 0) and (srcprelist != 0)  and (srcport != 0) and (destprelist != 0) and (destiport == 0) and (port == 0):
            for protoco in protocols:
                for src in srcas:
                    for dest in destas:
                        for srcportjoin in srcportjoinfinal:
                            eos.write(f"{deci} {protoco} {src} {srcportjoin} {dest} \n")
                            print(f"{deci} {protoco} {src} {srcportjoin} {dest} ")
        elif (protocol != 0) and (srcprelist != 0)  and (srcport != 0) and (destprelist == 0) and (destiport == 0) and (port == 0):
            for protoco in protocols:
                for src in srcas:
                    for srcportjoin in srcportjoinfinal:
                        eos.write(f"{deci} {protoco} {src} {srcportjoin} any \n")
                        print(f"{deci} {protoco} {src} {srcportjoin} any ")
        elif (protocol != 0) and (srcprelist == 0)  and (srcport != 0) and (destprelist != 0) and (destiport == 0) and (port == 0):
            for protoco in protocols:
                for dest in destas:
                    for srcportjoin in srcportjoinfinal:
                        eos.write(f"{deci} {protoco} any {srcportjoin} {dest}\n")
                        print(f"{deci} {protoco} any {srcportjoin} {dest}")
        elif (protocol != 0) and (srcprelist != 0)  and (srcport == 0) and (destprelist != 0) and (destiport == 0) and (port == 0):
            for protoco in protocols:
                for src in srcas:
                    for dest in destas:
                        eos.write(f"{deci} {protoco} {src} {dest} \n")
                        print(f"{deci} {protoco} {src} {dest} ")
        elif (protocol != 0) and (srcprelist == 0)  and (srcport == 0) and (destprelist == 0) and (destiport != 0) and (port == 0):
            for protoco in protocols:
                for destasportjoin in destasportjoinfinal:
                    eos.write(f"{deci} {protoco} any any {destasportjoin} \n")
                    print(f"{deci} {protoco} any any {destasportjoin}")
        elif (protocol != 0) and (srcprelist != 0)  and (srcport == 0) and (destprelist == 0) and (destiport != 0) and (port == 0):
            for protoco in protocols:
                for src in srcas:
                    for destasportjoin in destasportjoinfinal:
                        eos.write(f"{deci} {protoco} {src} any {destasportjoin} \n")
                        print(f"{deci} {protoco} {src} any {destasportjoin}")             
        elif (protocol != 0) and (srcprelist == 0)  and (srcport != 0) and (destprelist == 0) and (destiport == 0) and (port == 0):
            for protoco in protocols:
                for srcportjoin in srcportjoinfinal:
                    eos.write(f"{deci} {protoco} any {srcportjoin} any \n")
                    print(f"{deci} {protoco} any {srcportjoin} any ")
        elif (protocol != 0) and (srcprelist == 0)  and (srcport != 0) and (destprelist != 0) and (destiport != 0) and (port == 0):
            for protoco in protocols:
                for dest in destas:
                    for srcportjoin in srcportjoinfinal:
                        for destasportjoin in destasportjoinfinal:
                            eos.write(f"{deci} {protoco} any {srcportjoin} {dest} {destasportjoin} \n")
                            print(f"{deci} {protoco} any {srcportjoin} {dest} {destasportjoin} ") 
        elif (protocol != 0) and (srcprelist != 0)  and (srcport == 0) and (destprelist != 0) and (destiport != 0) and (port == 0):
            for protoco in protocols:
                for src in srcas:
                    for dest in destas:
                        for srcportjoin in srcportjoinfinal:
                            for destasportjoin in destasportjoinfinal:
                                eos.write(f"{deci} {protoco} {src} {dest} {destasportjoin}\n")
                                print(f"{deci} {protoco} {src} {dest} {destasportjoin}")
        elif (protocol != 0) and (srcprelist != 0)  and (srcport != 0) and (destprelist == 0) and (destiport != 0) and (port == 0):
            for protoco in protocols:
                for src in srcas:
                    for srcportjoin in srcportjoinfinal:
                        for destasportjoin in destasportjoinfinal:
                            eos.write(f"{deci} {protoco} {src} {srcportjoin} any {destasportjoin}\n")
                            print(f"{deci} {protoco} {src} {srcportjoin} any {destasportjoin}")
        elif (protocol != 0) and (srcprelist == 0)  and (srcport != 0) and (destprelist == 0) and (destiport != 0) and (port == 0):
            for protoco in protocols:
                for srcportjoin in srcportjoinfinal:
                    for destasportjoin in destasportjoinfinal:
                        eos.write(f"{deci} {protoco} any {srcportjoin} any {destasportjoin}\n")
                        print(f"{deci} {protoco} any {srcportjoin} any {destasportjoin}")
        elif (protocol != 0) and (srcprelist != 0)  and (srcport == 0) and (destprelist == 0) and (destiport == 0) and (port != 0):
            for protoco in protocols:
                for src in srcas:
                    eos.write(f"{deci} {protoco} {src} {port} any\n")
                    print(f"{deci} {protoco} {src} {port} any")
        elif (protocol != 0) and (srcprelist == 0)  and (srcport == 0) and (destprelist != 0) and (destiport != 0) and (port == 0):
            for protoco in protocols:
                    for dest in destas:
                        for destasportjoin in destasportjoinfinal:
                            eos.write(f"{deci} {protoco} any {dest} {destasportjoin}\n")
                            print(f"{deci} {protoco} any {dest} {destasportjoin}")
        elif (protocol != 0) and (srcprelist != 0)  and (srcport == 0) and (destprelist != 0) and (destiport == 0) and (port != 0):
            for protoco in protocols:
                for src in srcas:
                    for dest in destas:
                        eos.write(f"{deci} {protoco} {src} {dest} {port}\n")
                        print(f"{deci} {protoco} {src} {dest} {port}")
        elif (protocol != 0) and (srcprelist == 0)  and (srcport == 0) and (destprelist == 0) and (destiport == 0) and (port == 0):
            for protoco in protocols:
                for src in srcas:
                    for dest in destas:
                        eos.write(f"{deci} {protoco} any any\n")
                        print(f"{deci} {protoco} any any")
        #without protocol with source and destination prefixlist
        elif (protocol == 0) and (srcprelist != 0)  and (srcport != 0) and (destprelist != 0) and (destiport != 0) and (port == 0):
            for src in srcas:
                for dest in destas:
                    for srcportjoin in srcportjoinfinal:
                        for destasportjoin in destasportjoinfinal:
                            eos.write(f"{deci} ip {src} {srcportjoin} {dest} {destasportjoin}\n")
                            print(f"{deci} ip {src} {srcportjoin} {dest} {destasportjoin}")
        elif (protocol == 0) and (srcprelist != 0)  and (srcport == 0) and (destprelist == 0) and (destiport == 0) and (port == 0):
            for src in srcas:
                eos.write(f"{deci} ip {src} any \n")
                print(f"{deci} ip {src} any ")
        elif (protocol == 0) and (srcprelist == 0)  and (srcport != 0) and (destprelist == 0) and (destiport == 0) and (port == 0):
            for srcportjoin in srcportjoinfinal:
                eos.write(f"{deci} ip any {srcportjoin} any \n")
                print(f"{deci} ip any {srcportjoin} any")
        elif (protocol == 0) and (srcprelist == 0)  and (srcport == 0) and (destprelist != 0) and (destiport == 0) and (port == 0):         
                for dest in destas:
                    eos.write(f"{deci} ip any {dest} \n")
                    print(f"{deci} ip any {dest}")
        elif (protocol == 0) and (srcprelist == 0)  and (srcport == 0) and (destprelist == 0) and (destiport != 0) and (port == 0):
            for destasportjoin in destasportjoinfinal:
                eos.write(f"{deci} ip any any {destasportjoin} \n")
                print(f"{deci} ip any any {destasportjoin}")
        elif (protocol == 0) and (srcprelist != 0)  and (srcport != 0) and (destprelist != 0) and (destiport == 0) and (port == 0):
            for srcportjoin in srcportjoinfinal:
                for src in srcas:
                    for dest in destas:
                        eos.write(f"{deci} ip {src} {srcportjoin} {dest} \n")
                        print(f"{deci} ip {src} {srcportjoin} {dest} ")
        elif (protocol == 0) and (srcprelist != 0)  and (srcport != 0) and (destprelist == 0) and (destiport == 0) and (port == 0):
            for srcportjoin in srcportjoinfinal:
                for src in srcas:
                    eos.write(f"{deci} ip {src} {srcportjoin} any \n")
                    print(f"{deci} ip {src} {srcportjoin} any ")
        elif (protocol == 0) and (srcprelist == 0)  and (srcport != 0) and (destprelist != 0) and (destiport == 0) and (port == 0):
            
                for dest in destas:
                    eos.write(f"{deci} ip any {srcportjoin} {dest}\n")
                    print(f"{deci} ip any {srcportjoin} {dest}")
        elif (protocol == 0) and (srcprelist != 0)  and (srcport == 0) and (destprelist != 0) and (destiport == 0) and (port == 0):
                for src in srcas:
                    for dest in destas:
                        eos.write(f"{deci} ip {src} {dest} \n")
                        print(f"{deci} ip {src} {dest} ")
        elif (protocol == 0) and (srcprelist == 0)  and (srcport == 0) and (destprelist == 0) and (destiport != 0) and (port == 0):
            for destasportjoin in destasportjoinfinal:  
                eos.write(f"{deci} ip any any {destasportjoin} \n")
                print(f"{deci} ip any any {destasportjoin}")
        elif (protocol == 0) and (srcprelist != 0)  and (srcport == 0) and (destprelist == 0) and (destiport != 0) and (port == 0):
            for destasportjoin in destasportjoinfinal:
                for src in srcas:
                    eos.write(f"{deci} ip {src} any {destasportjoin} \n")
                    print(f"{deci} ip {src} any {destasportjoin}")             
        elif (protocol == 0) and (srcprelist == 0)  and (srcport != 0) and (destprelist == 0) and (destiport == 0) and (port == 0):
            for srcportjoin in srcportjoinfinal:
                eos.write(f"{deci} ip any {srcportjoin} any \n")
                print(f"{deci} ip any {srcportjoin} any ")
        elif (protocol == 0) and (srcprelist == 0)  and (srcport != 0) and (destprelist != 0) and (destiport != 0) and (port == 0):
            for srcportjoin in srcportjoinfinal:
                for destasportjoin in destasportjoinfinal:
                    for dest in destas:
                        eos.write(f"{deci} ip any {srcportjoin} {dest} {destasportjoin} \n")
                        print(f"{deci} ip any {srcportjoin} {dest} {destasportjoin} ") 
        elif (protocol == 0) and (srcprelist != 0)  and (srcport == 0) and (destprelist != 0) and (destiport != 0) and (port == 0):
            for destasportjoin in destasportjoinfinal:           
                for src in srcas:
                    for dest in destas:
                        eos.write(f"{deci} ip {src} {dest} {destasportjoin}\n")
                        print(f"{deci} ip {src} {dest} {destasportjoin}")
        elif (protocol == 0) and (srcprelist != 0)  and (srcport != 0) and (destprelist == 0) and (destiport != 0) and (port == 0):
            for srcportjoin in srcportjoinfinal:
                for destasportjoin in destasportjoinfinal: 
                    for src in srcas:
                        eos.write(f"{deci} ip {src} {srcportjoin} any {destasportjoin}\n")
                        print(f"{deci} ip {src} {srcportjoin} any {destasportjoin}")
        elif (protocol == 0) and (srcprelist == 0)  and (srcport != 0) and (destprelist == 0) and (destiport != 0) and (port == 0):
            for srcportjoin in srcportjoinfinal:
                for destasportjoin in destasportjoinfinal:
                    for src in srcas:
                        eos.write(f"{deci} ip any {srcportjoin} any {destasportjoin}\n")
                        print(f"{deci} ip any {srcportjoin} any {destasportjoin}")
        elif (protocol == 0) and (srcprelist == 0)  and (srcport == 0) and (destprelist == 0) and (destiport == 0) and (port == 0):
                for src in srcas:
                    for dest in destas:
                        eos.write(f"{deci} ip any any\n")
                        print(f"{deci} ip any any")

        #with protocol and source address and destination address
        elif (protocol != 0) and (srcadd != 0)  and (port != 0) and (destadd != 0):
            for protoco in protocols:
                for srcad in srcadds:
                    for destad in destadds:
                        eos.write(f"{deci} {protoco} {srcad}  {port} {destad}  {port}\n")
                        print(f"{deci} {protoco} {srcad}  {port} {destad}  {port}")
        elif (protocol != 0) and (srcadd != 0)  and (port == 0) and (destadd == 0):
            for protoco in protocols:
                for srcad in srcadds:
                    eos.write(f"{deci} {protoco} {srcad} any \n")
                    print(f"{deci} {protoco} {srcad} any ")
        elif (protocol != 0) and (srcadd == 0)  and (port != 0) and (destadd == 0):
            for protoco in protocols:
                eos.write(f"{deci} {protoco} any  {port} any \n")
                print(f"{deci} {protoco} any  {port} any")
        elif (protocol != 0) and (srcadd == 0)  and (port == 0) and (destadd != 0):
            for protoco in protocols:
                for destad in destadds:
                    eos.write(f"{deci} {protoco} any {destad} \n")
                    print(f"{deci} {protoco} any {destad}")
        elif (protocol != 0) and (srcadd == 0)  and (port != 0) and (destadd == 0):
            for protoco in protocols:
                eos.write(f"{deci} {protoco} any any {port}\n")
                print(f"{deci} {protoco} any any {port}")
        elif (protocol != 0) and (srcadd != 0)  and (port != 0) and (destadd != 0):
            for protoco in protocols:
                for srcad in srcadds:
                    for destad in destadds:
                        eos.write(f"{deci} {protoco} {srcad}  {port} {destad} \n")
                        print(f"{deci} {protoco} {srcad}  {port} {destad} ")
        elif (protocol != 0) and (srcadd != 0)  and (port != 0) and (destadd == 0):
            for protoco in protocols:
                for srcad in srcadds:
                    for por in ports:
                        eos.write(f"{deci} {protoco} any any {por}\n")
                        print(f"{deci} {protoco} any any {por}")
                        eos.write(f"{deci} {protoco} any {por} any\n")
                        print(f"{deci} {protoco} any {por} any")
                        eos.write(f"{deci} {protoco} {srcad} any \n")
                        print(f"{deci} {protoco} {srcad} any ")
        elif (protocol != 0) and (srcadd == 0)  and (port != 0) and (destadd != 0):
            for protoco in protocols:
                for destad in destadds:
                    for por in ports:
                        eos.write(f"{deci} {protoco} any any {por}\n")
                        print(f"{deci} {protoco} any any {por}")
                        eos.write(f"{deci} {protoco} any {por} any\n")
                        print(f"{deci} {protoco} any {por} any")
                        eos.write(f"{deci} {protoco} any {destad}\n")
                        print(f"{deci} {protoco} any {destad}")
        elif (protocol != 0) and (srcadd != 0)  and (port == 0) and (destadd != 0):
            for protoco in protocols:
                for srcad in srcadds:
                    for destad in destadds:
                        eos.write(f"{deci} {protoco} {srcad} {destad} \n")
                        print(f"{deci} {protoco} {srcad} {destad} ")
        elif (protocol != 0) and (srcadd == 0) and (destadd == 0) and (port != 0):
            for protoco in protocols:
                for por in ports:
                    eos.write(f"{deci} {protoco} any any {por}\n")
                    print(f"{deci} {protoco} any any {por}")
                    eos.write(f"{deci} {protoco} any {por} any\n")
                    print(f"{deci} {protoco} any {por} any")
                    eos.write(f"{deci} {protoco} any any \n")
                    print(f"{deci} {protoco} any any")
        elif (protocol != 0) and (srcadd != 0) and (destadd == 0) and (port != 0):
            for protoco in protocols:
                for srcad in srcadds:
                    for por in ports:
                        eos.write(f"{deci} {protoco} any any {por}\n")
                        print(f"{deci} {protoco} any any {por}")
                        eos.write(f"{deci} {protoco} any {por} any\n")
                        print(f"{deci} {protoco} any {por} any")
                        eos.write(f"{deci} {protoco} {srcad} any \n")
                        print(f"{deci} {protoco} {srcad} any ")             
        elif (protocol != 0) and (srcadd == 0)  and (port != 0) and (destadd == 0):
            for protoco in protocols:
                for por in ports:
                    eos.write(f"{deci} {protoco} any any {por}\n")
                    print(f"{deci} {protoco} any any {por}")
                    eos.write(f"{deci} {protoco} any {por} any\n")
                    print(f"{deci} {protoco} any {por} any")
        elif (protocol != 0) and (srcadd == 0)  and (port != 0) and (destadd != 0):
            for protoco in protocols:
                for destad in destadds:
                    for por in ports:
                        eos.write(f"{deci} {protoco} any any {por}\n")
                        print(f"{deci} {protoco} any any {por}")
                        eos.write(f"{deci} {protoco} any {por} any\n")
                        print(f"{deci} {protoco} any {por} any")
                        eos.write(f"{deci} {protoco} any {destad}\n")
                        print(f"{deci} {protoco} any {destad}") 
        elif (protocol != 0) and (srcadd != 0) and (destadd != 0) and (port != 0):
            for protoco in protocols:
                for srcad in srcadds:
                    for destad in destadds:
                        for por in ports:
                            eos.write(f"{deci} {protoco} any any {por}\n")
                            print(f"{deci} {protoco} any any {por}")
                            eos.write(f"{deci} {protoco} any {por} any\n")
                            print(f"{deci} {protoco} any {por} any")
                            eos.write(f"{deci} {protoco} {srcad} {destad} \n")
                            print(f"{deci} {protoco} {srcad} {destad}")
        elif (protocol != 0) and (srcadd != 0)  and (port != 0) and (destadd == 0):
            for protoco in protocols:
                for srcad in srcadds:
                    for por in ports:
                        eos.write(f"{deci} {protoco} any any {por}\n")
                        print(f"{deci} {protoco} any any {por}")
                        eos.write(f"{deci} {protoco} any {por} any\n")
                        print(f"{deci} {protoco} any {por} any")
                        eos.write(f"{deci} {protoco} {srcad} any\n")
                        print(f"{deci} {protoco} {srcad} any")
        elif (protocol != 0) and (srcadd == 0)  and (port != 0) and (destadd == 0):
            for protoco in protocols:
                for srcad in srcadds:
                    for por in ports:
                        eos.write(f"{deci} {protoco} any any {por}\n")
                        print(f"{deci} {protoco} any any {por}")
                        eos.write(f"{deci} {protoco} any {por} any\n")
                        print(f"{deci} {protoco} any {por} any")
        elif (protocol != 0) and (srcadd == 0)  and (port == 0) and (destadd == 0):
            for protoco in protocols:
                for srcad in srcadds:
                    for destad in destadds:
                        eos.write(f"{deci} {protoco} any any\n")
                        print(f"{deci} {protoco} any any")
        #without protocol with source and destination prefixlist
        elif (protocol == 0) and (srcadd != 0)  and (port != 0) and (destadd != 0):   
                for srcad in srcadds:
                    for destad in destadds:
                        for por in ports:
                            eos.write(f"{deci} ip any any {por}\n")
                            print(f"{deci} ip any any {por}")
                            eos.write(f"{deci} ip any {por} any\n")
                            print(f"{deci} ip any {por} any")
                            eos.write(f"{deci} ip {srcad} {destad} \n")
                            print(f"{deci} ip {srcad} {destad}")
        elif (protocol == 0) and (srcadd != 0)  and (port == 0) and (destadd == 0):    
                for srcad in srcadds:
                    eos.write(f"{deci} ip {srcad} any \n")
                    print(f"{deci} ip {srcad} any ")
        elif (protocol == 0) and (srcadd == 0)  and (port != 0) and (destadd == 0):    
            for por in ports:
                eos.write(f"{deci} ip any any {por}\n")
                print(f"{deci} ip any any {por}")
                eos.write(f"{deci} ip any {por} any\n")
                print(f"{deci} ip any {por} any")
        elif (protocol == 0) and (srcadd == 0) and (destadd != 0) and (port == 0):
                for destad in destadds:
                    eos.write(f"{deci} ip any {destad} \n")
                    print(f"{deci} ip any {destad}")
        elif (protocol == 0) and (srcadd == 0) and (destadd == 0) and (port != 0):
            for por in ports:
                eos.write(f"{deci} ip any any {por}\n")
                print(f"{deci} ip any any {por}")
                eos.write(f"{deci} ip any {por} any\n")
                print(f"{deci} ip any {por} any")
        elif (protocol == 0) and (srcadd != 0)  and (port != 0) and (destadd != 0):
                for srcad in srcadds:
                    for destad in destadds:
                        for por in ports:
                            eos.write(f"{deci} ip any any {por}\n")
                            print(f"{deci} ip any any {por}")
                            eos.write(f"{deci} ip any {por} any\n")
                            print(f"{deci} ip any {por} any")
                            eos.write(f"{deci} ip {srcad} {destad} \n")
                            print(f"{deci} ip {srcad} {destad} ")
        elif (protocol == 0) and (srcadd != 0)  and (port != 0) and (destadd == 0):
                for srcad in srcadds:
                    for por in ports:
                        eos.write(f"{deci} ip any any {por}\n")
                        print(f"{deci} ip any any {por}")
                        eos.write(f"{deci} ip any {por} any\n")
                        print(f"{deci} ip any {por} any")
                        eos.write(f"{deci} ip {srcad} any \n")
                        print(f"{deci} ip {srcad} any ")
        elif (protocol == 0) and (srcadd == 0)  and (port != 0) and (destadd != 0):
                for destad in destadds:
                    for por in ports:
                        eos.write(f"{deci} ip any any {por}\n")
                        print(f"{deci} ip any any {por}")
                        eos.write(f"{deci} ip any {por} any\n")
                        print(f"{deci} ip any {por} any")
                        eos.write(f"{deci} ip any {destad}\n")
                        print(f"{deci} ip any {destad}")
        elif (protocol == 0) and (srcadd != 0)  and (port == 0) and (destadd != 0):
                for srcad in srcadds:
                    for destad in destadds:
                        eos.write(f"{deci} ip {srcad} {destad} \n")
                        print(f"{deci} ip {srcad} {destad} ")
        elif (protocol == 0) and (srcadd == 0)  and (port != 0) and (destadd == 0):  
            for por in ports:
                eos.write(f"{deci} ip any any {por}\n")
                print(f"{deci} ip any any {por}")
                eos.write(f"{deci} ip any {por} any\n")
                print(f"{deci} ip any {por} any")    
        elif (protocol == 0) and (srcadd != 0)  and (port != 0) and (destadd == 0):
            for srcad in srcadds:
                for por in ports:
                    eos.write(f"{deci} ip any any {por}\n")
                    print(f"{deci} ip any any {por}")
                    eos.write(f"{deci} ip any {por} any\n")
                    print(f"{deci} ip any {por} any") 
                    eos.write(f"{deci} ip {srcad} any \n")
                    print(f"{deci} ip {srcad} any")             
        elif (protocol == 0) and (srcadd == 0)  and (port != 0) and (destadd == 0):
            for por in ports:
                eos.write(f"{deci} ip any any {por}\n")
                print(f"{deci} ip any any {por}")
                eos.write(f"{deci} ip any {por} any\n")
                print(f"{deci} ip any {por} any")
        elif (protocol == 0) and (srcadd == 0)  and (port != 0) and (destadd != 0):  
                for destad in destadds:
                    for por in ports:
                        eos.write(f"{deci} ip any any {por}\n")
                        print(f"{deci} ip any any {por}")
                        eos.write(f"{deci} ip any {por} any\n")
                        print(f"{deci} ip any {por} any")
                        eos.write(f"{deci} ip any {destad}\n")
                        print(f"{deci} ip any {destad}") 
        elif (protocol == 0) and (srcadd != 0)  and (port != 0) and (destadd != 0):           
                for srcad in srcadds:
                    for destad in destadds:
                        for por in ports:
                            eos.write(f"{deci} ip any any {por}\n")
                            print(f"{deci} ip any any {por}")
                            eos.write(f"{deci} ip any {por} any\n")
                            print(f"{deci} ip any {por} any")
                            eos.write(f"{deci} ip {srcad} {destad}\n")
                            print(f"{deci} ip {srcad} {destad}")
        elif (protocol == 0) and (srcadd != 0)  and (port != 0) and (destadd == 0): 
                for srcad in srcadds:
                    for por in ports:
                        eos.write(f"{deci} ip any any {por}\n")
                        print(f"{deci} ip any any {por}")
                        eos.write(f"{deci} ip any {por} any\n")
                        print(f"{deci} ip any {por} any")
                        eos.write(f"{deci} ip {srcad} any \n")
                        print(f"{deci} ip {srcad} any")
        elif (protocol == 0) and (srcadd == 0)  and (port != 0) and (destadd == 0):
                for srcad in srcadds:
                    for por in ports:
                        eos.write(f"{deci} ip any any {por}\n")
                        print(f"{deci} ip any any {por}")
                        eos.write(f"{deci} ip any {por} any\n")
                        print(f"{deci} ip any {por} any")
                        eos.write(f"{deci} ip any any\n")
                        print(f"{deci} ip any any")
        elif (protocol == 0) and (srcadd == 0)  and (port == 0) and (destadd == 0):
                for srcad in srcadds:
                    for destad in destadds:
                        eos.write(f"{deci} ip any any\n")
                        print(f"{deci} ip any any")

def aclname():
    with open(outputfilename,"a") as eos:
        eos.write(f"\nip access-list {filtername}\n")
        eos.write(f"!!{comment}\n")
        print(f"ip access-list {filtername}")
        print(f"!!{comment}")

def aclconvert():
    print("\n ACL Conversion started....")
    aclname()
    aclcondition()
    aclcount()
    print("\n Completed configuration generation....")

def aegisaction():
    try:
        with open(outputfilename,"a") as eos:
            eos.write("actions\n")
            print("actions")
            if dscp != None:
                eos.write(f"dscp {dscpno}\n")
                print(f"dscp {dscpno}")
            if frdclass != 0:
                eos.write(f"set traffic class {frdclassno}\n")
                print(f"set traffic class {frdclassno}")
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
    with open(outputfilename,"a") as eos:
        if srcport != 0 and destiport != 0:
            if protocol != 0:
                for protoco in protocols:
                    for destipor in destiports:
                        for srcpor in srcports:
                            eos.write(f"protocol {protoco} source port {srcpor} destination port {destipor}\n")
                            print(f"protocol {protoco} source port {srcpor} destination port {destipor}")
            else:
                for destipor in destiports:
                        for srcpor in srcports:
                            eos.write(f"protocol tcp source port {srcpor} destination port {destipor}\n")
                            eos.write(f"protocol udp source port {srcpor} destination port {destipor}\n")
                            print(f"protocol tcp source port {srcpor} destination port {destipor}")
                            print(f"protocol udp source port {srcpor} destination port {destipor}")       
        if destiport != 0 and srcport == 0:
            if protocol != 0:
                for protoco in protocols:
                    for destipor in destiports:
                        eos.write(f"protocol {protoco} destination port {destipor}\n")
                        print(f"protocol {protoco} destination port {destipor}")
            else:
                for destipor in destiports:
                    eos.write(f"protocol tcp destination port {destipor}\n")
                    eos.write(f"protocol udp destination port {destipor}\n")
                    print(f"protocol tcp destination port {destipor}")
                    print(f"protocol udp destination port {destipor}")     
        if destiport == 0 and srcport != 0:
            if protocol != 0:
                for protoco in protocols:
                    for destipor in destiports:
                        eos.write(f"protocol {protoco} source port {destipor}\n")
                        print(f"protocol {protoco} source port {destipor}")
            else:
                for srcpor in srcports:
                    eos.write(f"protocol tcp source port {srcpor}\n")
                    eos.write(f"protocol udp source port {srcpor}\n")
                    print(f"protocol tcp source port {srcpor}")
                    print(f"protocol udp source port {srcpor}")
        if protocol != 0 and port != 0:    
            for protoco in protocols:
                for por in ports:
                    eos.write(f"protocol {protoco} source port {por}\n")
                    print(f"protocol {protoco} source port {por}")   
                    eos.write(f"protocol {protoco} destination port {por}\n")
                    print(f"protocol {protoco} destination port {por}")                
           

def aegisprefix():
    with open(outputfilename,"a") as eos:
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
    with open(outputfilename,"a") as eos:
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
        with open(outputfilename,"a") as eos:
            eos.write("traffic-policies\n")
            print("traffic-policies")
            eos.write(f"field-set ipv4 prefix {filtername}-source\n")
            print(f"field-set ipv4 prefix {filtername}-source")
            for srcad in srcadds:
                eos.write(f"{srcad}\n")
                print(f"{srcad}")
    if destadd != 0:
        with open(outputfilename,"a") as eos:
            eos.write("traffic-policies\n")
            print("traffic-policies")
            eos.write(f"field-set ipv4 prefix {filtername}-destination\n")
            print(f"field-set ipv4 prefix {filtername}-destination")              
            for destad in destadds:
                eos.write(f"{destad}\n")
                print(f"{destad}")
    if destprelist != 0:
        with open(outputfilename,"a") as eos:
            eos.write("traffic-policies\n")
            print("traffic-policies")
            eos.write(f"field-set ipv4 prefix {destprelist}\n")
            print(f"field-set ipv4 prefix {destprelist}")
            global dest              
            for dest in destas:
                eos.write(f"{dest}\n")
                print(f"{dest}")
    if srcprelist != 0:
        with open(outputfilename,"a") as eos:
            eos.write("traffic-policies\n")
            print("traffic-policies")
            eos.write(f"field-set ipv4 prefix {srcprelist}\n")
            print(f"field-set ipv4 prefix {srcprelist}")
            global src              
            for src in srcas:
                eos.write(f"{src}\n")
                print(f"{src}") 

#second level of parsing by using the inputs gained - dscptable, range or single(eq) ports check, 
def secondparse():
    global rowcount; rowcount  = 0
    global srcportjoinfinal; srcportjoinfinal = []
    global destasportjoinfinal; destasportjoinfinal = []
    global destas; destas = []
    global srcas; srcas = []
    global dscpno; 
    global frdclassno;
    if destiport != 0:
        for checkdestport in destiports:
            if ('-' in  checkdestport):
                destiportsjoin = f"range-{checkdestport}"
                destasportsplit = destiportsjoin.split('-')
                destasportjoins = ' '.join(destasportsplit)
                destasportjoinfinal.append(destasportjoins)
            elif ('-' not in checkdestport):
                destasportjoins = f"eq {checkdestport}"
                destasportjoinfinal.append(destasportjoins)
    if srcport != 0:
        for checksrcport in srcports:
            if ('-' in  checksrcport):
                srcportsjoin = f"range-{checksrcport}"
                srcportsplit = srcportsjoin.split('-')
                srcportjoins = ' '.join(srcportsplit)
                srcportjoinfinal.append(srcportjoins)
            elif ('-' not in checksrcport):
                srcportjoins = f"eq {checksrcport}"
                srcportjoinfinal.append(srcportjoins)
    #parsing ip address from prefix list if any - prefixlistparse
    if destprelist != 0:
        with open(inputfilename,"r") as file2:
            n2 = file2.readlines();
            for destprelis in destprelists:
                for r2 in n2:
                    try:
                        if destprelis in r2:
                            a = re.search(rf'\b( prefix-list {destprelis} )\b',r2)
                            fi = a.end(); 
                            l = len(r2)
                            o = r2[fi:l]
                            g = o.split(' ')
                            desta = g[0].strip()
                            destas.append(desta)
                    except:
                        end = 1
    if srcprelist != 0:
        with open(inputfilename,"r") as file2:
            n2 = file2.readlines();
            for srcprelis in srcprelists:
                for r2 in n2:
                    #print(r2)
                    try:
                        if srcprelis in r2:
                            a = re.search(rf'\b( prefix-list {srcprelis} )\b',r2)
                            fi = a.end(); 
                            l = len(r2)
                            o = r2[fi:l]
                            g = o.split(' ')
                            srca = g[0].strip()
                            srcas.append(srca)
                    except:
                        end = 1
    #dscptable
    if dscp != None:
        if dscp == 'af11':
            dscpno = 10
        if dscp == 'af12':
            dscpno = 12
        if dscp == 'af13':
            dscpno = 14
        if dscp == 'af21':
            dscpno = 18
        if dscp == 'af22':
            dscpno = 20
        if dscp == 'af23':
            dscpno = 22
        if dscp == 'af31':
            dscpno = 26
        if dscp == 'af32':
            dscpno = 28
        if dscp == 'af33':
            dscpno = 30
        if dscp == 'af41':
            dscpno = 34
        if dscp == 'af42':
            dscpno = 36
        if dscp == 'af43':
            dscpno = 38
        if dscp == 'cs1':
            dscpno = 8
        if dscp == 'cs2':
            dscpno = 16
        if dscp == 'cs3':
            dscpno = 24
        if dscp == 'cs4':
            dscpno = 32
        if dscp == 'cs5':
            dscpno = 40
        if dscp == 'cs6':
            dscpno = 48
        if dscp == 'cs7':
            dscpno = 56
        if (dscp == 'default') or (dscp == 'be') or (dscp == '0'):
            dscpno = 0   
        if dscp == 'ef':
            dscpno = 46

    #forwarding-class check
    if frdclass != 0:
        if frdclass in qosnames:
            frdclassnoindex = qosnames.index(frdclass)
            frdclassno = qosvalues[frdclassnoindex]

#parse junos command for filtername
def firstparse():
    try:
        global port; port = 0
        global srcadd; srcadd = 0
        global protocol; protocol = 0
        global destadd; destadd = 0
        global srcadds; srcadds = []
        global destadds; destadds = []
        global inputs; inputs = []
        global value; value = 0
        global protocols; protocols = []
        global count; count = 0
        global srcprelist; srcprelist = 0
        global destprelist; destprelist = 0
        global destiport; destiport = 0
        global srcport; srcport = 0
        global deci; deci = 0
        global completeinput; completeinput = []
        global destiports; destiports = []
        global srcports; srcports = []
        global ports; ports = []
        global srcprelists; srcprelists =[]
        global destprelists; destprelists = []
        global rouins; rouins = 0
        global frdclass; frdclass = 0
        global dscp; dscp = None
        with open(inputfilename,"r") as file1:
            n1 = file1.readlines();
            global r1
            for r1 in n1:
                filternamecheck = f"{filtername} "
                commentcheck = f"{comment} "
                if (filternamecheck in r1) and (commentcheck in r1):
                        completeinput.append(r1)
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
                            if " protocol " in r1:
                                a = re.search(rf'\b( protocol )\b', r1)
                                fi = a.end(); 
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
                                if args.output == "aegis":
                                    ports.append(port)
                                elif args.output == "acl":
                                    ports.append(f"eq {port}")
                                print(f"Found port: {ports}")
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
                            #in junos for permit they will have accpet or nothing(0) 
                            if deci == 0:
                                deci = "permit"
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
                                srcprelists.append(srcprelist)
                                print(f"Found source-prefix-list: {srcprelists}")
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
                                destprelists.append(destprelist)
                                print(f"Found destination-prefix-list: {destprelists}")
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
                                destiports.append(destiport)
                                print(f"Found destination-port: {destiports}")
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
                                srcports.append(srcport)
                                print(f"Found source-port: {srcports}")
                        except:
                                end=1;
                        try:
                            if " forwarding-class " in r1:
                                a = re.search(rf'\b( forwarding-class )\b', r1)
                                fi = a.end(); 
                                l = len(r1)
                                o = r1[fi:l]
                                g = o.split(' ')
                                frdclass = g[0].strip()
                                print(f"Found forwarding-class: {frdclass}")
                        except:
                                end=1;
                        try:
                            if " routing-instance " in r1:
                                a = re.search(rf'\b( routing-instance )\b', r1)
                                fi = a.end(); 
                                l = len(r1)
                                o = r1[fi:l]
                                g = o.split(' ')
                                rouins = g[0].strip()
                                print(f"Found routing-instance: {rouins}")
                        except:
                                end=1;
                        try:
                            if " dscp " in r1:
                                a = re.search(rf'\b( dscp )\b', r1)
                                fi = a.end(); 
                                l = len(r1)
                                o = r1[fi:l]
                                g = o.split(' ')
                                dscp = g[0].strip()
                                print(f"Found dscp: {dscp}")
                        except:
                                end=1;
    except Exception as ex:
        trace = []
        tb = ex.__traceback__
        while tb is not None:
            trace.append({
                "inputfilename": tb.tb_frame.f_code.co_inputfilename,
                "name": tb.tb_frame.f_code.co_name,
                "lineno": tb.tb_lineno
            })
            tb = tb.tb_next
        print(str({
            'type': type(ex).__name__,
            'message': str(ex),
            'trace': trace
        }))

def aegisconvert():
    print("\n Aegis Conversion started...")
    print(" Generating aegis Conf....")   
    aegisfieldset()  
    aegistrafficpolicy()
    aegisprefix()
    aegisprotocol()
    aegisaction()
    print("\n Completed configuration generation....")

def qosparse():
    global qosvalues; qosvalues =[]
    global qosnames; qosnames = []
    global qosmatchdict; qosmatchdict = {}
    global qosrows; qosrows = []
    print("\n Converting and Generating QOS arista configuration....")
    with open(inputfilename,'r') as qosin:
        qosinc = qosin.readlines();
        for qosrow in qosinc:
            if "set class-of-service forwarding-classes queue" in qosrow:
                a = re.search(rf'\b(forwarding-classes queue )\b', qosrow)
                qosrows.append(qosrow)
                fi = a.end(); 
                l = len(qosrow)
                o = qosrow[fi:l]
                g = o.split(' ')
                qosvalue = g[0].strip()
                qosname = g[1].strip()
                qosvalues.append(qosvalue)
                qosnames.append(qosname)

#Convert juniper QOS conf to arista QOS conf. Do this before aegiscli conversion because we may use this in aegiscli
def qosconf():
    #create a dictionary using values we got
    n = 0
    while n < len(qosvalues):
        qosmatchdict.update({qosvalues[n]:qosnames[n]})
        n = n+1;
    print(f"\nFound QOS match: {qosmatchdict}")
    print(f"\n Complete JUNOS QOS match input:")
    for qosro in qosrows:
        print(qosro.strip())
    print("\n Generating Arista QOS match Configuration.....")
    with open(outputfilename,"a") as eosqos:
        eosqos.write(" ")
        print(" ")
    n = 0
    while n < len(qosvalues):
        print(f"\n JUNOS input for QOS '{qosvalues[n]}:{qosnames[n]}'")
        with open('junosconf.csv','r') as qosin:
            qosinc = qosin.readlines();
            for qosrow in qosinc:
                if qosnames[n] in qosrow:
                    if ' then ' not in qosrow:
                        if ' from ' not in qosrow:
                            print(qosrow.strip())
        print(f"\n Generating Arista Config for QOS '{qosvalues[n]}:{qosnames[n]}'")
        with open(outputfilename,"a") as eosqos:
            eosqos.write(" ")
            print(" ")
        n = n+1

def convert():
    #if output is qos just do only qos conversion
    if args.output == "qos":
        qosparse()
        qosconf()
    #if output is aegis or acl get filtername and start the firewall filter conversion
    elif (args.output == "aegis") or (args.output =="acl"):    
        for filters in filterfinal:
            sep = filters.split(';')
            global filtername
            global comment
            filtername = sep[0]
            comment = sep[1]
            print(f"\nFound filtername: {filtername}")
            print(f"Found Term: {comment}")
            qosparse()
            firstparse()
            secondparse()
            print("\n Complete Input:")
            for inputs in completeinput:
                print(inputs.strip())
            if args.output == "aegis":
                aegisconvert()
            #ACL is not fully completed need to work on function arrangements
            elif args.output == "acl":
                aclconvert()

#parse junos command for filtername
def getfilternames():
    try:
        filternames = []
        with open(inputfilename,"r") as file:
            csvreader = csv.reader(file)
            for row in csvreader:
                if (" filter" in row[0]) and (" term" in row[0]):
                    r = row[0]
                    a = re.search(r'\b( filter)\b', r)
                    fi = a.end()+1;
                    l = len(r)
                    o = r[fi:l]
                    g = o.split(' ')
                    filtername = g[0]
                    a = re.search(r'\b( term)\b', r)
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
                "inputfilename": tb.tb_frame.f_code.co_inputfilename,
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
    global outputfilename
    global inputfilename
    #end= 1-continue ; 0-stop
    global end
    #check the input and output given
    if (args.output != "aegis") and (args.output != "acl") and (args.output != "qos"):
        print("Please type only aegis or acl or qos for output")
        exit()
    if (args.input != "junos"):
        print("Please type only junos for input")
        exit()
    #if input filename is not given default - eosaegisconf.csv or eosaclconf.csv will be used
    if  (args.outputfilename == None):
        if args.output == "aegis":
            outputfilename = "eosaegisconf.csv"
        elif args.output == "acl":
            outputfilename = "eosaclconf.csv"
        elif args.output == "qos":
            outputfilename = "eosqosconf.csv"
    elif (args.outputfilename != None):
        if '.csv' not in args.outputfilename:
            print(" Output filename must have '.csv' ex:eosaclconf.csv")
            exit()
        outputfilename = args.outputfilename
    #if output filename is not given default - junosconf.csv will be used
    if  (args.inputfilename == None):
        if args.input == "junos":
            inputfilename = "junosconf.csv"
    elif (args.inputfilename != None):
        if '.csv' not in args.inputfilename:
            print(" Output filename must have '.csv' ex:junosconf.csv")
            exit()
        inputfilename = args.inputfilename
    #open("eosqosconf.csv","w")
    open(outputfilename,"w")
    print(f" Outputs stored in {outputfilename}")
    print(f" Reading file {inputfilename} for inputs")
    try:
        open(inputfilename,"r")
    except:
        print(f"Error: {inputfilename} must be in same folder or under '~/' if you run program from that location")
        exit()
    with open(inputfilename,"r") as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            if ("filter" in row[0]) and ("term" in row[0]):
                end = 1
                break
            else:
                continue
    if end == 1:
        #get all filternames and terms
        print(" Input verification completed")
    else:
        print(f"Can't find keywords filter and term in csv file. Please check the csv file {inputfilename}")
        exit()

#choose input(junosconf) and output(aegis or acl) and inputfilename(optional default name is eosqosconf.csv or eosaclconf.csv or eosaegisconf.csv)
def choice():
    parser = argparse.ArgumentParser(description='Process some integers.')
    #inputs
    #1)junos
    parser.add_argument('input', help='Type of input given is junos')
    #inputfilename
    parser.add_argument('--inputfilename', help='Optional input filename, if not given default will be used')
    #outputs
    #1)qos 2)aegis 3)acl
    parser.add_argument('output', help='Type of output needed is qos or aegis or acl.')
    #outputfilename
    parser.add_argument('--outputfilename', help='Optional output filename, if not given default will be used')
    global args
    args = parser.parse_args()
    
#just call functions in suence order
def main():
    #choose(argparse) input(junosconf) and output(aegis or acl)
    choice()
    #do precheck to make sure the junos conf in the csv file
    precheck()
    #get all filternames and terms
    getfilternames()
    #conversion step and process
    convert()
    
if __name__=='__main__':
       main()