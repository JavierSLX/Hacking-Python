#!user/bin/env python
#_*_ coding: utf8 _*_

# Hay que instalar pip y agregarlo al PATH para descargar paquetes

import requests
import argparse

# Define argumentos para uso en consola
parser = argparse.ArgumentParser(description="Detector de cabeceras")
parser.add_argument('-t', '--target', help="Objetivo")
parser = parser.parse_args()

def main():
    # Evalua si el target no está nulo
    if parser.target:
        try:
            url = requests.get(url=parser.target)

            # Convierte la cabecera a forma de diccionario
            cabeceras = dict(url.headers)
            for key in cabeceras:
                print(key + " : " + cabeceras[key])
        except:
            print("No me pude conectar")
    else:
        print("No hay objetivo")

if __name__ == "__main__":
    main()