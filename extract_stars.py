import os
import json

def extract_stars():
    

    json_file=open('input_param.json') #open parameter file
    data = json.load(json_file) #load everyting into dictionary called 'data'
    json_file.close() #close the parameter file


    #This code has been taken from the following website:
    #http://www.ariel.com.au/a/python-point-int-poly.html
    poly=[(883,853),(840,915),(840,1166),(883,1240),(1145,1240),(1175,1166),(1175,915),(1145,853)] 
    #coordinates of corners of polygon of RoboPol Mask
    
    
    
    hori=[(60,915),(60,1166),(1190,915),(1990,1166)] #Horizontal Box Coordinates
    vert=[(883,60),(1145,60),(883,1990),(1145,1990)] #Vertical Box Coordinates

    #x=457 #test pixel x coordinate
    #y=901 #test pixel y coordinate



    def point_inside_poly(x,y,poly):

        n=len(poly) #total number of corners in polygon

        inside=False

        p1x,p1y=poly[0] #first corner of polygon

        for i in range(n+1):
            p2x,p2y=poly[i % n] #iterating through every corner of polygon

            if y > min(p1y,p2y): #check if it is between the y coordinates of the 2 points
                if y<=max(p1y,p2y):                 
                        if(x<=max(p1x,p2x)): #if so then check if it is to the left of either of the points
                            if(p1y!=p2y): #to avoid division by 0
                                xinters=(y - p1y)*(p2x - p1x)/(p2y - p1y) + p1x #find the x coordinate of interior point
                            if(p1x == p2x) or (x <= xinters): #check for the condition
                                inside=not inside
            p1x,p1y=p2x,p2y

        return(inside)

    def point_near_boundary(x,y):
        near=False
        if(x<=60 or x>=1990 or y<=60 or y>=1990): #if near the boundary make near True
            near=not near

        return(near)

    path=data['extract_stars'][0] #Set the path where you want to store the result text files 

    sorted_path=data['extract_stars'][1] #path from where to read the sorted .txt files 

    for file in os.listdir(sorted_path): #go through all files sorted directory
        
        if file.endswith(".txt") and not file.startswith("coords_"): #the files should only be our original'.txt' files 
            c="" #we reset c each iteration to avoid having a repitition of file names
            d=1 #set a flag d to count how many stars are chosen. 
            
            filepath=os.path.join(sorted_path,file)
            
            f=open(filepath,"r") #open the file in read mode
            lines=f.readlines() #store lines in the file
            
            f.close()

            c="coords_"+file #c will contain the original image name prefixed by "coords_"
            coords=os.path.join(path,c) #coords is the path to the coordinate file with above path
            w=open(coords,"w") #open the file in write mode

            w.truncate(0) #erase any text if present
            
            
            
            r1=-12.3
            r2=-11.8

            for line in lines: #loop through all lines in the original file

                if(d==7): #only if 4 stars have been chosen then exit the loop
                    break
                line=(line.split()) #split the line so that white spaces are eliminated and you get 
                #a list of words for every line
                
                

                mag=float(line[0]) #find magnitude of the star
                

                if r1<=mag and r2>=mag:


                    x,y=float(line[1]),float(line[2]) #store the x and y coordinates
                    if (point_inside_poly(x,y,poly) or point_inside_poly(x,y,hori) or point_inside_poly(x,y,vert) or point_near_boundary(x,y))==False:
                        w.write("%f\t%f\n"%(x,y)) #only if the point is not in the restricted regions write to the file               
                        d+=1 #increment the flag to indicate that you have a star which is not in the restricted regions

                        r1+=0.5
                        r2+=0.5
                
                    
                
            w.close() #close the file   
            
extract_stars()
