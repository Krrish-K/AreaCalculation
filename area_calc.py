# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 11:49:01 2020

@author: krish
"""
from PIL import Image
import random
im=Image.open("map-01.png")
rgb_im=im.convert("RGB")
count_in=0
count_pun=0
count=0
while(count<=100000):
    x=random.randint(0,2480)
    y=random.randint(0,2735)
    z=0
    r,g,b=rgb_im.getpixel((x,y))
    if(r==60):
        count_in=count_in+1
        count+=1
    else:
        if(r==80):
            count_pun+=1
            count+=1
            
area_pun=(count_pun/count_in)*3287263
print(area_pun)
