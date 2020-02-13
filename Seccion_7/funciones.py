#!/usr/bin/env python
#_*_ coding: utf8 _*_

# __name__ 
# main()

# Funciones
def saludo(nombre):
    print("Bienvenido {}".format(nombre))

def main():
    # indica que temporalmente no tiene nada
    #pass
    nombre = raw_input("Nombre: ")
    saludo(nombre) 

# Manda llamar la funcion main
if __name__ == '__main__':
    main()