#!/usr/bin/env python
#_*_ coding: utf8 _*_

#if
#elif
#else

edad = int(raw_input("Digite su edad: "))

# Usando los condicionales
if edad < 18:
    print('Es menor de edad')
elif edad > 18 and edad < 95:
    print('Es mayor de edad')
else:
    print('Sigues vivo?')