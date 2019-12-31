import cv2
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import os

images = os.listdir('images/')

start = (35,35,35)
end = (100,255,255)

def mask_image(image):
    mask = cv2.inRange(image, start, end)
    result = cv2.bitwise_and(image, image, mask=mask)
    return mask, result    
    
for filename in images:
    print(filename)
    img = cv2.imread(os.path.join('images/',filename), cv2.COLOR_BGR2HSV)
    mask, result = mask_image(img)
    
    im = Image.fromarray(result)
    im.save(f"output/{filename}_converted.jpeg")