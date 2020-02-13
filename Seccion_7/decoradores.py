#!/usr/bin/env python
#_*_ coding: utf8 _*_

# classmethod
# staticmethod
# property

class Prueba(object):

    def __init__(self, radio):
        self.radio = radio

    # Decorador que permite llamar el método sin que la clase sea instanciada (Igual a static en Java)
    @classmethod
    def saludo(cls, nombre):
        print("Hola {}".format(nombre))

    # Permite usar el metodo sin necesidad de argumentos (sin poner self)
    @staticmethod
    def saludo_static():
        print("Bienvenido")

    # Decorador que permite trabajar con metodos como si fueran variables
    @property
    def area_circulo(self):
        return 3.141592 * (self.radio ** 2)

def main():
    Prueba.saludo("Javier")

    prueba = Prueba(5)
    prueba.saludo_static()

    # Se usa como si fuera una variable sin parentesis
    area = prueba.area_circulo
    print(area)

if __name__ == '__main__':
    main()