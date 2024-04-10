
from pytube import YouTube, Channel
from pytube.cli import on_progress
import os 

# Python code to
# demonstrate readlines()
"""
L = ["Geeks\n", "for\n", "Geeks\n"]
 
# writing to file
file1 = open('myfile.txt', 'w')
file1.writelines(L)
file1.close()
""" 
# Using readlines()
file1 = open('listaVideos4.txt', 'r')
Lines = file1.readlines()
 
count = 0
# Strips the newline character
for line in Lines:
    count += 1
    print("Line{}: {}".format(count, line.strip()))
    video = YouTube(line)
    try:
        yt = YouTube(line, on_progress_callback=on_progress)
        

        #video = yt.streams.filter(only_audio=True).first() 
        stream = yt.streams.filter(only_audio=True).first() 
        #video = yt.streams.filter(only_audio = True).first()
        print(yt.title + " audio extraido .")
        destination = '.'
        out_file = stream.download(output_path = destination)
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)
        print(yt.title + " has been successfully downloaded.")
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
    # Choose a higher-resolution mp4 by default
   
    # Download stream...
    
    #stream.download()
