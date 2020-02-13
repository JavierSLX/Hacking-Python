#!/usr/bin/env python
#_*_ coding: utf8 _*_

import time

def suma(n, m):
    return n + m

def resta(n, m):
    return n - m

def multiplicacion(n, m):
    return n * m

def division(n, m):
    return n / m

def main():
    while True:
        print("Bienvenido\n")
        print("1.- Suma")
        print("2.- Resta")
        print("3.- Multiplicacion")
        print("4.- Division")
        print("5.- Salir")
        
        opcion = int(raw_input("Opcion: "))

        if opcion > 4:
            print("Adios!")
            break
        else:
            n = int(raw_input("Numero 1: "))
            m = int(raw_input("Numero 2: "))
            if opcion == 1:
                print("El resultado es {}".format(suma(n, m)))
            elif opcion == 2:
                print("El resultado es {}".format(resta(n, m)))
            elif opcion == 3:
                print("El resultado es {}".format(multiplicacion(n, m)))
            else:
                print("El resultado es {}".format(division(n, m)))

            time.sleep(2)

if __name__ == '__main__':
    main()