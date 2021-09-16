#Este programa fue creado con la documentación obtenida de la pagina geeksforgeeks https://www.geeksforgeeks.org/python-opencv-capture-video-from-camera/ creado por KaranGupta5
#Asi mismo se siguio el código creado en el video Color Filtering - OpenCV with Python for Image and Video Analysis 7 por el usuario sentdex https://www.youtube.com/watch?v=CCOXg75HkvM
#Es importante tener instalado el paquete opencv-python para poder correr el programa
#Fernando Cerriteño Magaña A01702790

#Este programa utiliza la camara para poder generar una mascara, la cual filtre todos los objetos que sean de color rojo, para poder generar una capa final, 
#la cual muestre video de lo que la camara esta viendo en rojo. El color que se filtra se puede cambiar desde la variable lower_red, la cual indica el color 
#en HSV que se va a filtrar.

import numpy as np
import cv2

#Se crea la variable cap con cv2 para capturar frame por frame
cap=cv2.VideoCapture(0)

#Se crea un while infinito para poder mostrar el frame constantemente
while (True):
    ret,frame = cap.read()
    hav = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #HSV = hue sat value
    lower_red = np.array([150,100,50])
    uper_red = np.array([255,255,255])
    
    #Se crea una mascara para filtrar el color
    mask = cv2.inRange(hav, lower_red,uper_red)
    #Se crea el resultado del filtro
    res = cv2.bitwise_and(frame, frame, mask = mask)

    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #Se muestra el resultado del visor original, la mascara y el resultado final
    cv2.imshow('Visor',frame)
    cv2.imshow('Mask',mask)
    cv2.imshow('Result',res)

    #Se crea un condicional para finalizar el bucle infinito al presionar "q"
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
