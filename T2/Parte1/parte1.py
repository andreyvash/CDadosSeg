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
        print(k[26:-4] + ': ' +  str(list(i)).replace("\"", "") + '\n\n')

    print("===================\n")
    print("Permissões únicas por APK\n")
    print("===================\n\n")
    repeated_permissions = set()
    for k, v in permissions_apk.items():
        unique_permission = v.copy()
        for ki, vi in permissions_apk.items():
            if k == ki:
                continue
            unique_permission -= v & vi

        repeated_permissions.update(v - unique_permission)
        print(k[26:-4] + str(': ') + str(list(unique_permission)).replace("\"", "") + '\n\n')
        
    print("===================\n")
    print("Permissões comuns das APKs\n")
    print("===================\n\n")
    print(str(list(repeated_permissions)).replace("\"", ""))

if __name__ == "__main__":
    main()