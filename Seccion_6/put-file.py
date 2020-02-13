#!/usr/bin/env python
#_*_ coding: utf8 _*_

archivo = open('archivo.txt', 'a')

dedicacion = raw_input("Dedicacion: ")
empresa = raw_input("Empresa: ")
idioma = raw_input("Idioma: ")

archivo.write(dedicacion)
archivo.write(empresa)
archivo.write(idioma)

archivo.close()