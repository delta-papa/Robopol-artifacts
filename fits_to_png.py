import os
import glob
from astropy.io import fits
import numpy as np
from PIL import Image
import json


def fits_to_png():
    
    json_file=open('input_param.json')
    data = json.load(json_file)
    
    input_path=data['fits_to_png'][0] #path where you will find the fits images
    
    outpath=data['fits_to_png'][1] #path where you want to keep the png images
    
    for filename in glob.glob(input_path):
        image_data = fits.getdata(filename, ext=0)


        median=np.median(image_data) #median value of image
        std_dev=np.std(image_data) #std deviation of image 
        min_val=np.min(image_data) #minimum value of image
        max_val=np.max(image_data) #maximum value of image

        a=0 #minimum value in grayscale image
        b=255 #maximum value in grayscale image
        c=median-0.5*std_dev #lower threshold
        d=median+2*std_dev #higher threshold


        lower = image_data < c #find pixel values less than threshold
        image_data[lower] = 0 #set those values to 0

        higher = image_data > d #find pixel values greater than threshold
        image_data[higher] = 255 #set them to 255

        middle=  (image_data <= d) & (image_data >= c) #find pixel values between c and d

        image_data[middle]= (image_data[middle] - c)*(b - a)/(d - c) + a #scale those values according to our formula

        I = image_data.astype(np.uint8)#make sure you set the data type to unsigned integer 8 bit since it is a grayscale image
        
        I=np.rot90(I,2) #rotate by 90 degree twice
        I=np.flip(I,1) #flip horizontally so that it is same as original fits image
        img = Image.fromarray(I)
        filename=outpath+filename[18:-5] #strip ./artifact_images and .fits from the filename
        img.save(filename+".png","PNG") #save image as a PNG File

fits_to_png()
