import xml.etree.ElementTree as ET
import re
import os
import sys
import glob 

def main():
    path = sys.argv[1]

    print("===================\n")
    print("Permissões por APK\n")
    print("===================\n\n")
    for filename in glob.glob(os.path.join(path, '*.xml')):

        manifest = open(filename, 'rt')
        root = ET.parse(manifest).getroot()

        tags = []
        for elem in root.iter('uses-permission'):
            tags.append(elem.attrib)

        print(filename.split("/")[1] + ": ", end='')
        permissions = []
        for i in tags:
            aux = re.split(r'[.\'}]',str(i))
            permissions.append(aux[-3:-2])
        print("[", end='')
        for i in permissions:
            if(i == permissions[len(permissions)-1]):
                print(re.split(r'[\[\]]',str(i))[1]+ "]")
            else:
                print(re.split(r'[\[\]]',str(i))[1] + ", ", end='')
        print()

if __name__ == "__main__":
    main()