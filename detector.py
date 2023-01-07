import cv2

cap = cv2.VideoCapture(1,cv2.CAP_DSHOW)

Classif = cv2.CascadeClassifier('garbage.xml')

while True:
   
   ret,frame = cap.read()
   gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

   waste = Classif.detectMultiScale(gray,
   scaleFactor = 10,
   minNeighbors = 150,
   minSize=(95,95))

   for (x,y,w,h) in waste:
      cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
      cv2.putText(frame,'litter',(x,y-10),2,0.7,(0,255,0),2,cv2.LINE_AA)

   cv2.imshow('frame',frame)
   
   if cv2.waitKey(1) == 27:
      break
cap.release()
cv2.destroyAllWindows()