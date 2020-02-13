#!usr/bin/env python
#_*_ coding _*_

try:
    while True:
        print("l")
except NameError:
    print("La variable no existe")
except KeyboardInterrupt:
    print("Salida forzosa")
finally:
    print("Siempre se ejecuta")

try:
    # Genera el error
    raise IOError
except IOError:
    print("Probando los errores")