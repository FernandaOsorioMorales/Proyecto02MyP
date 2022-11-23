class Colores:
    '''
    Clase implementada para el escaneo de colores dentro de nuestra imagen.
    '''


def escaneoDeColores(imagen):
    '''
    Funcion que encuentra los colores presentes en la imagen (correspondientes a las figuras) y el color del fondo.
    :param imagen: imagen a la que se le desea encontrar sus colores.
    :return: colores de las figuras y el color de fondo.
    '''
    colores = set()
    fondo = ""
    for x in range(imagen.width):
        for y in range(imagen.height):
            coordenada = x,y
            pixel = imagen.getpixel(coordenada);
            rgb = ""
            for elemento in pixel:
                rgb+=str(elemento)+","
            rgb = rgb.rstrip(rgb[-1])
            if (x==0 and y==0):
                fondo = rgb
            elif(rgb!=fondo):
                colores.add(rgb)
    return colores, fondo

def hexadecimal(numero):
    '''
    Funcion que convierte el valor en RGB a hexadecimal.
    :param numero: valor del color en RGB.
    :return: valor del color en hexadecimal.
    '''
    decimal = numero.split(",")
    hexa = ""
    for elemento in decimal:
        num = int(elemento)
        num = hex(num)
        num = num[2:]
        hexa+=num
    ans = hexa.upper()
    return ans