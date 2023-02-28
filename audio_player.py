import pygame 
import time
from playsound import playsound

song_list = [r"C:\Users\akhil\OneDrive - dsatm.edu.in\Documents\Akhil\Java\music_player\music.mp3",r"C:\Users\akhil\OneDrive - dsatm.edu.in\Documents\Akhil\Java\music_player\TilluAnnaDJPedithe.mp3",r"C:\Users\akhil\OneDrive - dsatm.edu.in\Documents\Akhil\Java\music_player\Jai_Balayya_Mass_Anthem.mp3",r"C:\Users\akhil\OneDrive - dsatm.edu.in\Documents\Akhil\Java\music_player\AbhiTohPartyShuruHuiHaiFULLVIDEOSongKhoobsuratBadshahAastha.mp3",r"C:\Users\akhil\OneDrive - dsatm.edu.in\Documents\Akhil\Java\music_player\BadtameezDil.mp3",r"C:\Users\akhil\OneDrive - dsatm.edu.in\Documents\Akhil\Java\music_player\BadtameezDil.mp3"]
q = []

pygame.mixer.init()

def play():
    pygame.mixer.music.load(q[0])
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy(): 
        a = int(input(menu()))
        if a == 1:
            queue()
        elif a == 2:
            pause()
        elif a==3:
            pygame.mixer.music.unload()
        elif a==4:
            pygame.mixer.music.stop()
            break
    
    q.pop(0)
    try:
        if q[0]!= None:
            play()
    except:
        print("\nThe Queue is Over........")
        time.sleep(2)


def pause(): 
    pygame.mixer.music.pause()
    a = input("Press r to resume: ")
    if a == "r":
        pygame.mixer.music.unpause()


def queue():
    a = int(input(('''\n\n<--------Song-List-------->
1)Swif7 Six Feet Under
2)TilluAnnaDJPedithe
3)Jai Ballaya Mass Anthem
4)Abhi Toh Party Shuru Hui Hai
5)Batameez Dil
6)Kolaveri Di
:''')))
    
    q.append(song_list[a-1])

    

def menu():
    return '''\n\n<----------------MENU---------------->
1)Queue
2)Pause
3)Skip
4)Stop

No input to keep it running

:'''

queue()
play()