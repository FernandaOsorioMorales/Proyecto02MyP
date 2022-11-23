import LecturaImagenes
import colores
from PIL import Image


if __name__ == '__main__':
    '''
    Funcion principal del programa con la cual implementamos la lectura de la imagen y el procesamiento de la misma.
    '''
    imagen_fuente = LecturaImagenes.solicitarImagenYPasarlaAMatriz()
    colores_fuente, fondo_fuente = colores.escaneoDeColores(imagen_fuente)
    colores_fuente = list(colores_fuente)
    for color in colores_fuente:
        figura_aislada = LecturaImagenes.aislarFigura(color, fondo_fuente, imagen_fuente)
        #figura_aislada.show()
        figura_aislada.save(f"{color}.jpg")
        figura_aisladaBN = LecturaImagenes.transformacion_imagen_opencv(f"{color}.jpg")
        figura_aislada_grande = LecturaImagenes.agrandar(figura_aisladaBN)
        figuraContorneada = LecturaImagenes.encuentra_contorno(figura_aislada_grande)
        imagen_control = Image.fromarray(figura_aislada_grande)
        vertices_figura = LecturaImagenes.obtener_vertices(figuraContorneada, imagen_control, color)
        hex_color = colores.hexadecimal(color)
        figura_final = LecturaImagenes.tipo_de_figura(vertices_figura)
        print(f"{hex_color} = {figura_final}")
        
        


        
        

