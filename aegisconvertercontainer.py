#! /usr/bin/env python3
#SHEBANG
import re
#read this prgram from bottom to top for understanding
import csv
import argparse
#add time if you need slow in output generation on screen
#import time

#if count in decision on acl
def aclcount():
    if count != 0:
        with open("eosaclconf.csv","a") as eos:
            eos.write("counter per-entry\n")
            print("counter per-entry")
            
def aclcondition():
    with open("eosaclconf.csv","a") as eos:
        #with protocol and source and destination prefixlist
        #if protocol, source prefix list, source-port(srcport), destination prefix list, destination-port(destiport) are present ; port after source(srcadport), port after destination(destiadport) are not present;
        if (protocol != 0) and (srcprelist != 0)  and (srcport != 0) and (destprelist != 0) and (destiport != 0) and (srcadport == 0) and (destiadport == 0):
            for protoco in protocols:
                for src in srcas:
                    for dest in destas:
                        for srcportjoin in srcportjoinfinal:
                            for destasportjoin in destasportjoinfinal:
                                eos.write(f"{deci} {protoco} {src} {srcportjoin} {dest} {destasportjoin}\n")
                                print(f"{deci} {protoco} {src} {srcportjoin} {dest} {destasportjoin}")
        elif (protocol != 0) and (srcprelist == 0)  and (srcport == 0) and (destprelist != 0) and (destiport == 0) and (srcadport == 0) and (destiadport != 0):
            for protoco in protocols:
                    for dest in destas:
                        eos.write(f"{deci} {protoco} any {dest} {destiadport}\n")
                        print(f"{deci} {protoco} any {dest} {destiadport}")
        elif (protocol != 0) and (srcprelist != 0)  and (srcport == 0) and (destprelist == 0) and (destiport == 0) and (srcadport != 0) and (destiadport != 0):
            for protoco in protocols:
                for src in srcas:
                    eos.write(f"{deci} {protoco} {src} {srcadport} any {destiadport} \n")
                    print(f"{deci} {protoco} {src} {srcadport} any {destiadport}")
        elif (protocol != 0) and (srcprelist == 0)  and (srcport != 0) and (destprelist == 0) and (destiport == 0) and (srcadport == 0) and (destiadport != 0):
            for protoco in protocols:
                for srcportjoin in srcportjoinfinal:
                    eos.write(f"{deci} {protoco} any {srcportjoin} any {destiadport}\n")
                    print(f"{deci} {protoco} any {srcportjoin} anany {destiadport}")
        elif (protocol != 0) and (srcprelist == 0)  and (srcport == 0) and (destprelist != 0) and (destiport == 0) and (srcadport != 0) and (destiadport != 0):
            for protoco in protocols:
                for dest in destas:
                    eos.write(f"{deci} {protoco} any {srcadport} {dest} {destiadport} \n")
                    print(f"{deci} {protoco} any {srcadport} {dest} {destiadport}")
        elif (protocol != 0) and (srcprelist == 0)  and (srcport == 0) and (destprelist == 0) and (destiport != 0) and (srcadport != 0) and (destiadport == 0):
            for protoco in protocols:
                for destasportjoin in destasportjoinfinal:
                    eos.write(f"{deci} {protoco} any {srcadport} any {destasportjoin}\n")
                    print(f"{deci} {protoco} any {srcadport} any {destasportjoin}")
        elif (protocol != 0) and (srcprelist != 0)  and (srcport != 0) and (destprelist != 0) and (destiport == 0) and (srcadport == 0) and (destiadport != 0):
            for protoco in protocols:
                for src in srcas:
                    for dest in destas:
                        for srcportjoin in srcportjoinfinal:
                            eos.write(f"{deci} {protoco} {src} {srcportjoin} {dest} {destiadport} \n")
                            print(f"{deci} {protoco} {src} {srcportjoin} {dest} {destiadport}")
        elif (protocol != 0) and (srcprelist != 0)  and (srcport != 0) and (destprelist == 0) and (destiport == 0) and (srcadport == 0) and (destiadport != 0):
            for protoco in protocols:
                for src in srcas:
                    for srcportjoin in srcportjoinfinal:
                        eos.write(f"{deci} {protoco} {src} {srcportjoin} any {destiadport}\n")
                        print(f"{deci} {protoco} {src} {srcportjoin} anany {destiadport}")
        elif (protocol != 0) and (srcprelist == 0)  and (srcport != 0) and (destprelist != 0) and (destiport == 0) and (srcadport == 0) and (destiadport != 0):
            for protoco in protocols:
                for dest in destas:
                    for srcportjoin in srcportjoinfinal:
                        eos.write(f"{deci} {protoco} any {srcportjoin} {dest} {destiadport}\n")
                        print(f"{deci} {protoco} any {srcportjoin} {dest} {destiadport}")
        elif (protocol != 0) and (srcprelist != 0)  and (srcport == 0) and (destprelist != 0) and (destiport == 0) and (srcadport != 0) and (destiadport != 0):
            for protoco in protocols:
                for src in srcas:
                    for dest in destas:
                        eos.write(f"{deci} {protoco} {src} {srcadport}  {dest} {destiadport}\n")
                        print(f"{deci} {protoco} {src} {srcadport}  {dest} {destiadport}")
        elif (protocol != 0) and (srcprelist == 0)  and (srcport == 0) and (destprelist == 0) and (destiport != 0) and (srcadport != 0) and (destiadport == 0):
            for protoco in protocols:
                for destasportjoin in destasportjoinfinal:
                    eos.write(f"{deci} {protoco} any {srcadport} any {destasportjoin} \n")
                    print(f"{deci} {protoco} any {srcadport} any {destasportjoin}")
        elif (protocol != 0) and (srcprelist != 0)  and (srcport == 0) and (destprelist == 0) and (destiport != 0) and (srcadport != 0) and (destiadport == 0):
            for protoco in protocols:
                for src in srcas:
                    for destasportjoin in destasportjoinfinal:
                        eos.write(f"{deci} {protoco} {src} {srcadport} any {destasportjoin} \n")
                        print(f"{deci} {protoco} {src} {srcadport} any {destasportjoin}")             
        elif (protocol != 0) and (srcprelist == 0)  and (srcport != 0) and (destprelist == 0) and (destiport == 0) and (srcadport == 0) and (destiadport != 0):
            for protoco in protocols:
                for srcportjoin in srcportjoinfinal:
                    eos.write(f"{deci} {protoco} any {srcportjoin} any {destiadport}\n")
                    print(f"{deci} {protoco} any {srcportjoin} anany {destiadport}")
        elif (protocol != 0) and (srcprelist == 0)  and (srcport != 0) and (destprelist != 0) and (destiport != 0) and (srcadport == 0) and (destiadport == 0):
            for protoco in protocols:
                for dest in destas:
                    for srcportjoin in srcportjoinfinal:
                        for destasportjoin in destasportjoinfinal:
                            eos.write(f"{deci} {protoco} any {srcportjoin} {dest} {destasportjoin} \n")
                            print(f"{deci} {protoco} any {srcportjoin} {dest} {destasportjoin} ") 
        elif (protocol != 0) and (srcprelist != 0)  and (srcport == 0) and (destprelist != 0) and (destiport != 0) and (srcadport != 0) and (destiadport == 0):
            for protoco in protocols:
                for src in srcas:
                    for dest in destas:
                        for srcportjoin in srcportjoinfinal:
                            for destasportjoin in destasportjoinfinal:
                                eos.write(f"{deci} {protoco} {src} {srcadport} {dest} {destasportjoin}\n")
                                print(f"{deci} {protoco} {src} {srcadport} {dest} {destasportjoin}")
        elif (protocol != 0) and (srcprelist != 0)  and (srcport != 0) and (destprelist == 0) and (destiport != 0) and (srcadport == 0) and (destiadport == 0):
            for protoco in protocols:
                for src in srcas:
                    for srcportjoin in srcportjoinfinal:
                        for destasportjoin in destasportjoinfinal:
                            eos.write(f"{deci} {protoco} {src} {srcportjoin} any {destasportjoin}\n")
                            print(f"{deci} {protoco} {src} {srcportjoin} any {destasportjoin}")
        elif (protocol != 0) and (srcprelist == 0)  and (srcport != 0) and (destprelist == 0) and (destiport != 0) and (srcadport == 0) and (destiadport == 0):
            for protoco in protocols:
                for src in srcas:
                    for srcportjoin in srcportjoinfinal:
                        for destasportjoin in destasportjoinfinal:
                            eos.write(f"{deci} {protoco} any {srcportjoin} any {destasportjoin}\n")
                            print(f"{deci} {protoco} any {srcportjoin} any {destasportjoin}")
        elif (protocol != 0) and (srcprelist == 0)  and (srcport == 0) and (destprelist == 0) and (destiport == 0) and (srcadport != 0) and (destiadport != 0):
            for protoco in protocols:
                for src in srcas:
                    for dest in destas:
                        eos.write(f"{deci} {protoco} any {srcadport} any {destiadport}\n")
                        print(f"{deci} {protoco} any {srcadport} anany {destiadport}")
        #without protocol with source and destination prefixlist
        elif (protocol == 0) and (srcprelist != 0)  and (srcport != 0) and (destprelist != 0) and (destiport != 0) and (srcadport == 0) and (destiadport == 0):
            for src in srcas:
                for dest in destas:
                    for srcportjoin in srcportjoinfinal:
                        for destasportjoin in destasportjoinfinal:
                            eos.write(f"{deci} ip {src} {srcportjoin} {dest} {destasportjoin}\n")
                            print(f"{deci} ip {src} {srcportjoin} {dest} {destasportjoin}")
        elif (protocol == 0) and (srcprelist != 0)  and (srcport == 0) and (destprelist == 0) and (destiport == 0) and (srcadport != 0) and (destiadport != 0):
            for src in srcas:
                eos.write(f"{deci} ip {src} any \n")
                print(f"{deci} ip {src} any ")
        elif (protocol == 0) and (srcprelist == 0)  and (srcport != 0) and (destprelist == 0) and (destiport == 0) and (srcadport == 0) and (destiadport != 0):
            for srcportjoin in srcportjoinfinal:
                eos.write(f"{deci} ip any {srcportjoin} any {destiadport}\n")
                print(f"{deci} ip any {srcportjoin} anany {destiadport}")
        elif (protocol == 0) and (srcprelist == 0)  and (srcport == 0) and (destprelist != 0) and (destiport == 0) and (srcadport != 0) and (destiadport != 0):
            
                for dest in destas:
                    eos.write(f"{deci} ip any {srcadport} {dest} {destiadport}\n")
                    print(f"{deci} ip any {srcadport} {dest} {destiadport}")
        elif (protocol == 0) and (srcprelist == 0)  and (srcport == 0) and (destprelist == 0) and (destiport != 0) and (srcadport != 0) and (destiadport == 0):
            for destasportjoin in destasportjoinfinal:
                eos.write(f"{deci} ip any {srcadport} any {destasportjoin} \n")
                print(f"{deci} ip any {srcadport} any {destasportjoin}")
        elif (protocol == 0) and (srcprelist != 0)  and (srcport != 0) and (destprelist != 0) and (destiport == 0) and (srcadport == 0) and (destiadport != 0):
            for srcportjoin in srcportjoinfinal:
                for src in srcas:
                    for dest in destas:
                        eos.write(f"{deci} ip {src} {srcportjoin} {dest} {destiadport}\n")
                        print(f"{deci} ip {src} {srcportjoin} {dest} {destiadport}")
        elif (protocol == 0) and (srcprelist != 0)  and (srcport != 0) and (destprelist == 0) and (destiport == 0) and (srcadport == 0) and (destiadport != 0):
            for srcportjoin in srcportjoinfinal:
                for src in srcas:
                    eos.write(f"{deci} ip {src} {srcportjoin} any {destiadport}\n")
                    print(f"{deci} ip {src} {srcportjoin} anany {destiadport}")
        elif (protocol == 0) and (srcprelist == 0)  and (srcport != 0) and (destprelist != 0) and (destiport == 0) and (srcadport == 0) and (destiadport != 0):
                for dest in destas:
                    eos.write(f"{deci} ip any {srcportjoin} {dest} {destiadport}\n")
                    print(f"{deci} ip any {srcportjoin} {dest} {destiadport}")
        elif (protocol == 0) and (srcprelist != 0)  and (srcport == 0) and (destprelist != 0) and (destiport == 0) and (srcadport != 0) and (destiadport != 0):
                for src in srcas:
                    for dest in destas:
                        eos.write(f"{deci} ip {src} {srcadport} {dest} {destiadport}\n")
                        print(f"{deci} ip {src} {srcadport} {dest} {destiadport}")
        elif (protocol == 0) and (srcprelist == 0)  and (srcport == 0) and (destprelist == 0) and (destiport != 0) and (srcadport != 0) and (destiadport == 0):
            for destasportjoin in destasportjoinfinal:  
                eos.write(f"{deci} ip any {srcadport} any {destasportjoin} \n")
                print(f"{deci} ip any {srcadport} any {destasportjoin}")
        elif (protocol == 0) and (srcprelist != 0)  and (srcport == 0) and (destprelist == 0) and (destiport != 0) and (srcadport != 0) and (destiadport == 0):
            for destasportjoin in destasportjoinfinal:
                for src in srcas:
                    eos.write(f"{deci} ip {src} {srcadport} any {destasportjoin} \n")
                    print(f"{deci} ip {src} {srcadport} any {destasportjoin}")             
        elif (protocol == 0) and (srcprelist == 0)  and (srcport != 0) and (destprelist == 0) and (destiport == 0) and (srcadport == 0) and (destiadport != 0):
            for srcportjoin in srcportjoinfinal:
                eos.write(f"{deci} ip any {srcportjoin} any {destiadport}\n")
                print(f"{deci} ip any {srcportjoin} anany {destiadport}")
        elif (protocol == 0) and (srcprelist == 0)  and (srcport != 0) and (destprelist != 0) and (destiport != 0) and (srcadport == 0) and (destiadport == 0):
            for srcportjoin in srcportjoinfinal:
                for destasportjoin in destasportjoinfinal:
                    for dest in destas:
                        eos.write(f"{deci} ip any {srcportjoin} {dest} {destasportjoin} \n")
                        print(f"{deci} ip any {srcportjoin} {dest} {destasportjoin} ") 
        elif (protocol == 0) and (srcprelist != 0)  and (srcport == 0) and (destprelist != 0) and (destiport != 0) and (srcadport != 0) and (destiadport == 0):
            for destasportjoin in destasportjoinfinal:           
                for src in srcas:
                    for dest in destas:
                        eos.write(f"{deci} ip {src} {srcadport} {dest} {destasportjoin}\n")
                        print(f"{deci} ip {src} {srcadport} {dest} {destasportjoin}")
        elif (protocol == 0) and (srcprelist != 0)  and (srcport != 0) and (destprelist == 0) and (destiport != 0) and (srcadport == 0) and (destiadport == 0):
            for srcportjoin in srcportjoinfinal:
                for destasportjoin in destasportjoinfinal: 
                    for src in srcas:
                        eos.write(f"{deci} ip {src} {srcportjoin} any {destasportjoin}\n")
                        print(f"{deci} ip {src} {srcportjoin} any {destasportjoin}")
        elif (protocol == 0) and (srcprelist == 0)  and (srcport != 0) and (destprelist == 0) and (destiport != 0) and (srcadport == 0) and (destiadport == 0):
            for srcportjoin in srcportjoinfinal:
                for destasportjoin in destasportjoinfinal:
                    for src in srcas:
                        eos.write(f"{deci} ip any {srcportjoin} any {destasportjoin}\n")
                        print(f"{deci} ip any {srcportjoin} any {destasportjoin}")
        elif (protocol == 0) and (srcprelist == 0)  and (srcport == 0) and (destprelist == 0) and (destiport == 0) and (srcadport != 0) and (destiadport != 0):
                for src in srcas:
                    for dest in destas:
                        eos.write(f"{deci} ip any {srcadport} any {destiadport}\n")
                        print(f"{deci} ip any {srcadport} anany {destiadport}")
        #with only ports keyword not present
        elif (protocol != 0) and (srcprelist != 0)  and (srcport != 0) and (destprelist != 0) and (destiport != 0) and (srcadport == 0) and (destiadport == 0):
            for protoco in protocols:
                for src in srcas:
                    for dest in destas:
                        for srcportjoin in srcportjoinfinal:
                            for destasportjoin in destasportjoinfinal:
                                eos.write(f"{deci} {protoco} {src} {srcportjoin} {dest} {destasportjoin}\n")
                                print(f"{deci} {protoco} {src} {srcportjoin} {dest} {destasportjoin}")
        elif (protocol != 0) and (srcprelist != 0)  and (srcport == 0) and (destprelist == 0) and (destiport == 0) and (srcadport == 0) and (destiadport == 0):
            for protoco in protocols:
                for src in srcas:
                    eos.write(f"{deci} {protoco} {src} any \n")
                    print(f"{deci} {protoco} {src} any ")
        elif (protocol != 0) and (srcprelist == 0)  and (srcport != 0) and (destprelist == 0) and (destiport == 0) and (srcadport == 0) and (destiadport == 0):
            for protoco in protocols:
                for srcportjoin in srcportjoinfinal:
                    eos.write(f"{deci} {protoco} any {srcportjoin} any \n")
                    print(f"{deci} {protoco} any {srcportjoin} any")
        elif (protocol != 0) and (srcprelist == 0)  and (srcport == 0) and (destprelist != 0) and (destiport == 0) and (srcadport == 0) and (destiadport == 0):
            for protoco in protocols:
                for dest in destas:
                    eos.write(f"{deci} {protoco} any {dest} \n")
                    print(f"{deci} {protoco} any {dest}")
        elif (protocol != 0) and (srcprelist == 0)  and (srcport == 0) and (destprelist == 0) and (destiport != 0) and (srcadport == 0) and (destiadport == 0):
            for protoco in protocols:
                for destasportjoin in destasportjoinfinal:
                    eos.write(f"{deci} {protoco} any any {destasportjoin} \n")
                    print(f"{deci} {protoco} any any {destasportjoin}")
        elif (protocol != 0) and (srcprelist != 0)  and (srcport != 0) and (destprelist != 0) and (destiport == 0) and (srcadport == 0) and (destiadport == 0):
            for protoco in protocols:
                for src in srcas:
                    for dest in destas:
                        for srcportjoin in srcportjoinfinal:
                            eos.write(f"{deci} {protoco} {src} {srcportjoin} {dest} \n")
                            print(f"{deci} {protoco} {src} {srcportjoin} {dest} ")
        elif (protocol != 0) and (srcprelist != 0)  and (srcport != 0) and (destprelist == 0) and (destiport == 0) and (srcadport == 0) and (destiadport == 0):
            for protoco in protocols:
                for src in srcas:
                    for srcportjoin in srcportjoinfinal:
                        eos.write(f"{deci} {protoco} {src} {srcportjoin} any \n")
                        print(f"{deci} {protoco} {src} {srcportjoin} any ")
        elif (protocol != 0) and (srcprelist == 0)  and (srcport != 0) and (destprelist != 0) and (destiport == 0) and (srcadport == 0) and (destiadport == 0):
            for protoco in protocols:
                for dest in destas:
                    for srcportjoin in srcportjoinfinal:
                        eos.write(f"{deci} {protoco} any {srcportjoin} {dest}\n")
                        print(f"{deci} {protoco} any {srcportjoin} {dest}")
        elif (protocol != 0) and (srcprelist != 0)  and (srcport == 0) and (destprelist != 0) and (destiport == 0) and (srcadport == 0) and (destiadport == 0):
            for protoco in protocols:
                for src in srcas:
                    for dest in destas:
                        eos.write(f"{deci} {protoco} {src} {dest} \n")
                        print(f"{deci} {protoco} {src} {dest} ")
        elif (protocol != 0) and (srcprelist == 0)  and (srcport == 0) and (destprelist == 0) and (destiport != 0) and (srcadport == 0) and (destiadport == 0):
            for protoco in protocols:
                for destasportjoin in destasportjoinfinal:
                    eos.write(f"{deci} {protoco} any any {destasportjoin} \n")
                    print(f"{deci} {protoco} any any {destasportjoin}")
        elif (protocol != 0) and (srcprelist != 0)  and (srcport == 0) and (destprelist == 0) and (destiport != 0) and (srcadport == 0) and (destiadport == 0):
            for protoco in protocols:
                for src in srcas:
                    for destasportjoin in destasportjoinfinal:
                        eos.write(f"{deci} {protoco} {src} any {destasportjoin} \n")
                        print(f"{deci} {protoco} {src} any {destasportjoin}")             
        elif (protocol != 0) and (srcprelist == 0)  and (srcport != 0) and (destprelist == 0) and (destiport == 0) and (srcadport == 0) and (destiadport == 0):
            for protoco in protocols:
                for srcportjoin in srcportjoinfinal:
                    eos.write(f"{deci} {protoco} any {srcportjoin} any \n")
                    print(f"{deci} {protoco} any {srcportjoin} any ")
        elif (protocol != 0) and (srcprelist == 0)  and (srcport != 0) and (destprelist != 0) and (destiport != 0) and (srcadport == 0) and (destiadport == 0):
            for protoco in protocols:
                for dest in destas:
                    for srcportjoin in srcportjoinfinal:
                        for destasportjoin in destasportjoinfinal:
                            eos.write(f"{deci} {protoco} any {srcportjoin} {dest} {destasportjoin} \n")
                            print(f"{deci} {protoco} any {srcportjoin} {dest} {destasportjoin} ") 
        elif (protocol != 0) and (srcprelist != 0)  and (srcport == 0) and (destprelist != 0) and (destiport != 0) and (srcadport == 0) and (destiadport == 0):
            for protoco in protocols:
                for src in srcas:
                    for dest in destas:
                        for srcportjoin in srcportjoinfinal:
                            for destasportjoin in destasportjoinfinal:
                                eos.write(f"{deci} {protoco} {src} {dest} {destasportjoin}\n")
                                print(f"{deci} {protoco} {src} {dest} {destasportjoin}")
        elif (protocol != 0) and (srcprelist != 0)  and (srcport != 0) and (destprelist == 0) and (destiport != 0) and (srcadport == 0) and (destiadport == 0):
            for protoco in protocols:
                for src in srcas:
                    for srcportjoin in srcportjoinfinal:
                        for destasportjoin in destasportjoinfinal:
                            eos.write(f"{deci} {protoco} {src} {srcportjoin} any {destasportjoin}\n")
                            print(f"{deci} {protoco} {src} {srcportjoin} any {destasportjoin}")
        elif (protocol != 0) and (srcprelist == 0)  and (srcport != 0) and (destprelist == 0) and (destiport != 0) and (srcadport == 0) and (destiadport == 0):
            for protoco in protocols:
                for srcportjoin in srcportjoinfinal:
                    for destasportjoin in destasportjoinfinal:
                        eos.write(f"{deci} {protoco} any {srcportjoin} any {destasportjoin}\n")
                        print(f"{deci} {protoco} any {srcportjoin} any {destasportjoin}")
        elif (protocol != 0) and (srcprelist != 0)  and (srcport == 0) and (destprelist == 0) and (destiport == 0) and (srcadport != 0) and (destiadport == 0):
            for protoco in protocols:
                for src in srcas:
                    eos.write(f"{deci} {protoco} {src} {srcadport} any\n")
                    print(f"{deci} {protoco} {src} {srcadport} any")
        elif (protocol != 0) and (srcprelist == 0)  and (srcport == 0) and (destprelist != 0) and (destiport != 0) and (srcadport == 0) and (destiadport == 0):
            for protoco in protocols:
                    for dest in destas:
                        for destasportjoin in destasportjoinfinal:
                            eos.write(f"{deci} {protoco} any {dest} {destasportjoinfinal}\n")
                            print(f"{deci} {protoco} any {dest} {destasportjoinfinal}")
        elif (protocol != 0) and (srcprelist != 0)  and (srcport == 0) and (destprelist != 0) and (destiport == 0) and (srcadport == 0) and (destiadport != 0):
            for protoco in protocols:
                for src in srcas:
                    for dest in destas:
                        eos.write(f"{deci} {protoco} {src} {dest} {destiadport}\n")
                        print(f"{deci} {protoco} {src} {dest} {destiadport}")
        elif (protocol != 0) and (srcprelist == 0)  and (srcport == 0) and (destprelist == 0) and (destiport == 0) and (srcadport == 0) and (destiadport == 0):
            for protoco in protocols:
                for src in srcas:
                    for dest in destas:
                        eos.write(f"{deci} {protoco} any any\n")
                        print(f"{deci} {protoco} any any")
        #without protocol with source and destination prefixlist
        elif (protocol == 0) and (srcprelist != 0)  and (srcport != 0) and (destprelist != 0) and (destiport != 0) and (srcadport == 0) and (destiadport == 0):
            for src in srcas:
                for dest in destas:
                    for srcportjoin in srcportjoinfinal:
                        for destasportjoin in destasportjoinfinal:
                            eos.write(f"{deci} ip {src} {srcportjoin} {dest} {destasportjoin}\n")
                            print(f"{deci} ip {src} {srcportjoin} {dest} {destasportjoin}")
        elif (protocol == 0) and (srcprelist != 0)  and (srcport == 0) and (destprelist == 0) and (destiport == 0) and (srcadport == 0) and (destiadport == 0):
            for src in srcas:
                eos.write(f"{deci} ip {src} any \n")
                print(f"{deci} ip {src} any ")
        elif (protocol == 0) and (srcprelist == 0)  and (srcport != 0) and (destprelist == 0) and (destiport == 0) and (srcadport == 0) and (destiadport == 0):
            for srcportjoin in srcportjoinfinal:
                eos.write(f"{deci} ip any {srcportjoin} any \n")
                print(f"{deci} ip any {srcportjoin} any")
        elif (protocol == 0) and (srcprelist == 0)  and (srcport == 0) and (destprelist != 0) and (destiport == 0) and (srcadport == 0) and (destiadport == 0):         
                for dest in destas:
                    eos.write(f"{deci} ip any {dest} \n")
                    print(f"{deci} ip any {dest}")
        elif (protocol == 0) and (srcprelist == 0)  and (srcport == 0) and (destprelist == 0) and (destiport != 0) and (srcadport == 0) and (destiadport == 0):
            for destasportjoin in destasportjoinfinal:
                eos.write(f"{deci} ip any any {destasportjoin} \n")
                print(f"{deci} ip any any {destasportjoin}")
        elif (protocol == 0) and (srcprelist != 0)  and (srcport != 0) and (destprelist != 0) and (destiport == 0) and (srcadport == 0) and (destiadport == 0):
            for srcportjoin in srcportjoinfinal:
                for src in srcas:
                    for dest in destas:
                        eos.write(f"{deci} ip {src} {srcportjoin} {dest} \n")
                        print(f"{deci} ip {src} {srcportjoin} {dest} ")
        elif (protocol == 0) and (srcprelist != 0)  and (srcport != 0) and (destprelist == 0) and (destiport == 0) and (srcadport == 0) and (destiadport == 0):
            for srcportjoin in srcportjoinfinal:
                for src in srcas:
                    eos.write(f"{deci} ip {src} {srcportjoin} any \n")
                    print(f"{deci} ip {src} {srcportjoin} any ")
        elif (protocol == 0) and (srcprelist == 0)  and (srcport != 0) and (destprelist != 0) and (destiport == 0) and (srcadport == 0) and (destiadport == 0):
            
                for dest in destas:
                    eos.write(f"{deci} ip any {srcportjoin} {dest}\n")
                    print(f"{deci} ip any {srcportjoin} {dest}")
        elif (protocol == 0) and (srcprelist != 0)  and (srcport == 0) and (destprelist != 0) and (destiport == 0) and (srcadport == 0) and (destiadport == 0):
                for src in srcas:
                    for dest in destas:
                        eos.write(f"{deci} ip {src} {dest} \n")
                        print(f"{deci} ip {src} {dest} ")
        elif (protocol == 0) and (srcprelist == 0)  and (srcport == 0) and (destprelist == 0) and (destiport != 0) and (srcadport == 0) and (destiadport == 0):
            for destasportjoin in destasportjoinfinal:  
                eos.write(f"{deci} ip any any {destasportjoin} \n")
                print(f"{deci} ip any any {destasportjoin}")
        elif (protocol == 0) and (srcprelist != 0)  and (srcport == 0) and (destprelist == 0) and (destiport != 0) and (srcadport == 0) and (destiadport == 0):
            for destasportjoin in destasportjoinfinal:
                for src in srcas:
                    eos.write(f"{deci} ip {src} any {destasportjoin} \n")
                    print(f"{deci} ip {src} any {destasportjoin}")             
        elif (protocol == 0) and (srcprelist == 0)  and (srcport != 0) and (destprelist == 0) and (destiport == 0) and (srcadport == 0) and (destiadport == 0):
            for srcportjoin in srcportjoinfinal:
                eos.write(f"{deci} ip any {srcportjoin} any \n")
                print(f"{deci} ip any {srcportjoin} any ")
        elif (protocol == 0) and (srcprelist == 0)  and (srcport != 0) and (destprelist != 0) and (destiport != 0) and (srcadport == 0) and (destiadport == 0):
            for srcportjoin in srcportjoinfinal:
                for destasportjoin in destasportjoinfinal:
                    for dest in destas:
                        eos.write(f"{deci} ip any {srcportjoin} {dest} {destasportjoin} \n")
                        print(f"{deci} ip any {srcportjoin} {dest} {destasportjoin} ") 
        elif (protocol == 0) and (srcprelist != 0)  and (srcport == 0) and (destprelist != 0) and (destiport != 0) and (srcadport == 0) and (destiadport == 0):
            for destasportjoin in destasportjoinfinal:           
                for src in srcas:
                    for dest in destas:
                        eos.write(f"{deci} ip {src} {dest} {destasportjoin}\n")
                        print(f"{deci} ip {src} {dest} {destasportjoin}")
        elif (protocol == 0) and (srcprelist != 0)  and (srcport != 0) and (destprelist == 0) and (destiport != 0) and (srcadport == 0) and (destiadport == 0):
            for srcportjoin in srcportjoinfinal:
                for destasportjoin in destasportjoinfinal: 
                    for src in srcas:
                        eos.write(f"{deci} ip {src} {srcportjoin} any {destasportjoin}\n")
                        print(f"{deci} ip {src} {srcportjoin} any {destasportjoin}")
        elif (protocol == 0) and (srcprelist == 0)  and (srcport != 0) and (destprelist == 0) and (destiport != 0) and (srcadport == 0) and (destiadport == 0):
            for srcportjoin in srcportjoinfinal:
                for destasportjoin in destasportjoinfinal:
                    for src in srcas:
                        eos.write(f"{deci} ip any {srcportjoin} any {destasportjoin}\n")
                        print(f"{deci} ip any {srcportjoin} any {destasportjoin}")
        elif (protocol == 0) and (srcprelist == 0)  and (srcport == 0) and (destprelist == 0) and (destiport == 0) and (srcadport == 0) and (destiadport == 0):
                for src in srcas:
                    for dest in destas:
                        eos.write(f"{deci} ip any any\n")
                        print(f"{deci} ip any any")

        #with protocol and source address and destination address
        elif (protocol != 0) and (srcadd != 0)  and (srcadport != 0) and (destadd != 0) and (destiadport != 0):
            for protoco in protocols:
                for srcad in srcadds:
                    for destad in destadds:
                        eos.write(f"{deci} {protoco} {srcad}  {srcadport} {destad}  {destiadport}\n")
                        print(f"{deci} {protoco} {srcad}  {srcadport} {destad}  {destiadport}")
        elif (protocol != 0) and (srcadd != 0)  and (srcadport == 0) and (destadd == 0) and (destiadport == 0):
            for protoco in protocols:
                for srcad in srcadds:
                    eos.write(f"{deci} {protoco} {srcad} any \n")
                    print(f"{deci} {protoco} {srcad} any ")
        elif (protocol != 0) and (srcadd == 0)  and (srcadport != 0) and (destadd == 0) and (destiadport == 0):
            for protoco in protocols:
                eos.write(f"{deci} {protoco} any  {srcadport} any \n")
                print(f"{deci} {protoco} any  {srcadport} any")
        elif (protocol != 0) and (srcadd == 0)  and (srcadport == 0) and (destadd != 0) and (destiadport == 0):
            for protoco in protocols:
                for destad in destadds:
                    eos.write(f"{deci} {protoco} any {destad} \n")
                    print(f"{deci} {protoco} any {destad}")
        elif (protocol != 0) and (srcadd == 0)  and (srcadport == 0) and (destadd == 0) and (destiadport != 0):
            for protoco in protocols:
                eos.write(f"{deci} {protoco} any any {destiadport}\n")
                print(f"{deci} {protoco} any any {destiadport}")
        elif (protocol != 0) and (srcadd != 0)  and (srcadport != 0) and (destadd != 0) and (destiadport == 0):
            for protoco in protocols:
                for srcad in srcadds:
                    for destad in destadds:
                        eos.write(f"{deci} {protoco} {srcad}  {srcadport} {destad} \n")
                        print(f"{deci} {protoco} {srcad}  {srcadport} {destad} ")
        elif (protocol != 0) and (srcadd != 0)  and (srcadport != 0) and (destadd == 0) and (destiadport == 0):
            for protoco in protocols:
                for srcad in srcadds:
                    eos.write(f"{deci} {protoco} {srcad}  {srcadport} any \n")
                    print(f"{deci} {protoco} {srcad}  {srcadport} any ")
        elif (protocol != 0) and (srcadd == 0)  and (srcadport != 0) and (destadd != 0) and (destiadport == 0):
            for protoco in protocols:
                for destad in destadds:
                    eos.write(f"{deci} {protoco} any  {srcadport} {destad}\n")
                    print(f"{deci} {protoco} any  {srcadport} {destad}")
        elif (protocol != 0) and (srcadd != 0)  and (srcadport == 0) and (destadd != 0) and (destiadport == 0):
            for protoco in protocols:
                for srcad in srcadds:
                    for destad in destadds:
                        eos.write(f"{deci} {protoco} {srcad} {destad} \n")
                        print(f"{deci} {protoco} {srcad} {destad} ")
        elif (protocol != 0) and (srcadd == 0)  and (srcadport == 0) and (destadd == 0) and (destiadport != 0):
            for protoco in protocols:
                eos.write(f"{deci} {protoco} any any  {destiadport} \n")
                print(f"{deci} {protoco} any any  {destiadport}")
        elif (protocol != 0) and (srcadd != 0)  and (srcadport == 0) and (destadd == 0) and (destiadport != 0):
            for protoco in protocols:
                for srcad in srcadds:
                    eos.write(f"{deci} {protoco} {srcad} any  {destiadport} \n")
                    print(f"{deci} {protoco} {srcad} any  {destiadport}")             
        elif (protocol != 0) and (srcadd == 0)  and (srcadport != 0) and (destadd == 0) and (destiadport == 0):
            for protoco in protocols:
                eos.write(f"{deci} {protoco} any  {srcadport} any \n")
                print(f"{deci} {protoco} any  {srcadport} any ")
        elif (protocol != 0) and (srcadd == 0)  and (srcadport != 0) and (destadd != 0) and (destiadport != 0):
            for protoco in protocols:
                for destad in destadds:
                    eos.write(f"{deci} {protoco} any  {srcadport} {destad}  {destiadport} \n")
                    print(f"{deci} {protoco} any  {srcadport} {destad}  {destiadport} ") 
        elif (protocol != 0) and (srcadd != 0)  and (srcadport == 0) and (destadd != 0) and (destiadport != 0):
            for protoco in protocols:
                for srcad in srcadds:
                    for destad in destadds:
                        eos.write(f"{deci} {protoco} {srcad} {destad}  {destiadport}\n")
                        print(f"{deci} {protoco} {srcad} {destad}  {destiadport}")
        elif (protocol != 0) and (srcadd != 0)  and (srcadport != 0) and (destadd == 0) and (destiadport != 0):
            for protoco in protocols:
                for srcad in srcadds:
                    eos.write(f"{deci} {protoco} {srcad}  {srcadport} any  {destiadport}\n")
                    print(f"{deci} {protoco} {srcad}  {srcadport} any  {destiadport}")
        elif (protocol != 0) and (srcadd == 0)  and (srcadport != 0) and (destadd == 0) and (destiadport != 0):
            for protoco in protocols:
                for srcad in srcadds:
                    eos.write(f"{deci} {protoco} any  {srcadport} any  {destiadport}\n")
                    print(f"{deci} {protoco} any  {srcadport} any  {destiadport}")
        elif (protocol != 0) and (srcadd == 0)  and (srcadport == 0) and (destadd == 0) and (destiadport == 0):
            for protoco in protocols:
                for srcad in srcadds:
                    for destad in destadds:
                        eos.write(f"{deci} {protoco} any any\n")
                        print(f"{deci} {protoco} any any")
        #without protocol with source and destination prefixlist
        elif (protocol == 0) and (srcadd != 0)  and (srcadport != 0) and (destadd != 0) and (destiadport != 0):   
                for srcad in srcadds:
                    for destad in destadds:
                        eos.write(f"{deci} ip {srcad}  {srcadport} {destad}  {destiadport}\n")
                        print(f"{deci} ip {srcad}  {srcadport} {destad}  {destiadport}")
        elif (protocol == 0) and (srcadd != 0)  and (srcadport == 0) and (destadd == 0) and (destiadport == 0):    
                for srcad in srcadds:
                    eos.write(f"{deci} ip {srcad} any \n")
                    print(f"{deci} ip {srcad} any ")
        elif (protocol == 0) and (srcadd == 0)  and (srcadport != 0) and (destadd == 0) and (destiadport == 0):    
                eos.write(f"{deci} ip any  {srcadport} any \n")
                print(f"{deci} ip any  {srcadport} any")
        elif (protocol == 0) and (srcadd == 0)  and (srcadport == 0) and (destadd != 0) and (destiadport == 0):
                for destad in destadds:
                    eos.write(f"{deci} ip any {destad} \n")
                    print(f"{deci} ip any {destad}")
        elif (protocol == 0) and (srcadd == 0)  and (srcadport == 0) and (destadd == 0) and (destiadport != 0):
                eos.write(f"{deci} ip any any  {destiadport} \n")
                print(f"{deci} ip any any  {destiadport}")
        elif (protocol == 0) and (srcadd != 0)  and (srcadport != 0) and (destadd != 0) and (destiadport == 0):
                for srcad in srcadds:
                    for destad in destadds:
                        eos.write(f"{deci} ip {srcad}  {srcadport} {destad} \n")
                        print(f"{deci} ip {srcad}  {srcadport} {destad} ")
        elif (protocol == 0) and (srcadd != 0)  and (srcadport != 0) and (destadd == 0) and (destiadport == 0):
                for srcad in srcadds:
                    eos.write(f"{deci} ip {srcad}  {srcadport} any \n")
                    print(f"{deci} ip {srcad}  {srcadport} any ")
        elif (protocol == 0) and (srcadd == 0)  and (srcadport != 0) and (destadd != 0) and (destiadport == 0):
                for destad in destadds:
                    eos.write(f"{deci} ip any  {srcadport} {destad}\n")
                    print(f"{deci} ip any  {srcadport} {destad}")
        elif (protocol == 0) and (srcadd != 0)  and (srcadport == 0) and (destadd != 0) and (destiadport == 0):
                for srcad in srcadds:
                    for destad in destadds:
                        eos.write(f"{deci} ip {srcad} {destad} \n")
                        print(f"{deci} ip {srcad} {destad} ")
        elif (protocol == 0) and (srcadd == 0)  and (srcadport == 0) and (destadd == 0) and (destiadport != 0):  
                eos.write(f"{deci} ip any any  {destiadport} \n")
                print(f"{deci} ip any any  {destiadport}")
        elif (protocol == 0) and (srcadd != 0)  and (srcadport == 0) and (destadd == 0) and (destiadport != 0):
                for srcad in srcadds:
                    eos.write(f"{deci} ip {srcad} any  {destiadport} \n")
                    print(f"{deci} ip {srcad} any  {destiadport}")             
        elif (protocol == 0) and (srcadd == 0)  and (srcadport != 0) and (destadd == 0) and (destiadport == 0):
                eos.write(f"{deci} ip any  {srcadport} any \n")
                print(f"{deci} ip any  {srcadport} any ")
        elif (protocol == 0) and (srcadd == 0)  and (srcadport != 0) and (destadd != 0) and (destiadport != 0):  
                for destad in destadds:
                    eos.write(f"{deci} ip any  {srcadport} {destad}  {destiadport} \n")
                    print(f"{deci} ip any  {srcadport} {destad}  {destiadport} ") 
        elif (protocol == 0) and (srcadd != 0)  and (srcadport == 0) and (destadd != 0) and (destiadport != 0):           
                for srcad in srcadds:
                    for destad in destadds:
                        eos.write(f"{deci} ip {srcad} {destad}  {destiadport}\n")
                        print(f"{deci} ip {srcad} {destad}  {destiadport}")
        elif (protocol == 0) and (srcadd != 0)  and (srcadport != 0) and (destadd == 0) and (destiadport != 0): 
                for srcad in srcadds:
                    eos.write(f"{deci} ip {srcad}  {srcadport} any  {destiadport}\n")
                    print(f"{deci} ip {srcad}  {srcadport} any  {destiadport}")
        elif (protocol == 0) and (srcadd == 0)  and (srcadport != 0) and (destadd == 0) and (destiadport != 0):
                for srcad in srcadds:
                    eos.write(f"{deci} ip any  {srcadport} any  {destiadport}\n")
                    print(f"{deci} ip any  {srcadport} any  {destiadport}")
        elif (protocol == 0) and (srcadd == 0)  and (srcadport == 0) and (destadd == 0) and (destiadport == 0):
                for srcad in srcadds:
                    for destad in destadds:
                        eos.write(f"{deci} ip any any\n")
                        print(f"{deci} ip any any")

def aclname():
    with open("eosaclconf.csv","a") as eos:
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
        with open("eosaegisconf.csv","a") as eos:
            eos.write("actions\n")
            print("actions")
            if dscp != 0:
                eos.write(f"dscp {dscpno}\n")
                print(f"dscp {dscpno}")
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
                if protocol != 0:
                    for protoco in protocols:
                        eos.write(f"protocol {protoco} source port {srcport} destination port {destiport}\n")
                        print(f"protocol {protoco} source port {srcport} destination port {destiport}")
                else:
                    eos.write(f"protocol tcp source port {srcport} destination port {destiport}\n")
                    eos.write(f"protocol udp source port {srcport} destination port {destiport}\n")
                    print(f"protocol tcp source port {srcport} destination port {destiport}")
                    print(f"protocol udp source port {srcport} destination port {destiport}")
        except:
            end = 1
        try:        
            if destiport != 0 and srcport == 0:
                if protocol != 0:
                    for protoco in protocols:
                        eos.write(f"protocol {protoco} destination port {destiport}\n")
                        print(f"protocol {protoco} destination port {destiport}")
                else:
                    eos.write(f"protocol tcp destination port {destiport}\n")
                    eos.write(f"protocol udp destination port {destiport}\n")
                    print(f"protocol tcp destination port {destiport}")
                    print(f"protocol udp destination port {destiport}")
        except:
            end = 1
        try:        
            if destiport == 0 and srcport != 0:
                if protocol != 0:
                    for protoco in protocols:
                        eos.write(f"protocol {protoco} source port {destiport}\n")
                        print(f"protocol {protoco} source port {destiport}")
                else:
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
            eos.write("traffic-policies\n")
            print("traffic-policies")
            eos.write(f"field-set ipv4 prefix {filtername}-source\n")
            print(f"field-set ipv4 prefix {filtername}-source")
            for srcad in srcadds:
                eos.write(f"{srcad}\n")
                print(f"{srcad}")
    if destadd != 0:
        with open("eosaegisconf.csv","a") as eos:
            eos.write("traffic-policies\n")
            print("traffic-policies")
            eos.write(f"field-set ipv4 prefix {filtername}-destination\n")
            print(f"field-set ipv4 prefix {filtername}-destination")              
            for destad in destadds:
                eos.write(f"{destad}\n")
                print(f"{destad}")
    if destprelist != 0:
        with open("eosaegisconf.csv","a") as eos:
            eos.write("traffic-policies\n")
            print("traffic-policies")
            eos.write(f"field-set ipv4 prefix {destprelist}\n")
            print(f"field-set ipv4 prefix {destprelist}")
            global dest              
            for dest in destas:
                eos.write(f"{dest}\n")
                print(f"{dest}")
    if srcprelist != 0:
        with open("eosaegisconf.csv","a") as eos:
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
    global srcadport; srcadport = 0
    global destiadport; destiadport = 0
    global destas; destas = []
    global srcas; srcas = []
    global dscpno; dscpno = 0
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
    srcrow = 0
    destrow = 0
    if port != 0:
        rowcount  = 0
        for row in open(filename):
            if (filtername in row) and (comment in row):
                if "destination" in row:
                    destrow=rowcount
                elif "source" in row:
                    srcrow = rowcount 
                rowcount+= 1
        if destrow != 0:
            destiadport = f"eq {port}"
        elif srcrow != 0:
            srcadport = f"eq {port}"
        else:
            destiadport = f"eq {port}"
    #parsing ip address from prefix list if any - prefixlistparse
    if destprelist != 0:
        with open(filename,"r") as file2:
            n2 = file2.readlines();
            for destprelis in destprelists:
                for r2 in n2:
                    #print(r2)
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
                            end=1;
    if srcprelist != 0:
        with open(filename,"r") as file2:
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
                            end=1;
    #dscptable
    if dscp != 0:
        if dscp == 'af41':
            dscpno = 34
        if dscp == 'ef':
            dscpno = 46
        

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
        global dscp; dscp = 0
        with open(filename,"r") as file1:
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
                                ports.append(port)
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

def aegisconvert():
    print("\n Aegis Conversion started...")
    print("Generating aegis Conf....")   
    aegisfieldset()  
    aegistrafficpolicy()
    aegisprefix()
    aegisprotocol()
    aegisaction()
    print("\n Completed configuration generation....")

def convert():
    for filters in filterfinal:
        sep = filters.split(';')
        global filtername
        global comment
        filtername = sep[0]
        comment = sep[1]
        print(f"\nFound filtername: {filtername}")
        print(f"Found Term: {comment}")
        firstparse()
        secondparse()
        print("\nComplete Input:")
        for inputs in completeinput:
            print(inputs.strip())
        if args.output == "aegis":
            aegisconvert()
            #time.sleep is added for slow output generation so that user can read the output easily
            #time.sleep(2)
        #ACL is not fully completed need to work on function arrangements
        elif args.output == "acl":
            aclconvert()
            #time.sleep(2)

#parse junos command for filtername
def getfilternames():
    try:
        filternames = []
        with open(filename,"r") as file:
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
    #check the input and output given
    if (args.output != "aegis") and (args.output != "acl"):
        print("Please type only aegis or acl for output")
        exit()
    if (args.input != "junos"):
        print("Please type only junos for input")
        exit()
    open("eosaclconf.csv","w")
    open("eosaegisconf.csv","w")
    global filename
    #end= 1-continue ; 0-stop
    global end
    print("outputs in 'eosaclconf.csv' & 'eosaegisconf.csv'")
    #this if is for temporary until we complete aegis and acl program complete parallely
    filename = "junosconf.csv"
    print(f"Reading file {filename} for inputs")
    try:
        open(filename,"r")
    except:
        print("Error: 'junosconf.csv' must be in same folder or under '~/' if you run program from that location")
        exit()
    with open(filename,"r") as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            if ("filter" in row[0]) and ("term" in row[0]):
                end = 1
                break
            else:
                continue
    if end == 1:
        #get all filternames and terms
        print("Input verification completed")
    else:
        print(f"Can't find keywords filter and term in csv file. Please check the csv file {filename}")
        exit()

#choose input(junosconf) and output(aegis or acl)
def choice():
    parser = argparse.ArgumentParser(description='Process some integers.')
    #inputs
    #1)junos 2)aegis 3)acl
    parser.add_argument('input', help='Type of input given is junos or aegis or acl.')
    #outputs
    #1)junos 2)aegis 3)acl
    parser.add_argument('output', help='Type of output needed is junos or aegis or acl.')
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