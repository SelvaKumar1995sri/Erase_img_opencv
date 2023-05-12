import cv2
screen="Drawing" #Output screen Name 
img=cv2.imread("result.jpg") #After changing background 
bg=cv2.imread("frame2.jpg")  #Original Image 
#resize both image to same size
half = cv2.resize(img, (0, 0), fx = 0.1, fy = 0.1) 
bghalf = cv2.resize(bg, (0, 0), fx = 0.1, fy = 0.1)
cv2.namedWindow(screen)
eraser=False 
radius = 1  #Brush Size

def draw_circle(x,y):
        color = bghalf[y,x]
        cv2.circle(half, ( x, y), radius, (int(color[0]), int(color[1]), int(color[2])), -1)
        cv2.imshow(screen,half)

def handleMouseEvent(event,x,y,flags,param):
      global eraser , radius     
      if (event==cv2.EVENT_MOUSEMOVE):
            if eraser==True:
                  draw_circle(x,y)
      elif (event==cv2.EVENT_MOUSEWHEEL):
            if flags > 0:
                radius +=   5
            else:
                if radius > 10:
                    radius -=   5
      elif event == cv2.EVENT_LBUTTONUP:
            eraser = False
      elif (event==cv2.EVENT_LBUTTONDOWN):
            eraser=True
            draw_circle(x,y)

cv2.setMouseCallback(screen,handleMouseEvent)
cv2.imshow(screen,half)
cv2.waitKey(0)
cv2.destroyAllWindows()