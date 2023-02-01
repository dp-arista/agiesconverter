from conditions import *
from agiesconverter import parse
#import agiesconverter
#convert the junos command to eos command
def convert():
    print(parse.srcadd)
    try:
        try:
            if srcadd != 0 and destadd != 0 and protocol != 0 and port != 0 and count != 0 and deci != 0:
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
        except:
            i=0
        try:
            if srcadd != 0 and destadd != 0 and protocol != 0 and count != 0 and deci != 0:
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
        except:
            i=0
    except Exception as e: 
        print(e)
        print("This looks new type of configuration. Inform developer to add this")
    nextiteration()
