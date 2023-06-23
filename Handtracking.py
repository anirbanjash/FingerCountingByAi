import cv2  # jjoto camera ache tar module
import mediapipe as mp#hand trackl kora
import time
cap=cv2.VideoCapture(0)#camera number ekhane..
mpHands=mp.solutions.hands# this hand s is a class thats why there is no brackket open close,mp  module r vetor solution function
hands=mpHands.Hands()# tghis hands is a function mphands holon variable ekta``
mpDraw=mp.solutions.drawing_utils#eta duto pab er mane hater paber majhe j daag  gulo ache tar jonno
pTime=0
cTime=0
while True:
    success,img=cap.read()# ja image capture hbe seta cap e ache then seta read hoche
    imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results=hands.process(imgRGB)
    # print(results.multi_hand_landmarks)
    multihands=results.multi_hand_landmarks#MULTYHANDS E
    if  (multihands):
       for handLms in  multihands:#C AT A TIME KON HAT ATA BEBOHARHOCHE DEKHA JABE
           for id, lm in enumerate(handLms.landmark): #ENUMERATEINDEXD KORE
            #    print(id,lm)
               #id taa holo finger tips and lm holo landmarks
               h,w,c=img.shape#height width colour channel
               cx,cy=int(lm.x*w),int(lm.y*h)#ETA GRAPH FORMAT E STORE KORBE
               print(id,cx,cy)
               #if(id==4 or id==8):# if wew remove this if then it add the circle mark too all id ba pabo of hands
               cv2.circle(img,(cx,cy),15,(255,0,0),cv2.FILLED)#  15 is radius cx cy  co ordinate 255,0,0  et bgr
                

           mpDraw.draw_landmarks(img,handLms,mpHands.HAND_CONNECTIONS)
    cTime=time.time()
    fps=1/(cTime-pTime)
    pTime=cTime
    cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_SCRIPT_COMPLEX,3,(255,43,234),thickness=2)
    #KOTHAY ANKBO ??=> img te ,,ki ankgo ==>fps (ami only text pari mane only string so typecast korlam),kothay ankbo??=> co ordinates of frame,style,3=font size ,255,43,234 BGR..
    cv2.imshow("Image",img)# jeta capture hoyeche ota show kore dao ,
    cv2.waitKey(1)#you have to eait er main kaj aager j image ta esche ota k stay koray ei wait key command ta..erom sec sec e age img ta rakhe ba wait koray.
    
    # all images or colour  in open cv it reads in bgr format..but we get  this as rgb format so we have to converrt it.