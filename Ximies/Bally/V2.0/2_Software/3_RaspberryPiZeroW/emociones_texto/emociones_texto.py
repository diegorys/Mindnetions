#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import sys

'''
- Proyecto: Bally 2.0
- Nombre del desarrollador: Diego de los Reyes Rodríguez (diegorys)
- Para: Xpikuos
- Version: 20.07.12.16.15.00
- Descripción: Analiza un texto y busca emociones en él.
- Licencia: Este trabajo está licenciado bajo la licencia de Atribución-NoComercialCompartirIgual 4.0 Internacional (CC BY-NC-SA 4.0)
    Para ver una copia de esta licencia, visita
    https://creativecommons.org/licenses/by-nc-sa/4.0/deed.es
'''


class EmocionesTexto():

    def actuar(self, texto):
        print('Buscando emociones en: ' + texto)


if __name__ == "__main__":
    emocionesTexto = EmocionesTexto()
    emocionesTexto.actuar(sys.argv[1])
