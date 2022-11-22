import LecturaImagenes
import ImagenesEjemplos
from PIL import ImageShow
from numpy import asarray 
import cv2


if __name__ == '__main__':
    imagen_fuente = LecturaImagenes.solicitarImagenYPasarlaAMatriz()
    colores_fuente, fondo_fuente = LecturaImagenes.escaneoDeColores(imagen_fuente)
    colores_fuente = list(colores_fuente)
    for color in colores_fuente:
        figura_aislada = LecturaImagenes.aislarFigura(color, fondo_fuente, imagen_fuente)
        #figura_aislada.show()
        figura_aislada.save(f"{color}.jpg")
        figura_aisladaBN = LecturaImagenes.escalas_de_grises(f"{color}.jpg")
        figuraContorneada = LecturaImagenes.encuentra_contorno(figura_aisladaBN)
        vertices_figura = LecturaImagenes.obtener_vertices(figuraContorneada, figura_aislada, color)
        print(color+" : "+str(vertices_figura))
        


        
        

