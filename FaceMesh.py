import cv2 
import mediapipe as mp 
import time 
import math 
import pyautogui 
import os

width = int(1280/2)
height = int(720/2)
cam = cv2.VideoCapture(0)
pTime = 0

mpDraw = mp.solutions.drawing_utils 
mpFaceMesh =  mp.solutions.face_mesh
faceMesh =  mpFaceMesh.FaceMesh(max_num_faces=1)
drawSpace =  mpDraw.DrawingSpec(thickness=1 , circle_radius= 2 )

#  idList = [22 , 23 , 24 , 26 , 110 , 157 , 158 , 159 , 160 , 161 , 130 , 243]

RIGHT_EYE=[ 33, 7, 163, 144, 145, 153, 154, 155, 133, 173, 157, 158, 159, 160, 161 , 246 ] 
LEFT_EYE =[ 362, 382, 381, 380, 374, 373, 390, 249, 263, 466, 388, 387, 386, 385,384, 398 ]




def Face_Mesh(frame):
    # MyFaces = []
    imgRGB =  cv2.cvtColor(frame , cv2.COLOR_BGR2RGB)
    results =  faceMesh.process(imgRGB)
    if results.multi_face_landmarks  != None:
        for FaceLand in results.multi_face_landmarks:
            MyFace= []
            # mpDraw.draw_landmarks(resized_image,FaceLand, mpFaceMesh.FACE_CONNECTIONS , drawSpace , drawSpace)
            for LandMark  in FaceLand.landmark:
                MyFace.append( ( int(LandMark.x*width), int(LandMark.y*height) ) )
 
        return MyFace    



def euclaideanDistance(point, point1):
    x, y = point
    x1, y1 = point1
    distance = math.sqrt((x1 - x)**2 + (y1 - y)**2)
    return distance





def blinkRatio_Right(frame, landmarks, right_indices):
    # Right eyes 
    # horizontal line 
    rh_right = landmarks[right_indices[0]]
    rh_left = landmarks[right_indices[8]]
    # vertical line 
    rv_top = landmarks[right_indices[12]]
    rv_bottom = landmarks[right_indices[4]]
    # draw lines on right eyes 
    cv2.line(frame, rh_right, rh_left, (255 , 0 , 255), 2)
    cv2.line(frame, rv_top, rv_bottom, (255 , 255 , 255), 2)

    rhDistance = euclaideanDistance(rh_right, rh_left)
    rvDistance = euclaideanDistance(rv_top, rv_bottom)

    reRatio = (rhDistance/rvDistance)

    return reRatio


def blinkRatio_Left(frame, landmarks, left_indices):
    # LEFT_EYE 
    # horizontal line 
    lh_right = landmarks[left_indices[0]]
    lh_left = landmarks[left_indices[8]]

    # vertical line 
    lv_top = landmarks[left_indices[13]]
    lv_bottom = landmarks[left_indices[4]] #hdhd

    cv2.line(frame, lh_right, lh_left, (255 , 0 , 255), 2)
    cv2.line(frame, lv_top, lv_bottom, (255 , 255 , 255), 2)


    lvDistance = euclaideanDistance(lv_top, lv_bottom)
    lhDistance = euclaideanDistance(lh_right, lh_left)

   

    leRatio = (lhDistance/lvDistance)
    return leRatio





while True:
   
    ignore, frame = cam.read()
    frame = cv2.resize(frame, (width, height))
    Face = Face_Mesh(frame)
    if Face != None :

        for id in  LEFT_EYE:
            cv2.circle(frame , Face[id], 2 , (255 , 255 , 0) , -1)
        for id in  RIGHT_EYE :   
                cv2.circle(frame , Face[id], 2 , (255 , 255 , 0) , -1)

        
        Ratio_Right = blinkRatio_Right(frame, Face, RIGHT_EYE)
        Ratio_Left  = blinkRatio_Left(frame, Face, LEFT_EYE )
        
        if Ratio_Right > 5.4 :
            pyautogui.press('tab')


      
                                                                                                        
        
      

      

    
    cTime = time.time()
    fps = 1 / (cTime - pTime )
    pTime = cTime
    cv2.putText(frame, f'FPS:{int(fps)}',(20,70), cv2.FONT_HERSHEY_PLAIN,
                3,(0,255,0),3 )   
  

    cv2.imshow("hello", frame)
    cv2.waitKey(1)


cam.release()  