import os, shutil 
from datetime import datetime

filepath = "/Users/alfietorres/Downloads/"      #base file path 
for filename in os.listdir(filepath):           #iterate through each file in the directory

    r = os.stat(filepath+filename)              #look for the file path and the file name
    d = r.st_birthtime                          #look for the time created 
    date=datetime.fromtimestamp(d)              #assign the details to a date variable

    month_directory = filepath+str(date.month)+"-"+str(date.year)      #use the date variable to create a UNIQUE new directory 
    file_being_moved = filepath+filename        #file the path of the file being moved    

    if os.path.isdir(month_directory) :         #check if the directory is created
        print("directory found ... ")
        shutil.move(file_being_moved,month_directory)   #move the file we are iterating on to the directory
    else: 
        print("creating directory ... ")        
        os.mkdir(month_directory)                       #create new directory 
        shutil.move(file_being_moved,month_directory)   #move items in new directory


