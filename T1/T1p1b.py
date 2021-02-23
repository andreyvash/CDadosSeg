import re
import sys
def main():
    av2 = open(sys.argv[1], 'rt')
    win = []
    tool = []
    psy = []
    num = []
    for i in av2:
        aux = re.split(r'[.:-]',i)
        win.append(aux[1])
        tool.append(aux[2])
        psy.append(aux[3])
        num.append(aux[4])

    t1p1b = open("T1p1b.txt", "w")
    for i,j,k,l in zip(win, tool, psy, num):
        t1p1b.write(i + "," + j + "," + k + "," + l + "\n")

    av2.close()
    t1p1b.close()    

if __name__ == "__main__":
    main()