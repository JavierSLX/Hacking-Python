#!/usr/bin/env python
#_*_ coding: utf8 _*_

# diccionario
diccionario = dict(nombre = "alumno", plataforma = "Udemy", edad = 18)
print(diccionario)
print(diccionario['nombre'])
print(diccionario.viewkeys())

# Recorriendo un diccionario con las llaves
for i in range(0, len(diccionario)):
    keys = diccionario.keys()
    print(diccionario[keys[i]])

for i in diccionario.keys():
    print(diccionario[i])

# Lo convierte en una lista de tuplas
a = diccionario.items()
print(a)

# Obtiene solo los valores del diccionario
values = diccionario.values()
print(values)