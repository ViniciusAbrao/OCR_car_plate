import cv2

im = cv2.imread('placa-carro2.jpg')

im=cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
ret,thresh1 = cv2.threshold(im,127,255,cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(thresh1,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
i=0
for cnt in contours:
        x,y,w,h = cv2.boundingRect(cnt)
        if w<1.4*h and w>0.6*h and h>30 and w<100 and h<70:
            print(w)
            i=i+1
            cv2.rectangle(im,(x,y),(x+w,y+h),(0,255,0),3)

    
cv2.namedWindow('BindingBox', cv2.WINDOW_NORMAL)
cv2.imshow('BindingBox',im)