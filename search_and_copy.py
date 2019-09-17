import os
from shutil import copy
import json

def search_and_copy():
    json_file=open('input_param.json')
    data = json.load(json_file)
    
    source=data['search_copy'][0] #path where original RoboPol data is stored
    dest=data['search_copy'][1] #path where selected artifact images have to be kept ready
    textfile=data['search_copy'][2] #path to the textfile containing the names of images having artifacts
    
    f=open(textfile,"r") #read the textfile
    
    lines=f.readlines() #store all lines in file in list "lines"    

    for line in lines: 
        #go through every image name ('line') in the text file
        for dirpath, dirnames, filenames in os.walk(source): 
            #walk through all subdirectories and files in them
            
            image=line #Why we store line in image is because we will be 
            #appending .fits to the line every iteration. Therefore, 
            #we don't want to keep appending .fits to lines already 
            #ending with .fits else it would become something like 
            #.fits.fits and so on
            image=image.strip() #we strip the whitespace from each line
            image=image+".fits" #we add a '.fits' extension to each line 

            #First, make a list of all those files in each directory 
            #that end with the given "line" (image name) in our "bad_data.txt" 
            #file. That is make a list of all those images in 
            #each directory which have the same name as that of the 
            #names in our "bad_data.txt" file.
            #Then iterate through those found images in each directory. If they are
            #not already in the destination directory copy them to destination
            #and copy them to destination directory. 

            for foundfile in [fi for fi in filenames if image in fi]:
                src=os.path.join(dirpath,foundfile) #store the path of the image in list 'src'
                if not foundfile in os.listdir(dest):
            
                    copy(src,dest) #copy list 'src' to destination'dest' which can be a directory or a file
search_and_copy()