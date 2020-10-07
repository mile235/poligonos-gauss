#importa numero de lados y las listas x y y
from entrada import lados, x, y 

rel = []

def areaPoligono():
    """Calcula el area del poligono"""

    n = lados[0]

    x.append(x[0])
    y.append(y[0])
    suma = 0
    suma2 = 0

    for i in range(n):

        suma = suma +  x[i]*y[i+1]
        suma2 = suma2 + y[i]*x[i+1]

    Area = (1/2)*abs(suma-(suma2))
    rel.append(Area)
