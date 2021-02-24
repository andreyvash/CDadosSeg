import sys
import os
import pefile
import glob


def format_print(sections):
    for k, v in sections.items():
        if type(k) == str:
            print(k + ':')
        else:
            print(k.name + ':')
        for value in v:
            print('\t\t\t' + value)


def main():
    arg = sys.argv[1]
    print('Nome binário: \t\t[Seções executáveis]')
    if os.path.isdir(arg):
        for filename in glob.glob(os.path.join(arg, '*.exe')):
            pe = pefile.PE(filename)
            secaoExecutavel = dict()
            secaoExecutavel[filename] = []
            for secao in pe.sections:
                if secao.IMAGE_SCN_MEM_EXECUTE:
                    secaoExecutavel[filename].append(secao.Name.decode('utf-8').rstrip('\x00'))

            format_print(secaoExecutavel)
 
    elif os.path.isfile(arg):
        pe = pefile.PE(arg)
        secaoExecutavel = dict()
        secaoExecutavel[arg] = []
        for secao in pe.sections:
            if secao.IMAGE_SCN_MEM_EXECUTE:
                secaoExecutavel[arg].append(secao.Name.decode('utf-8').rstrip('\x00'))

        format_print(secaoExecutavel)


if __name__ == '__main__':
    main()
