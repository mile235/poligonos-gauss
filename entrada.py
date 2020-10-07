#funcion entrada

lados= []
x=[]
y=[]

def entrada():
    """Pide los datos y los almacena en listas"""

    #n lados
    n =  int(input('Ingrese los lados del poligono: '))
    lados.append(n)

    for i in range(n):
        coordenada_x=int(input(f"Ingrese el valor de la coordenada x{i+1}:"))
        coordenada_y=int(input(f"Ingrese el valor de la coordenada y{i+1}:"))
        x.append(coordenada_x)
        y.append(coordenada_y)


