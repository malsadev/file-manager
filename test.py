#Program Name: automatic file handler
#Purpose : automatically moves file from a designated folder to appropriate directories
#Author : Mustafa Al-Sakkaf
#Date : June 6, 2021

import os
import shutil

print(os.getcwd()) #get current working directory


dump_folder_path ='C:\\Users\Mustafa\\Desktop\\Download Folder' #browser default download folder

print(os.listdir(dump_folder_path))


# this dictionary maps the certain keywords (part of file names) to the corresponding folder which are the 'keys'
key_words = {
    'phy1722' : [] , 
    'fls' : [] ,
    'mat' : [],
    'seg' : [] ,
    'iti' : [] ,
    'eng' : []}


print(key_words)
target_file = 'download.jpg' 

if os.listdir(dump_folder_path).__contains__('Download.jpg'):
    print('file found')
    shutil.move(dump_folder_path + '\\download.jpg', dump_folder_path + '\\PHY1722')



#def move_file():