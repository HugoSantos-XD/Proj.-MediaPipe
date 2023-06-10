#-------------BIBLIOTECAS----------------------------------------------------------------
import cv2 #importando bibliotecas 
import mediapipe as mp
import math 
#--------------VARIAVÉIS------------------------------------------------------------------
video = cv2.VideoCapture('polichinelos.mp4') #pegando o video da pasta 
pose = mp.solutions.pose #rastreamento de pontos no video
Pose = pose.Pose(min_tracking_confidence= 0.5, min_detection_confidence= 0.5) #melhorando o rastreamento de pontos 
draw = mp.solutions.drawing_utils #variavel que irá desenhar as linhas no video
contador = 0
check = True
#------------PRINCIPAL--------------------------------------------------------------------
while True: #colocando para rodar o video no loop 
    sucess, img = video.read() 
    videoRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB) #modificando a cor do video
    results = Pose.process(videoRGB) #processando os pontos no video
    points = results.pose_landmarks  #extraindo os pontos dentro do video
    draw.draw_landmarks(img,points,pose.POSE_CONNECTIONS) #exibindo os pontos no video
    h, w, _ = img.shape #extraindo as dimensões da imagem

    if points: #extraindo todas as coordenadas
        peDY = int(points.landmark[pose.PoseLandmark.RIGHT_FOOT_INDEX].y*h)
        peDX = int(points.landmark[pose.PoseLandmark.RIGHT_FOOT_INDEX].x*w)

        peEY = int(points.landmark[pose.PoseLandmark.LEFT_FOOT_INDEX].y*h)
        peEX = int(points.landmark[pose.PoseLandmark.LEFT_FOOT_INDEX].x*w)
        
        maoDY = int(points.landmark[pose.PoseLandmark.RIGHT_INDEX].y*h)
        maoDX = int(points.landmark[pose.PoseLandmark.RIGHT_INDEX].x*w)

        maoEY = int(points.landmark[pose.PoseLandmark.LEFT_INDEX].y*h)
        maoEX = int(points.landmark[pose.PoseLandmark.LEFT_INDEX].x*w)

        distMAO = math.hypot(maoDX-maoEX, maoDY-maoEY)
        distPE = math.hypot(peDX-peEX, peDY-peEY)
        
        print(f'maos {distMAO} pes {distPE}')
        if check == True and distMAO <= 150 and distPE >=150: #quando temos um polichinelo 
            contador +=1
            check = False

        if distMAO >= 150 and distPE <=150: #não temos polichinelos
            contador +1
            check = True 
        print (contador)
        texto = f'QUANTIDADE {contador}'

        cv2.rectangle(img,(20,240),(400,120),(255,0,0),-1)
        cv2.putText(img,texto,(40,200),cv2.FONT_HERSHEY_SIMPLEX,1.5,(255,255,255),5) # mostrando o contador de polichinelos no video

    cv2.imshow('Resultado',img)#rodando o video
    cv2.waitKey(10) #delay do video


