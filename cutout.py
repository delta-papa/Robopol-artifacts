import os
import imageio
import glob
import json

def cutout():
    
    
    json_file=open('input_param.json')
    data = json.load(json_file)
    
    png_src=data['cutout'][0] #path to all png images 
    artifact_src=data['cutout'][1] #path to all artifact coordinate files
    stars_src=data['cutout'][2] #path to all star coordinate files
    
    ref_folder=data['cutout'][3] #path where all reflection artifact cutouts are kept 
    
    star_folder=data['cutout'][4] #path where all stars cutouts are kept
    
    
    
 
    for img in glob.glob(png_src):
        im=imageio.imread(img)        

        name=img[6:-3]+"txt" #strip the .png and path name from the image name and add .txt to the name

        #search for the artifact coordinate text file for this image
        arti_name=artifact_src+"arti_"+name 

        f=open(arti_name,"r") #open the artifact coordinate text file 
        lines=f.readlines() #store all the lines in the file in the lines list

        for line in lines: #loop through all the lines
            line=line.split() #split every word of the line as a string

            x,y=(line[0]),(line[1]) #store the x and y coordinates 
            x,y=float(x),float(y) #convert from string to float
            x,y=int(x),int(y) #convert from float to int 
            
            #The way coordinates are referenced in DS9 and IRAF is slightly different than for 
            #Python image viewers. Hence we need to apply the scaling below for the coordinates so that
            #we can make a correct cutout for a given x and y. 
            
            x1=2047-(y+32) 
            x2=2047-(y-32)
            y1=x-32
            y2=x+32

            cutout=im[x1:x2,y1:y2] #make a cutout based on the coordinates

            outname=ref_folder+"cut_arti_"+name[:-3]+"_"+str(x)+"_"+str(y)+".png" #store an output name
            imageio.imwrite(outname,cutout,format="PNG")

        f.close()
        
        #Repeat the same for stars
        
        star_name=stars_src+"coords_"+name 
        g=open(star_name,"r")
        star_lines=g.readlines()
        for l in star_lines:
            l=l.split()

            x,y=(l[0]),(l[1])
            x,y=float(x),float(y)
            x,y=int(x),int(y)
            x1=2047-(y+32)
            x2=2047-(y-32)
            y1=x-32
            y2=x+32

            cutout=im[x1:x2,y1:y2]
            outname=star_folder+"cut_star_"+name[:-4]+"_"+str(x)+"_"+str(y)+".png"
            imageio.imwrite(outname,cutout,format="PNG")
        g.close()
    
cutout()
