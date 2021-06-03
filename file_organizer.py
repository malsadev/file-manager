#Program Name: automatic file handler
#Purpose : automatically moves file from a designated folder to appropriate directories
#Author : Mustafa Al-Sakkaf
#Date : June 6, 2021

import os
import shutil
import time





#resources:
#https://stackoverflow.com/questions/8023306/get-key-by-value-in-dictionary




dump_folder_path ='C:\\Users\Mustafa\\Desktop\\Download Folder' #browser default download folder

print(os.listdir(dump_folder_path))


# this dictionary maps the certain keywords (part of file names) to the corresponding folder which are the 'keys'
key_words = {
    'PHY1722' : 'oad', 
    'fls2581' : 'french' ,
    'mat1722' : 'mathematics',
    'seg2900' : 'software' ,
    'iti1520' : 'information technology' ,
    'eng1112' : 'english'
    }



p = dict(zip(key_words.values(),key_words.keys()))
print(p)
while True: #this program will have to run as a background process as long as the student account is logged in
    incoming_files = os.listdir(dump_folder_path)
    
    for key in key_words:
        
        for trigger_substring in key_words[key]: #goes through the list of key words associated with each key
            
            for file in incoming_files: # loop to check every file against trigger substring
                if trigger_substring in file:
                    print(trigger_substring)
                    print(file + ' found. Moving to correct folder')
                    corr_folder = p[trigger_substring]
                    shutil.move(dump_folder_path + '\\' + file, dump_folder_path + '\\' + corr_folder) # move file to corresponding folder
                    
        
    time.sleep(10)#only runs every x seconds so as to not consume all CPU cycles


#def move_file()


