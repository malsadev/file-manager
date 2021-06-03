#Program Name: automatic file handler
#Purpose : automatically moves file from a designated folder to appropriate directories
#Author : Mustafa Al-Sakkaf
#Date : June 6, 2021

import os
import shutil
import time



print(os.getcwd()) #get current working directory


dump_folder_path ='C:\\Users\Mustafa\\Desktop\\Download Folder' #browser default download folder

print(os.listdir(dump_folder_path))


# this dictionary maps the certain keywords (part of file names) to the corresponding folder which are the 'keys'
key_words = {
    'Phy1722' : ['physics.jpg', 'download.jpg', 'download1.jpg'] , 
    'fls2581' : ['french'] ,
    'mat1722' : ['mathematics'],
    'seg2900' : ['seg'] ,
    'iti1520' : ['information technology'] ,
    'eng1112' : ['english']
    }

print('l' in 'download.jpg')

print(key_words['Phy1722'])

target_file = 'download.jpg' #testing

while True: #this program will have to run as a background process as long as the student account is logged in
    incoming_files= os.listdir(dump_folder_path)
    
    for key in key_words:
        
        for key_word in key_words[key]: #goes through the list of key words associated with each key
            if incoming_files.__contains__(key_word):
                print('file found')
                shutil.move(dump_folder_path + '\\' + key_word, dump_folder_path + '\\PHY1722')
                
        
    time.sleep(3)#only runs every 3 seconds so as to not consume all CPU cycles


#def move_file():