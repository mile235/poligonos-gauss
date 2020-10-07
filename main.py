from entrada import entrada
import calculos
from salida import pares, areaPoligono

entrada()
""" Pide el numero de lados del poligono e itera 
el numero de lados para pedir las coordenadas en x y y"""

calculos.areaPoligono()
"""Calcula el area del poligono, adiciona a las listas x y y el x1 y y1
    genera la suma con x y con y para despues restar estas y multiplicarlas por 1/2
    retornando el resultado"""

areaPoligono()
""" Imprime el resultado de la funcion anterior """

pares()
""" Genera una lista con los pares ordenados del poligono """
