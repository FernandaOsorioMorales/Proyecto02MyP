import LecturaImagenes
import ImagenesEjemplos
from PIL import ImageShow
if __name__ == '__main__':
    imagen_fuente = LecturaImagenes.solicitarImagenYPasarlaAMatriz()
    colores_fuente, fondo_fuente = LecturaImagenes.escaneoDeColores(imagen_fuente)
    colores_fuente = list(colores_fuente)
    imagenes = []
    for color in colores_fuente:
        print(color)
        figura_aislada = LecturaImagenes.aislarFigura(color, fondo_fuente, imagen_fuente)
        

