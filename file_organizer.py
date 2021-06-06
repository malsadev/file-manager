#Program Name: automatic file handler
#Purpose : automatically moves file from a designated folder to appropriate directories
#Author : Mustafa Al-Sakkaf
#Date : June 6, 2021

import os
import shutil
import time
from fuzzywuzzy import fuzz #String comparision methods




#returns the key(folder name) whose keywords match best with the file name
def getKey(file, key_words):
    Highest_Ratio = 0
    Best_Key = 'PHY1722'
    for key in key_words:
        ratio = fuzz.token_set_ratio(file, key_words[key])
        if (ratio > Highest_Ratio):
            Highest_Ratio = ratio
            Best_Key = list(key_words.keys())[list(key_words.values()).index(key_words.get(key))]
    
    return Best_Key
    
    
    
    

download_folder_path ='C:\\Users\\Mustafa\\Desktop\\Download Folder' #browser default download folder
courses_directory = 'C:\\Users\\Mustafa\\Desktop\\Courses'
print(os.listdir(download_folder_path))


# this dictionary maps the keywords (values) (substrings of file names) to the corresponding folder which are the keys
key_words = {
    'PHY1722' : 'phyysics, phy', 
    'FLS2581' : 'french, fls' ,
    'MAT1722' : 'mathematics, mat',
    'SEG2900' : 'software, seg' ,
    'ITI1520' : 'information technology, iti' ,
    'ENG1112' : 'english, eng'
    }




while True: #this program will have to run as a background process as long as the student account is logged in
    time.sleep(10)#only runs every x seconds so as to not consume all CPU cycl
    incoming_files = os.listdir(download_folder_path)
       
    for file in incoming_files: # loop to check every file against trigger substring
        print(file)
        corr_folder = getKey(file, key_words)
        shutil.move(download_folder_path + '\\' + file, courses_directory + '\\' + corr_folder) # move file to corresponding folder
        
        
    es




