"""
DELIMITACION DE PUNTOS

Este código tiene la finalidad de implementar un 'tracker' para delimitar los puntos que conformarán la zona que se va a eliminar de los frames a estudiar. Como la zona a eliminar es fija, es posible crear una función que permita que realizar esta operación para el dataset de estudio.

Se pensaba en utilizar un Notebook perteneciente a Jupyter Notebook, pero debido a que el ambiente de trabajo no es compartible con Interfaces Gráficas, no fue posible implementarlo por el momento

"""

# AMBIENTE DE TRABAJO
import numpy as np
import cv2

"""
DEFINICION DE LA FUNCION

La función tendrá como objetivo obtener las coordenadas que se requierar para delimitar la zona que posee la base fija, además de la zona inferior de este elemento, pues produce un ruido innecesario. El evento del click izquierdo sobre la imagen a estudiar, nos permitirá visualizar las coordenadas.

"""

def click_event(event, x, y, flags, param):

#Creación del evento

    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,', ' ,y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        strXY = str(x) + ', '+ str(y)


        cv2.putText(img, strXY, (x, y), font, .5, (255, 255, 0), 2)
        cv2.imshow('image', img)

#Abrir el fichero a analizar
fichero = '.\Dataset 1 - Filamentos\0030.jpg'
img = cv2.imread(fichero)

#Abrir la interfaz
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.resizeWindow('image', (500, 500))
cv2.imshow('image', img)

#Llamar a la función
cv2.setMouseCallback('image', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()