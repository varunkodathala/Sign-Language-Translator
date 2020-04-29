import cv2
import numpy as np 
from tensorflow.keras import models
import time
import pyttsx3
import os


model = models.load_model('/Users/varun/Documents/Deep_Learning/Learn_PYTORCH/gesture_detection/gesture_model.h5')

cam = cv2.VideoCapture(0)

engine = pyttsx3.init('nsss')


class_labels = ['A','B','C','D','E','F','G','H','I','J','K','L',
               'M','N','O','P','Q','R','S','T','U','V','W','X',
               'Y','Z','delete','nothing','space']

i=0

font = cv2.FONT_HERSHEY_SIMPLEX

def format_string(label,string):

    if(label!='delete' and label!='space' and label!='nothing'):
        string = string + str(label)


    if(label == 'delete'):
        string = string[:-1]
    
    if(label == 'space'):
        string = string + " "

    if(label == 'nothing'):
        string = string
    
    return string

def speak(text):

    engine.say(text)
    engine.runAndWait()



string = ""


while(True):
    
    ret,frame = cam.read()
    frame = cv2.flip(frame,1)
    frame = cv2.rectangle(frame, (100,100), (450,400), (0,0,255), 2)
    frame = cv2.rectangle(frame, (1150,20), (1240,70), (0,0,0), 2)
    frame = cv2.arrowedLine(frame, (1040,45), (1140,45), 
                                     (0,0,0), 4)
    # frame[20:70,1200:1270,:] = (255,255,255)
    cv2.putText(frame,"Tap to speech",(1000,80), font, 0.5,(255,0,0),1,cv2.LINE_AA)

    roi = frame[100:400,100:450,:]
    speech_roi = frame[20:70,1150:1240,:]
    speech_gray = cv2.cvtColor(speech_roi,cv2.COLOR_BGR2GRAY)

    T = 229


    if(i>0):

        ret,speech_threshold = cv2.threshold(speech_gray,128,255,cv2.THRESH_BINARY)
        mean_speech = np.mean(speech_threshold)

        if(mean_speech<T):
            speak(string)
            break

        diff = cv2.absdiff(frame,temp)
        mean_val = np.mean(diff)
        if(i>1.5):
            val = mean_val - temp_mean
            if(val>1):
                img = cv2.resize(roi,(64,64))
                img = img/255
                img = np.expand_dims(img,axis = 0)
                prediction = model.predict(img)
                label = class_labels[prediction.argmax()]
                time.sleep(0.1)   
                string = format_string(label,string)    
                      
            
        temp = frame
        temp_mean = mean_val
    else:
        temp = frame
    i+=1

    # roi = cv2.flip(roi,1)

    disp = np.zeros((840,1280,3),np.uint8)
    disp[120:,:,:] = frame
    disp[:120,:,:] = (51,204,204)

    disp[650:,:,:] = (51,204,204)

    fps = cam.get(cv2.CAP_PROP_FPS)
    cv2.putText(disp,f"fps: {round(fps)}",(10,40), font, 1,(0,0,0),2,cv2.LINE_AA)
    cv2.putText(disp,f"Kodathala Sai Varun",(490,90), font, 1,(0,0,0),2,cv2.LINE_AA)
    cv2.putText(disp,f"Sign Language Translator",(450,40), font, 1,(0,0,0),2,cv2.LINE_AA)
    cv2.putText(disp,"Translated: ",(550,700), font, 1,(0,0,0),2,cv2.LINE_AA) 
    cv2.putText(disp,str(string),(0,750), font, 1,(0,0,0),2,cv2.LINE_AA)  
    disp[140:190,1150:1240,:] = (255,255,255)

    cv2.imshow("frame",disp) 


    if (cv2.waitKey(1) & 0xFF == ord('q')):
        break

cv2.destroyAllWindows()
