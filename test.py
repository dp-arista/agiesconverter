
#Setting initial value of the counter to zero
rowcount  = 0
#iterating through the whole file
for row in open("/Users/dp/Desktop/dp/agiesconverter/junosconftest.csv"):
    #print(row)
    if "port" in row:
        portrow=rowcount
    rowcount+= 1
print(portrow)
rowcount  = 0
for row in open("/Users/dp/Desktop/dp/agiesconverter/junosconftest.csv"):
    if "destination" in row:
        destrow=rowcount
        #       
    rowcount+= 1
print(destrow) 

if portrow > destrow:
    #eos.write(f"{deci} {protocol} {srcad} {destad} eq {port}")
    print(r"{deci} {protocol} {srcad} {destad} eq {port}")
else:
    #eos.write(f"{deci} {protocol} {srcad} eq {port} {destad} ")
    print(r"{deci} {protocol} {srcad} eq {port} {destad} ")

    