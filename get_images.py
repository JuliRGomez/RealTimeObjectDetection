from venv import create
import cv2
import os
import time
import uuid

IMAGES_PATH = 'Tensorflow/workspace/images/collectedimages'

labels = ['hello', 'thanks', 'yes', 'no', 'iloveyou']
num_imgs = 15
label_count = 0
imgs_count = 0
my_time = 0
my_timer = False

def my_timmer():
    global my_time
    global my_timer
    my_time-=1
    time.sleep(0.5)
    if my_time == 0:
        my_timer = True

def create_directory(label):
    os.mkdir(os.path.join(IMAGES_PATH,label))
    global imgs_count 
    imgs_count = 0

def save_img(frame, label):
    global imgs_count
    global num_imgs
    global label_count
    imgName = os.path.join(IMAGES_PATH, label, label +'.'+'{}.jpg'.format(str(uuid.uuid1())))
    cv2.imwrite(imgName,frame)
    if imgs_count < num_imgs:
        imgs_count+=1
    else:
        label_count+=1
        create_directory(labels[label_count])

#create_directory(labels[label_count])
text = 'hola mundo'
cap = cv2.VideoCapture(0)

while (cap.isOpened()):
    text = f"label: {labels[label_count]} image_number:{imgs_count} time = {my_time}"
    _,frame = cap.read()
    frame_copy = frame.copy()
    cv2.putText(frame_copy,text,(20,20),cv2.FONT_HERSHEY_SIMPLEX,0.65,(0,0,255),2,cv2.LINE_AA)
    cv2.imshow('frame',frame_copy)
    
    if my_timer and my_time<=0:
        my_timer = False
        my_time = 0
        if label_count > 4:
                break
        save_img(frame,labels[label_count])
    
    if my_time > 0:
        my_timmer()
    
    k = cv2.waitKey(1) & 0xFF 
    if k == ord('q'):
        break
    if k == ord ('c'):
        my_time=6
        my_timmer()
       
        
cap.release()
cv2.destroyAllWindows()