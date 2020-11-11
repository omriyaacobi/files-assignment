'''
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 10:07:28 2019

load an image as a Pillow image object. 
Convert to a NumPy array. Convert NumPy array to an Image object
 
@author: dina
"""
#from matplotlib import pyplot
from PIL import Image
from numpy import asarray

#load the image
image1_p = Image.open('ffs.png')
#convert image to numpy array
data_p = asarray(image1_p)
print("\ndata_p\n",data_p)
print("data shape PIL: ",data_p.shape)

#create Pillow image
image2_p = Image.fromarray(data_p)
#image details
print('\nimage format use PIL: ', image2_p.format)
print('image mode: ', image2_p.mode)
print('image size: ', image2_p.size)
print('\n',image2_p)


import matplotlib.image as mpimg
import matplotlib.pyplot as plt
 
#load image as pixel array
data_m = mpimg.imread("ffs.png")
print("\ndata_m\n", data_m)
#summarize shape of the pixel array
print(data_m.dtype)
print(data_m.shape)

#display the array of pixels as an image
plt.imshow(data_m)
plt.show()
'''
from PIL import Image
import os
import matplotlib.pyplot as plt

import numpy as np
import shutil 
import math
def transfer(path1,path2):
    #function get 2 paths and copy the required number of images from one director to another
    li=os.listdir(path2)
    if(path1==createlibrary(createlibrary("C:/bigfoler","folder"), "test")):
        for i in li:
            shutil.copy(os.path.join(path2,i),path1)
    if(path1==createlibrary(createlibrary("C:/bigfoler","folder"), "train")):    
        for i in range(math.floor(0.7*len(li))):
           shutil.copy(os.path.join(path2,li[i]),path1)


def plot_images(images):
    
   #function shows in plot all the files+ prints the name of the files
    li=os.listdir(createlibrary(createlibrary("C:/bigfoler","folder"), "test"))
    
    #plots the images in the list images
    
    f ,axs = plt.subplots(len(images))  
    for i in range(len(images)):
        axs[i].set_title(li[i])
        axs[i].imshow(images[i]) #imshow is from import matplotlib
       
    plt.show()
    

def createlibrary(path,name):
    #function creates directory in a path given with a name given+ return the created directory's path
    if(path==''):
        path="C:/Users/ori1j/OneDrive/שולחן העבודה"
    path=path+'/'+name
    try:
        os.mkdir(path)
    except OSError:
        print ("Creation of the directory %s failed" % path)
    else:
        print ("Successfully created the directory %s " % path)
    return path




createlibrary(createlibrary("C:/bigfoler","folder"), "train")
createlibrary(createlibrary("C:/bigfoler","folder"), "test")
transfer(createlibrary(createlibrary("C:/bigfoler","folder"), "train"),'C:/folder1')
transfer(createlibrary(createlibrary("C:/bigfoler","folder"), "test"),'C:/folder1')
li=os.listdir(createlibrary(createlibrary("C:/bigfoler","folder"), "test")) #list of all the images in test
images = [np.array(Image.open(os.path.join(createlibrary(createlibrary("C:/bigfoler","folder"), "test"),filename))) for filename in li]
plot_images(images)