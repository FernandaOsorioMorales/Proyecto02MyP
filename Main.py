import LecturaImagenes
import ImagenesEjemplos
from PIL import ImageShow
from numpy import asarray 
import cv2


if __name__ == '__main__':
    imagen_fuente = LecturaImagenes.solicitarImagenYPasarlaAMatriz()
    colores_fuente, fondo_fuente = LecturaImagenes.escaneoDeColores(imagen_fuente)
    colores_fuente = list(colores_fuente)
    imagenes = []
    
    for color in colores_fuente:
        print(color)
        figura_aislada = LecturaImagenes.aislarFigura(color, fondo_fuente, imagen_fuente)
        figura_aislada.show()
        figuraAisladaMatriz = asarray(figura_aislada)
        figura_aisladaBN = LecturaImagenes.escalas_de_grises(figuraAisladaMatriz)
        figuraParaContornear = figura_aisladaBN.copy()
        figuraContorneada = LecturaImagenes.encuentra_contorno(figuraParaContornear)
        print(figuraContorneada)


        
        

