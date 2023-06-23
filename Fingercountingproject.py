import  cv2
import time
import os
import HandTrackingMin as htm#hand tracking module ta import korlam jeta age baniyechi

from cv2 import putText

from matplotlib import image
from directkeys import PressKey, ReleaseKey, Z
wCam,hCam=640,480
cap=cv2.VideoCapture(1)#this is for camera selection
cap.set(3,wCam)# 3 here is widthof the cam
cap.set(4,hCam)#4 is height of the camera
folderPath="FingerImage"# this is the path of the image s folder

myList=os.listdir(folderPath)#here we want to list all the files present in our directory
print(myList)
overlayList=[]
for imPath in myList:
    image=cv2.imread(f'{folderPath}/{imPath}')
    overlayList.append(image)# ekhane overlayList e sob image gulo eke EKE APPEND HOLO..
# print(len(overlayList))#if it is 6 so img appaend hoyechwe
pTime = 0 
#through this loop we get each of the images..here loop ta amimyList directory r opor xchalachi and imPath holo bindex of images ,so amra sob image gulo pabo
tipIds=[4,8,12,16,20]#it stores the top finger tips of each finger
detector=htm.handDetector(detectionCon=0.75)
while True:
    success,img=cap.read()
    img=detector.findHands(img)# we will twll out detector to find our image return the image.we know that in hour handmodule there is a handDetector class and inside this class there is a function findHands which will find the hand and return  the image..

    lmList=detector.findPosition(img,draw=False)#we here create a list andf it will find the position of the image  and here draw is false bcz ,we here  already drawing so false dilam.
    #print(lmList)# it will tell the location of my hand or img whatever wwe say.. when hand will be in the screen it shows the location otherwise it returns the empty aRRAY.
    #if len(lmList)!=0:
    if len(lmList)!= 0:
        fingers=[]
        #THUMB
        if lmList[tipIds[0]][1]>lmList[tipIds[0]-1][1]:
                fingers.append(1)
        #EER AAGE OBDI HOCHILO KI JODI JODI JET A NORMAL  RULE FINGER UP DOWN ER SETA FOLLOW KORI THEN THUMB ER KHETRE EKTA PROBLEM ARRAISE KORCHILO  SETA HOLO INCASE OF THUMB WE NVER 4 KE 0 BA 2 ER NICHE NAMATE  PARINA NATURALLY..SO AMRA JOKHON HAT BONDHO KORI HOY THUMB ER TOP POINT 4 2 ER LEFT  E THAKE ...AAAR RIGHT E THAKLE THUMB KHOLA THAKE..SO THATS WHY  ALADA KORE THUMB LIKHTE HOLO..AAR AS EKHANE NO LOOP USE SO IDN R INDEX DIYE DITE HBE JETA HOLO 0
        else:
                fingers.append(0)
        #FOR OTHER 4 FINGER
        for id in range(1,5):
             #HOW WE CAN UNDER  STAND THAT A FINGER IS CLOSED OR UP ..WE KNOW PROTYWK  ANGUL; ER PAB ER EK EKTA POINT AXCHE SO SUPPOSE JODI KORI ANGUL DHORI  KORI ANGUL TA BONDHO SO ER LOGIC HBE JODI KORI ANGUL ER TOP POINT MANE 8 POINT TA 7 BA 6 5 ER THEKE DOWN E THAKE THEN ETAKE BONDHO ANGUL DHORBO..and here [2] holo 0 1 2 index finger mne torjonir koto number angul.
            if lmList[tipIds[id]][2]<lmList[tipIds[id]-2][2]:
                fingers.append(1)
                #ekkhane basically age each finger alada kore mentionkorte hochilo but ekhane sob finger er jonno jate bar bar likhte nahoy so loop chalalam aar GER BAR TIP ID ER BODOLE OPRE ITPID ER J ARRAY BANIYECHI TOP ID GULO NIYE SETAR INDEX ANUJAYI LAGALAM BYAS TAHOLE EBAR PROTYEK FINGER ER JONNO KAJ KORBE..AAR JODI CONDITION SATISFY HOY THEN EKTA BLANK FGINGER ARRAY ACHE TAR MODHYE 1 DOBO NAHOLE 0 DEBO.J J ANGUL OPEN THAKBE  TAR INDEX 1 HOYE JABE.
            else:
                fingers.append(0)
               
       # print(fingers)
        totalFingers=fingers.count(1)#basically we told here to count howmany 1 is there in fingers array and return it into totalFingers......
        print(totalFingers)
        h,w,c=overlayList[totalFingers-1].shape#eta korara reason holo we actually dont know j image gulo amra niyechi tar height ar width koto each img er height and width alada shoo  h,w,c te asmra overlaylist er jokhon j imgg asbe tar shape cal culate kore h ,w, c te dhukiye debo and seta img[0:h,0:w] te h aar w diye easily replaced hoye jabe. 
        # We know tootal finger holo jota 1 ache now img[0:h,o:w]=overlayList[totalFingers-1] ekhane total fingers jjai hbe tar theke -1 kore j sonkhyta ta pabo toto number index number er img print hb..now one important thing is 0 ta kemne elo…
# Bcz jokhon kono  finger uthchena then tf=0 aar tar -1 == -1 aar python e  neg index -1 mane last element jeta 6.jpg  jar mopdhye 0  chilo
        img[0:h,0:w]=overlayList[totalFingers-1]# here overlist e thaka img jeta img  te show hbe tar modhye store korlam.. jar height hbe h and width hbe w ..img holo total video ta and here tar thik h w pos er oi part tuku replace korlam overlayList  er  img dwara..`` 
    cTime=time.time()
    fps=1/(cTime-pTime)
    pTime=cTime#through this swap process we overlayed the image
    cv2.putText(img,f'FPS:{int(fps)}',(400,70),cv2.FONT_HERSHEY_DUPLEX,2,(255,0,0),3)
    # id=1
    # id=input("Enter the no")
    if(cv2.waitKey(1) & 0xFF==ord("Q") ) or (cv2.waitKey(1) & 0xFF==ord("q")):
        cap.release()
    #ekhane prothome img ta nilam then FPS: lekhata asbe aar taravalue ta intiger format e typecast hoye  asbe then 400,70 ta holo locvation of this lekha,2 ta holo width,and tar por jeta ache seta style then BGR format e colour dilam and last e 3 ta thickness
    cv2.imshow("Image",img)
    cv2.waitKey(1)
    
    # if(cv2.waitKey(1) and 0xF==ord("q")):
    #     break