"""
TRACKER UMBRALES

Este archivo tiene como finalidad explorar los valores requeridos para la umbralización por medio del espacio HSV (Hue, Saturation, Value). Los valores van a ser adquiridos por medio de un tracker, el cual nos permitirá ir variando tanto los valores del umbral bajo como del umbral alto para así poder determinar la estimación de resultados que sea la más acorde a la segmentación de la silueta del filamento.
"""

#AMBIENTE DE TRABAJO
import cv2
import numpy as np

"""
DEFINICION DE LA FUNCIÓN

La función recibe como único parámetro el nombre del fichero, y una vez activada se generará una GUI con la cual el usuario podrá ir variando tanto los valores del umbral bajo como del umbral alto para poder determinar que valores son los adecuados para la correcta segmentación del filamento.
"""

def tracker(filename):
    if isinstance(filename, str):
        file_name = cv2.imread(filename)
    else:
        file_name = filename

    def Null_Value(x):
        return None

    #Se crea la ventana	
    cv2.namedWindow("Trackbars")
    
    #Se crea el tracker
    cv2.createTrackbar("L - H", "Trackbars", 0, 179, Null_Value)
    cv2.createTrackbar("L - S", "Trackbars", 0, 255, Null_Value)
    cv2.createTrackbar("L - V", "Trackbars", 0, 255, Null_Value)
    cv2.createTrackbar("U - H", "Trackbars", 179, 179, Null_Value)
    cv2.createTrackbar("U - S", "Trackbars", 255, 255, Null_Value)
    cv2.createTrackbar("U - V", "Trackbars", 255, 255, Null_Value)
    
    #Se generan las barras de interacción
    while True:
	"""
	Como paso previo a la umbralización se realiza un filtro de la mediana con un 
        kernel de tamaño 11x11
	"""
	img = cv2.medianBlur(file_name, 11, 0)
	
	#Se configuran los trackers
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        l_h = cv2.getTrackbarPos("L - H", "Trackbars")
        l_s = cv2.getTrackbarPos("L - S", "Trackbars")
        l_v = cv2.getTrackbarPos("L - V", "Trackbars")
        u_h = cv2.getTrackbarPos("U - H", "Trackbars")
        u_s = cv2.getTrackbarPos("U - S", "Trackbars")
        u_v = cv2.getTrackbarPos("U - V", "Trackbars")

        lower = np.array([l_h, l_s, l_v])
        upper = np.array([u_h, u_s, u_v])
	
	#Guardan los resultados para su posterior visualización
        mask = cv2.inRange(hsv, lower, upper)
        result = cv2.bitwise_and(file_name, file_name, mask=mask)
	
	#Se realiza un resize de las ventanas debido al tamaño de la imagen a analizar
        cv2.namedWindow('frame', cv2.WINDOW_NORMAL)
        cv2.resizeWindow('frame', (500, 500))
        cv2.namedWindow('mask', cv2.WINDOW_NORMAL)
        cv2.resizeWindow('mask', (500, 500))
        cv2.namedWindow('result', cv2.WINDOW_NORMAL)
        cv2.resizeWindow('result', (500, 500))
        
	#Se visualizan los resultados
	cv2.imshow("frame", file_name)
        cv2.imshow("mask", mask)
        cv2.imshow("result", result)
        
	#Cierre del ciclo while
	key = cv2.waitKey(1)
        if key == 27:
            lower_hue = l_h
            lower_sat = l_s
            lower_val = l_v
            upper_hue = u_h
            upper_sat = u_s
            upper_val = u_v
            break
    
    #Retorna los valores de los umbrales
    cv2.destroyAllWindows()
    return lower_hue, lower_sat, lower_val, upper_hue, upper_sat, upper_val

"""
El fichero a abrir deberá ser parte de la carpeta Dataset 5 y Dataset 7 para su posterior analisis
"""
fichero = '.\Dataset 2 - Filamentos\0030.jpg'
tracker(fichero)