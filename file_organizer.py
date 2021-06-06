#Program Name: automatic file mover
#Purpose : automatically moves file from a designated download folder to the most appropriate directory
#Author : Mustafa 


import os
import shutil
import time
from fuzzywuzzy import fuzz #String comparision methods




#returns the key(folder name) whose keywords match best with the file name
def getKey(file, keywords):
    highestRatio = 0
    bestKey = 'PHY1722'
    for key in keywords:
        ratio = fuzz.token_set_ratio(file, keywords[key])
        if (ratio > highestRatio):
            highestRatio = ratio
            bestKey = list(keywords.keys())[list(keywords.values()).index(keywords.get(key))]
    
    return bestKey
    
    
downloadPath ='C:\\Users\\Mustafa\\Desktop\\Download Folder' #browser default download folder
coursesDir = 'C:\\Users\\Mustafa\\Desktop\\Courses'
print(os.listdir(downloadPath))


# this dictionary maps the keywords (values) (substrings of file names) to the corresponding folder which are the keys
keywords = {
    'PHY1722' : 'phyysics, phy', 
    'FLS2581' : 'french, fls' ,
    'MAT1722' : 'mathematics, mat',
    'SEG2900' : 'software, seg' ,
    'ITI1520' : 'information technology, iti' ,
    'ENG1112' : 'english, eng'
    }

while True: #this program will have to run as a background process as long as the student account is logged in
    time.sleep(10)
    incomingFiles = os.listdir(downloadPath)   
    for file in incomingFiles: # loop to check every file against triggering keywords
        corrFolder = getKey(file, keywords)
        shutil.move(downloadPath + '\\' + file, coursesDir + '\\' + corrFolder) # move file to corresponding folder
        
        
    




