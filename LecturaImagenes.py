from PIL import Image
from math import sqrt
import cv2

class LecturaImagenes():
    '''
    Clase implementada para la lectura y procesamiento de la imagen.
    '''

def solicitarImagenYPasarlaAMatriz():
    '''
    Funcion que solicita la ruta de la imagen y la pasa a una matriz.
    :return: matriz con la imagen.
    '''
    print("Bienvenido a nuestro programa de detección de figuras dentro de una imagen")
    print("Inserte el path de su imagen incluyendo su nombre y la terminación correspondiente al tipo")
    PathImagen = input()#recibimos el path
    imagenGuardada = Image.open(PathImagen)
    return imagenGuardada
    
def aislarFigura(color_figura, color_fondo, imagen):
    '''
    Funcion que aisla la figura de la imagen, para asi obtener las diferentes figuras que se encuentren en ella.
    :param color_figura: color de la figura que se desea aislar.
    :param color_fondo: color del fondo de la imagen.
    :param imagen: imagen a la que se le desea aislar la figura.
    :return: imagen con la figura aislada.
    '''
    imagen_auxiliar = imagen.copy()
    color_fondo_original = tuple(color_fondo.split(","))
    color_figura_original = tuple(color_figura.split(","))
    for x in range(imagen_auxiliar.width):
        for y in range(imagen_auxiliar.height):
            coordenada = (x,y)
            pixel = imagen_auxiliar.getpixel(coordenada)
            rgb = ""
            for elemento in pixel:
                rgb+=str(elemento)+","
            rgb = rgb.rstrip(rgb[-1])
            if(rgb !=color_figura):
                imagen_auxiliar.putpixel(coordenada, (int(color_fondo_original[0]), int(color_fondo_original[1]), int(color_fondo_original[2])))
    for x in range(imagen_auxiliar.width):
        for y in range(imagen_auxiliar.height):
            coordenada = (x,y)
            pixel = imagen_auxiliar.getpixel(coordenada)
            rgb = ""
            for elemento in pixel:
                rgb+=str(elemento)+","
            rgb = rgb.rstrip(rgb[-1])
            if(rgb !=color_figura):
                imagen_auxiliar.putpixel(coordenada, (0, 0, 0))
            else:
                imagen_auxiliar.putpixel(coordenada,(255,255,255))
    return imagen_auxiliar

def transformacion_imagen_opencv(imagen_path):
    '''
    Funcion que transforma la imagen a una imagen que pueda ser leida por opencv.
    :param imagen_path: path de la imagen a transformar.
    :return: imagen transformada.
    '''
    imagen = cv2.imread(imagen_path)
    return imagen

def encuentra_contorno(imagen):
    '''
    Funcion que encuentra los contornos de la imagen.
    :param imagen: imagen a la que se le desea encontrar los contornos.
    :return: contornos encontrados.
    '''
    imagen_blur = cv2.bilateralFilter(imagen,9,75,75)
    canny = cv2.Canny(imagen_blur, 800 , 1000)
    contornos,_ = cv2.findContours(canny,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    return contornos

def agrandar(imagen):
    '''
    Funcion que aumenta el tamaño de nuestra imagen.
    :param imagen: imagen a la que se le desea aumentar el tamaño.
    :return: imagen con el nuevo tamaño.
    '''
    porcentaje_de_escala = 500
    ancho = int(imagen.shape[1] * porcentaje_de_escala / 100)
    largo = int(imagen.shape[0] * porcentaje_de_escala / 100)
    dimension = (ancho, largo)
    imagen_grande = cv2.resize(imagen, dimension, interpolation = cv2.INTER_AREA)
    return imagen_grande

def obtener_vertices(contornos, imagen_control, color_figura):
    '''
    Funcion que obtiene los vertices de la figura usando la implemetnacion de opencv para obtener los contornos.
    :param contornos: contornos de la figura.
    :param imagen_control: imagen de control.
    :param color_figura: color de la figura.
    :return: vertices de la figura.
    '''
    vertices = 0
    for contorno in contornos:
        M = cv2.moments(contorno)
        if M['m00']!=0:
            centro_x = int(M['m10']/M['m00'])
            centro_y = int(M['m01']/M['m00'])
            coordenada = (centro_x,centro_y)
            pixel = imagen_control.getpixel(coordenada)
            rgb = ""
            for elemento in pixel:
                rgb+=str(elemento)+","
            rgb = rgb.rstrip(rgb[-1])
            distancias_contorno = []
            if(rgb == "255,255,255"):
                vertices_local = 0
                for elemento in contorno:
                    contorno_x = elemento[0][0]
                    contorno_y = elemento[0][1]
                    distancia = sqrt(((centro_x-contorno_x)*(centro_x-contorno_x))+((centro_y-contorno_y)*(centro_y-contorno_y)))
                    distancias_contorno.append(distancia)
                vertices = set() 
                for i in range(120,len(distancias_contorno)*2):
                    i = i%len(distancias_contorno)
                    flag = False
                    for j in range(0,120):
                        j = j%len(distancias_contorno)
                        if distancias_contorno[i-j]>distancias_contorno[i-60]:
                            flag = True
                    for j in range(120,60,-1):
                        j = j%len(distancias_contorno)
                        if distancias_contorno[i-j]>distancias_contorno[i-60]:
                            flag = True
                    if flag == False and not(i-60 in vertices):
                        vertices_local+=1
                        vertices.add(i-60)
                vertices = vertices_local
    return vertices

def tipo_de_figura(vertices):
    '''
    Funcion que clasifica el tipo de figura al que pertenecen de acuerdo a su número de vértices.
    :param vertices: numero de vertices encontrados en cada figura .
    :return: tipo de figura de la que estamos trabajando.
    '''
    figura = "X"
    if(vertices == 0 or vertices >= 7):
        figura = "O"
    elif vertices == 3:
        figura = "T"
    elif vertices == 4:
        figura = "C"
    return figura




