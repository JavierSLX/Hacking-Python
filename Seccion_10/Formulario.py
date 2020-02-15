#!user/bin/env python
#_*_ coding: utf8 _*_

import mechanize
import argparse
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser()
parser.add_argument("-b", "--buscar", help="Opcion a buscar")
parser = parser.parse_args()

def main():
    if parser.buscar:
        # Instancia un navegador
        navegador = mechanize.Browser()
        navegador.set_handle_robots(False)
        navegador.set_handle_equiv(False)
        navegador.addheaders = [('User-Agent', 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; de) Opera 8.0')]

        # Abre una página
        navegador.open("https://www.google.com")

        # Checa que formularios maneja Google
        #for n in navegador.forms():
        #    print(n)

        # Elije el formulario 0 y agrega texto a lo que hay que buscar
        navegador.select_form(nr=0)
        navegador['q'] = parser.buscar
        navegador.submit()

        # Muestra de manera legible la respuesta
        response = BeautifulSoup(navegador.response().read(), "html5lib")
        for link in response.find_all('a'):
            u = link.get('href')
            u = u.replace('/url?q=', '')
            print(u)
        
    else:
        print("Palabra a buscar")

if __name__ == "__main__":
    main()