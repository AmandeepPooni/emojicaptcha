import init
import numpy as np
labels= {'angry': 0,
 'disgust': 1,
 'fear': 2,
 'happy': 3,
 'neutral': 4,
 'sad': 5,
 'surprise': 6}
labels=init.idx_to_class(labels)
import cv2
import numpy as np
from time import sleep
import torch as T
import torchvision.transforms as transforms
from PIL import Image


face_classifier = cv2.CascadeClassifier('gg.xml')

def face_detector(img):
    # Convert image to grayscale
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
    if faces is ():
        return (0,0,0,0), np.zeros((224,224), np.uint8), img
    
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]

    try:
        roi_gray = cv2.resize(roi_gray, (224, 224), interpolation = cv2.INTER_AREA)
    except:
        return (x,w,y,h), np.zeros((224,224), np.uint8), img
    return (x,w,y,h), roi_gray, img

cap = cv2.VideoCapture(0)
validation_preprocessing = transforms.Compose([
    transforms.Grayscale(num_output_channels=1),
    
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    
])
model=init.model
while True:

    ret, frame = cap.read()
    rect, face, image = face_detector(frame)
    if np.sum([face]) != 0.0:
        # roi = face.astype("float") / 255.0
        # roi = img_to_array(roi)
        # roi = np.expand_dims(roi, axis=0)
        roi=Image.fromarray(face)
        
        roi=validation_preprocessing(roi)
        
        
        # make a prediction on the ROI, then lookup the class
        preds = init.predict(roi.unsqueeze(0).to('cuda'),model)[1]
        
        label = labels[preds.item()]  

        label_position = (rect[0] + int((rect[1]/2)), rect[2] + 25)
        cv2.putText(image, label, label_position , cv2.FONT_HERSHEY_SIMPLEX,2, (0,255,0), 3)
    else:
        cv2.putText(image, "No Face Found", (20, 60) , cv2.FONT_HERSHEY_SIMPLEX,2, (0,255,0), 3)
        
    cv2.imshow('All', image)
    if cv2.waitKey(1) == 13: #13 is the Enter Key
        break
        
cap.release()
cv2.destroyAllWindows()

