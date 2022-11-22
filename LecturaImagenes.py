from PIL import Image
from math import sqrt
import numpy as np
import cv2
import imutils

def solicitarImagenYPasarlaAMatriz():
    print("Bienvenido a nuestro programa de detección de figuras dentro de una imagen")
    print("Inserte el path de su imagen incluyendo su nombre y la terminación correspondiente al tipo")
    PathImagen = input()#recibimos el path
    imagenGuardada = Image.open(PathImagen)
    return imagenGuardada

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

def aislarFigura(color_figura, color_fondo, imagen):
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
    return imagen_auxiliar

def escalas_de_grises(imagen_path):
    imagen = cv2.imread(imagen_path)
    grises = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    # cv2.imshow("gris", grises)
    # cv2.waitKey(delay = 5000)
    return grises

def encuentra_contorno(imagen):
    canny = cv2.Canny(imagen,0,50)
    #threshold = cv2.threshold(imagen,255,255,cv2.THRESH_BINARY)[1]
    contornos,_ = cv2.findContours(canny,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    return contornos

def obtener_vertices(contornos, imagen_control, color_figura):
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
        vertices = 0
        distancias_contorno = []
        if(color_figura == rgb):
            vertices_local = 0
            print("ENCONTRADO!")
            for elemento in contorno:
                contorno_x = elemento[0][0]
                contorno_y = elemento[0][1]
                distancia = sqrt(pow(centro_x-contorno_x,2)+pow(centro_y-contorno_y,2))
                distancias_contorno.append(distancia)
            for i in range(2,len(distancias_contorno)):
                if distancias_contorno[i-2]<distancias_contorno[i-1] and distancias_contorno[i]<distancias_contorno[i-1]:
                    vertices_local+=1
            vertices = max(vertices,vertices_local)
    return vertices

#/home/anshar/modelado/proyecto2/Proyecto02MyP/ImagenesEjemplos/example_1.bmp



