import re
import sys
from collections import OrderedDict

def returnSid(elemen, lista):
    for i in lista:
        if elemen in i:
            index = lista.index(i)+1
            return lista[index].replace("\n", '') 
    return ""

def returnNumber(x):
    if x == "tcp":
        return "1"
    elif x == "ip":
        return "0"       
    elif x == "udp":
        return "2"       
    elif x == "icmp":
        return "3"       

def main():
    #o primeiro argumento deve ser o "community.rules" e o segundo o sid-msg
    community = open(sys.argv[1], 'rt')
    sid_msg = open(sys.argv[2], 'rt')
    protocol = []
    num = []
    sid = []

    for i in community:
        aux = re.split(r'[# .:-]',i)
        try:
            sid.append(aux[len(aux) - 3])
            if aux[0] == "alert":
                protocol.append(returnNumber(aux[1]))
                num.append(aux[7])
            else:
                protocol.append(returnNumber(aux[3]))
                num.append(aux[9])
        except IndexError:
            continue
    msg = []        
    for i in sid_msg:
        aux = re.split(r'[||]',i)
        msg.append(aux[0])
        msg.append(aux[2])

    t1p2a = open("T1p2.txt", "w")        
    for i,j,k in zip(protocol[16:],num[16:],sid[16:]):
        t1p2a.write(i + "," + j + "," + returnSid(k.replace(";", ''),msg)+ "\n")

    t1p2a.close()
    community.close()
    sid_msg.close()

if __name__ == "__main__":
    main()