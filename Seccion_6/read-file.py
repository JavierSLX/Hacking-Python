#!/usr/bin/env python
#_*_ coding: utf8 _*_

archivo = open('wordlist.lst', 'r')
#print(archivo.readlines())

#for line in archivo.read().split("\n"):
#    print(line)

lista = archivo.read().split('\n')
print(len(lista))