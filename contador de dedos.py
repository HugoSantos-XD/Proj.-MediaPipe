#-------------BIBLIOTECAS----------------------------------------------------------------

import cv2 #importando bibliotecas 
import mediapipe as mp 

video = cv2.VideoCapture('1')

hand = mp.solutions.hands
Hand = hand.Hands(max_num_hands = 1) #detecta a mão dentro do video 
mpDraw = mp.solutions.drawing_utils #desenha as linhas e os pontos na mão

while True: #rodando a webcam 
    check, img = video.read() #abrindo a webcam
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)#convertendo a imagem
    results = Hand.process(imgRGB) #processando a imagem

    cv2.imshow('WEB CAM',img)
    cv2.waitKey(1)


