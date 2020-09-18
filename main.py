# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 12:51:14 2020

@author: apurv
"""

import os 
from os import listdir
from os.path import isfile, join
import pdfplumber
import pyttsx3

##Setting the current working directory
os.chdir("C://Users//apurv//OneDrive//Documents//Projects//2020//pdf-to-audiofile")

pdf_path = 'pdf_files//'
audio_path = 'audio_files//'

##Getting list of all files in pdf folder
filenames = [f for f in listdir(pdf_path) if isfile(join(pdf_path, f))]

## Setting the voice properties

#initialize the voice engine
engine = pyttsx3.init()

##Choosing voice type
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id) #0 for Male, 1 for Female 

##Choosing voice rate
rate = engine.getProperty('rate')
engine.setProperty('rate', 150)

##Reading all PDF files one by one and saving the audio files for respective files
for f in filenames:
    with pdfplumber.open(r''.join([pdf_path,f])) as pdf:
        text = ''
        for page in pdf.pages:  
            text = text  + str(' ' if page.extract_text() is None else page.extract_text())
        engine.save_to_file(text, "".join([audio_path,f.split('.pdf')[0],'.mp3']))
        engine.runAndWait()

        
