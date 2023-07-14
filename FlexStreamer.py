'''Enjoy <3 - Viri'''

import subprocess

print("Enter the name of the file you want to stream. Include the file extension.\nExample: lofi.mp4 or image.png or pogchamp.gif")
filename = "image.gif"
with open('stream_keys.txt','r')as keys:
    for key in keys:
        subprocess.Popen(f'ffmpeg -stream_loop -1 -re -i {filename} -stream_loop -1 -i music.mp3 -c:v libx264 -preset veryfast -b:v 3000k -maxrate 3000k -bufsize 6000k -pix_fmt yuv420p -g 50 -c:a aac -b:a 160k -ac 2 -ar 44100 -f flv "rtmp://live.twitch.tv/app/{key}"', shell=True)
        
