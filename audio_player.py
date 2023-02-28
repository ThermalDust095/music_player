from audioplayer import AudioPlayer


song_list = [r"C:\Users\akhil\OneDrive - dsatm.edu.in\Documents\Akhil\Java\music_player\music.mp3"]
q = []


def play():
    print("Audio Playing....")
    AudioPlayer(q[0]).play(loop=False,block=True)
    q.pop(0)
        

def queue(i):
    q.append(song_list[i-1])
    print(q)

print('''-
1. Swif7 - Six Feet Under
2. 
''')

choice = int(input("which song: "))


queue(choice)
play()