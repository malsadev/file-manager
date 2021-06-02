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
    'phy1722' : [] , 
    'fls2581' : [] ,
    'mat1722' : [],
    'seg2900' : [] ,
    'iti1520' : [] ,
    'eng1112' : []
    }


print(key_words)
target_file = 'download.jpg' #testing

while True: #this program will have to run as a background process as long as the student account is logged in
    if os.listdir(dump_folder_path).__contains__('download.jpg'):
        print('file found')
        shutil.move(dump_folder_path + '\\download.jpg', dump_folder_path + '\\PHY1722')
        
        
    time.sleep(300)#only runs every 300 seconds so as to not consume all CPU cycles


#def move_file():