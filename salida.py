from entrada import x, y, lados #importa el numero de lados y las listas x y y
from calculos import rel #importa el area del modulo calculos

vertices = []

def pares():
    """Genera una lista con los puntos del poligono y lo imprime en pantalla """
    for i in range(lados[0]):
        vertices.append((x[i],y[i]))
    print(f"Vertices: {vertices}");


def areaPoligono():
    """ Imprime el area del poligono """
    print(f"El area del poligono es: {rel[0]} u^2")

