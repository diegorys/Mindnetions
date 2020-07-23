#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from classifier import SentimentClassifier

'''
- Proyecto: Bally 2.0
- Nombre del desarrollador: Diego de los Reyes Rodríguez (diegorys)
- Para: Xpikuos
- Version: 20.07.20.18.36.00
- Descripción: Analiza un texto en español y comprueba si el sentimiento que genera es positivo o negativo.
El resultado es un número decimal entre 0 y 1.
    Cuanto más cercano a 0, más negativo.
    Cuanto más cercano a 1, más positivo.
    Cuanto más cercano a 0.5, más neutro.
Para instalarlo, previamente hay que instalar las siguientes dependencias:
    sudo pip3 install spanish_sentiment_analysis
Puedes probarlo con:
python3 emociones_texto.py "Texto a probar"
- Licencia: Este trabajo está licenciado bajo la licencia de Atribución-NoComercialCompartirIgual 4.0 Internacional (CC BY-NC-SA 4.0)
    Para ver una copia de esta licencia, visita
    https://creativecommons.org/licenses/by-nc-sa/4.0/deed.es
'''


class EmocionesTexto():

    def __init__(self):
        self.clf = SentimentClassifier()

    def actuar(self, text):
        print(text)
        sentimiento = self.clf.predict(text)
        print(sentimiento)


if __name__ == "__main__":
    emocionesTexto = EmocionesTexto()
    emocionesTexto.actuar(sys.argv[1])
