#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install opencv-python numpy pandas


# In[2]:


import os
os.getcwd()


# In[3]:


import argparse
import cv2
import pandas as pd


# In[4]:


img_path = "colorpic.jpg"
img = cv2.imread(img_path)


# In[5]:


#Reading csv file with pandas and giving names to each column
index=["color","color_name","hex","R","G","B"]
csv = pd.read_csv('colors.csv', names=index, header=None)


# In[6]:


csv.head()


# In[9]:


cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_function)


# In[11]:


clicked = False
r = g = b = xpos = ypos = 0


# In[8]:


def draw_function(event, x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global b,g,r,xpos,ypos, clicked
        clicked = True
        xpos = x
        ypos = y
        b,g,r = img[y,x]
        b = int(b)
        g = int(g)
        r = int(r)


# In[10]:


def getColorName(R,G,B):
    minimum = 10000
    for i in range(len(csv)):
        d = abs(R- int(csv.loc[i,"R"])) + abs(G- int(csv.loc[i,"G"]))+ abs(B- int(csv.loc[i,"B"]))
        if(d<=minimum):
            minimum = d
            cname = csv.loc[i,"color_name"]
    return cname


# In[ ]:


while(1):
    cv2.imshow("image",img)
    if (clicked):
        #cv2.rectangle(image, startpoint, endpoint, color, thickness) -1 thickness fills rectangle entirely
        cv2.rectangle(img,(20,20), (750,60), (b,g,r), -1)

        #Creating text string to display ( Color name and RGB values )
        text = getColorName(r,g,b) + ' R='+ str(r) + ' G='+ str(g) + ' B='+ str(b)

        #cv2.putText(img,text,start,font(0-7), fontScale, color, thickness, lineType, (optional bottomLeft bool) )
        cv2.putText(img, text,(50,50),2,0.8,(255,255,255),2,cv2.LINE_AA)
  #For very light colours we will display text in black colour
        if(r+g+b>=600):
            cv2.putText(img, text,(50,50),2,0.8,(0,0,0),2,cv2.LINE_AA)

        clicked=False

    #Break the loop when user hits 'esc' key 
    if cv2.waitKey(2) & 0xFF ==27:
        break

cv2.destroyAllWindows()


# In[ ]:


import numpy as np
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
color = np.uint8([[[b,g,r]]])
hsv_color = cv2.cvtColor(color,cv2.COLOR_BGR2HSV)
lower_range = np.array([hsv_color[0][0][0] - 10,100,100])
upper_range = np.array([hsv_color[0][0][0] + 10,255,255])

mask = cv2.inRange(hsv, lower_range, upper_range)

cv2.imshow('mask', mask)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:




