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
    permissions_apk = {}
    for filename in glob.glob(os.path.join(path, '*.xml')):

        manifest = open(filename, 'rt')
        root = ET.parse(manifest).getroot()

        permissions_apk[filename] = set()
        
        tags = []
        for elem in root.iter('uses-permission'):
            tags.append(elem.attrib)

        permissions = []
        for i in tags:
            aux = re.split(r'[.\'}]',str(i))
            permissions.append(aux[-3:-2])
        for i in permissions:
            permissions_apk[filename].add(re.split(r'[\[\]]',str(i))[1])


    for k,i in permissions_apk.items():
        print(k + ': ' +  str(list(i)).replace("\"", "") + '\n\n')

if __name__ == "__main__":
    main()