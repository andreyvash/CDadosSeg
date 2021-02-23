import re
import sys
from collections import OrderedDict

def main():
    av1 = open(sys.argv[1], 'rt')
    saida = []
    #Adiciona o tipo e a familia numa lista
    for i in av1:
        aux = re.split(r'[.:-]',i)
        saida.append(aux[3] +","+ aux[4])

    saida = sorted(saida)

    #remove os repetidos
    saidaSet = list(OrderedDict.fromkeys(saida))
    t1p1a = open("T1p1a.txt", "w")
    
    #Adiciona no arquivo de saida o tipo e familia e a quantidade que eles aparecem no arquivo de entrada
    for i in saidaSet:
        t1p1a.write(i+","+ str(saida.count(i))+"\n")

    t1p1a.close()
    av1.close()

if __name__ == "__main__":
    main()