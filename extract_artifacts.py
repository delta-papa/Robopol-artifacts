import os
import json

def extract_artifacts():
    
    

    json_file=open('input_param.json')
    data = json.load(json_file)
    
    logfile = data['extract_artifacts'][1] #path to logfile made using imexamine
    

    f=open(logfile) #read the log file
    path= data['extract_artifacts'][0] #specify output folder path

    lines=f.readlines() #store all lines in a list called 'lines'


#filelist = [ g for g in os.listdir(path) ] #collect any existing files in the output folder
#for anyfile in filelist: #loop through those files
#    os.remove(os.path.join(path, anyfile)) #remove those files
    lines=[lines[m].split() for m in range(len(lines))] #split the lines i.e. remove the whitespaces
    
    i=0 
    while i <= (len(lines)-1): 

        if(lines[i][0]=="#"): #we know it is a new image 
            image_name=lines[i][2] #store the name of the image
            name="arti_"+str(image_name) #prefix the name with "arti_"
            name=name[:-4]+"txt" #remove '.fits' extension and add '.txt' extension
            filename=os.path.join(path,name) #store final path
            w=open(filename,"w") #open the new result file
            i+=1 #increment pointer by 1
            while(lines[i][0]!="#"): #make sure the line is a coordinates line and not image description line
                x,y=float(lines[i][0]),float(lines[i][1]) #store x and y coordinates
                w.write("%f\t%f\n"%(x,y)) #write the x and y to file
                i+=1 #increment by 1 
                if i==len(lines): #if we have reached end of file exit the program
                    break        

            w.close() #close the file
            
extract_artifacts()