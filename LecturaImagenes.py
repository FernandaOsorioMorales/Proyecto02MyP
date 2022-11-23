from PIL import Image
from math import sqrt
import numpy as np
import cv2
import imutils

class LecturaImagenes():
    '''
    Clase implementada para la lectura y procesamiento de la imagen usando la libreria opencv
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

def escaneoDeColores(imagen):
    '''
    Funcion que escanea los colores de la imagen y los guarda en un diccionario.
    :param imagen: imagen a la que se le desea escanear los colores.
    :return: diccionario con los colores de la imagen.
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

def transformacion_imagen_opencv(imagen_path,):
    '''
    Funcion que transforma la imagen a una imagen que pueda ser leida por opencv.
    :param imagen_path: path de la imagen a transformar.
    :return: imagen transformada.
    '''
    imagen = cv2.imread(imagen_path)
    cv2.imshow("gris", imagen)
    cv2.waitKey(delay = 5000)
    return imagen

def encuentra_contorno(imagen):
    '''
    Funcion que encuentra los contornos de la imagen.
    :param imagen: imagen a la que se le desea encontrar los contornos.
    :return: contornos encontrados.
    '''
    #kernel = np.ones((5,5),np.float32)/25
    #imagen_blur = cv2.filter2D(imagen, -1, kernel)
    # imagen_blur = cv2.bilateralFilter(imagen,9,75,75)
    # imagen_blur = cv2.GaussianBlur(imagen,(10,10),0)
    imagen_blur = cv2.blur(imagen, (5,5),cv2.BORDER_CONSTANT)
    canny = cv2.Canny(imagen,0,50)
    #threshold = cv2.threshold(imagen,255,255,cv2.THRESH_BINARY)[1]
    contornos,_ = cv2.findContours(canny,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    return contornos

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
        centro_x = 0
        centro_y = 0
        for par in contorno:
            centro_x+= par[0][0]
            centro_y+= par[0][1]
        centro_x/=len(contorno)
        centro_y/=len(contorno)
        coordenada = (centro_x,centro_y)
        pixel = imagen_control.getpixel(coordenada)
        rgb = ""
        for elemento in pixel:
            rgb+=str(elemento)+","
        rgb = rgb.rstrip(rgb[-1])
        distancias_contorno = []
        if(rgb == "255,255,255"):
            vertices_local = 0
            print("ENCONTRADO!")
            for elemento in contorno:
                contorno_x = elemento[0][0]
                contorno_y = elemento[0][1]
                distancia = sqrt(((centro_x-contorno_x)*(centro_x-contorno_x))+((centro_y-contorno_y)*(centro_y-contorno_y)))
                distancias_contorno.append(distancia)
            for i in range(2,len(distancias_contorno)):
                if distancias_contorno[i-2]<distancias_contorno[i-1] and distancias_contorno[i]<distancias_contorno[i-1]:
                    vertices_local+=1
            vertices = vertices_local
    return vertices

#/home/anshar/modelado/proyecto2/Proyecto02MyP/ImagenesEjemplos/example_1.bmp



