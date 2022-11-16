from PIL import Image
import numpy as np

def solicitarImagenYPasarlaAMatriz():
    print("Bienvenido a nuestro programa de detección de figuras dentro de una imagen, inserte el path de su imagen incluyendo su nombre y la terminación correspondiente al tipo")
    PathImagen = input()#recibimos el path
    imagenGuardada = Image.open(PathImagen)
    arregloDeImagen = np.array(imagenGuardada)
    print(arregloDeImagen)








