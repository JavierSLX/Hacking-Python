#!/usr/bin/env python
#_*_ coding: utf8 _*_

# Clase Carro
class Carro(object):

    # Constructor
    def __init__(self, velocidad):
        self.color = "Rojo"
        self.puertas = 4
        self.tipo = "Deportivo"
        self.velocidad = velocidad

    # Metodo
    def movilidad(self):
        if self.velocidad > 200:
            print("Carro de lujo")
        else:
            print("Carro normal")

def main():
    carro = Carro(150)
    print(carro.color)
    print(carro.puertas)
    print(carro.tipo)

    carro.movilidad()

if __name__ == '__main__':
    main()