from audioplayer import AudioPlayer
import pygame
import time
from playsound import playsound

song_list = [r"C:\Users\akhil\OneDrive - dsatm.edu.in\Documents\Akhil\Java\music_player\music.mp3",""]
q = []


def load(music_file):
    if music_file == None:
        print("No music to play :(")
        return
    
    pygame.mixer.music.load(music_file)

def play():
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy(): 
        print()
        a = input("Give:") 
        time.sleep(1) 
    
    q[0].pop()
    pygame.mixer.music.load(q[0])

def pause_music(): 
    pygame.mixer.music.pause()

def resume_music():
    pygame.mixer.unpause() 

def queue(i):
    q.append(i)

def menu():
    return '''1)Queue
2)Pause
3)Resume
4)'''

