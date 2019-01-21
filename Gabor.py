# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 13:01:12 2019

@author: erago




"""

import numpy as np
import math
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw #Подключим необходимые библиотеки. 

def gabor(D, T, point):
    return 1 + math.exp((-1 * point**2) / 2 * D**2) * math.cos(2 * math.pi * point * T)

plt.clf() # стираю предыдуший кадр
d = 0.007
t = 0.01
x = [gabor(d, t, i) for i in range(- 255, 255)]
print("")

plt.plot(range(- 255, 255), x)
plt.show()

n = 3

image = Image.open("temp.jpg") #Открываем изображение. 
draw = ImageDraw.Draw(image) #Создаем инструмент для рисования. 
width = image.size[0] #Определяем ширину. 
height = image.size[1] #Определяем высоту. 	
pix = image.load() #Выгружаем значения пикселей.

for i in range(width):
    for j in range(height):
        if i >= n and j >= n and i + n < width and j + n < height:
            S = 0
            for k in range(i - n, i + n):
                for l in range(j - n, j + n):
                    S += pix[k, l][0] + pix[k, l][1] + pix[k, l][2]
            S = S // (n**2 * 12)
            S = math.trunc(128 * gabor(d, t, S))
        else:
            S = (pix[i, j][0] + pix[i, j][1] + pix[i, j][2]) // 3
            S = math.trunc(128 * gabor(d, t, S))
        draw.point((i, j), (S, S, S))
        
        
image.save("ans.jpg", "JPEG")

print("n =", n)
