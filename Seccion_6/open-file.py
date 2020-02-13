#!/usr/bin/env python
#_*_ coding: utf8 _*_

# Abre el archivo en modo de escritura
archivo = open("archivo.txt", "w")
nombre = raw_input("Nombre: ")
edad = raw_input("Edad: ")
pais = raw_input("Pais: ")

archivo.write(nombre)
archivo.write(edad)
archivo.write(pais)

print("He escrito los datos")
archivo.close()