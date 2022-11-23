
def escaneoDeColores(imagen):
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
    decimal = numero.split(",")
    hexa = ""
    for elemento in decimal:
        num = int(elemento)
        num = hex(num)
        num = num[2:]
        hexa+=num
    ans = hexa.upper()
    return ans