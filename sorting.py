import os
import json
def sorting():
    
    json_file=open('input_param.json') #open parameter file
    data = json.load(json_file) #load everyting into dictionary called 'data'
    json_file.close() #close the parameter file
    
    sorting_path=data['sorting'][0] #get the path where all the .cat files are stored
    
    txt_path=data['sorting'][1] #path where all sorted .cat files will be made with extension .txt
    
    for file in os.listdir(sorting_path):
        
        
        if file.endswith(".cat"): #proceed if file is a ".cat" file
            cat_file=sorting_path+file
            filename=open(cat_file,"r") #open the file in reading mode
            lines=filename.readlines() #store all lines in the file in a list
            filename.close()

            src=txt_path+file[:-4]+".txt" 
            #remove the .cat extension and append .txt extension instead to the filename

            writefile=open(src,"w") #open a new file with above .txt name in writing mode.

            #write those lines in the original file which end with 0 to the file 'src'
            #note that you may have to strip any leading and trailing whitespaces using .strip() method
            #for strings 

            for foundlines in [fi for fi in lines if fi.strip().endswith("0")]:
                writefile.write(foundlines)

            writefile.close() #close the file

            f=open(src,"r") #open the src file in read mode.
            newlines=f.readlines() #store all its lines in a list
            newlines.sort(reverse=True) #sort the lines numerically in descending order.
            #Note that although we said ascending order above, here Python doesn't consider the minus sign 
            #and hence we should sort in reverse.
            f.close()

            f=open(src,"w") #open the src file in write mode.
            f.truncate(0) #erase all of its contents

            for l in newlines: #loop through the sorted lines and write them in the file we just erased
                f.write(l)
            f.close()
            #Your text files are ready.
            
sorting()
