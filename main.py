from tkinter import *
from tkinter import filedialog
import pygame
import os

#Creation of a window
root=Tk()
root.title('Music Player')
root.geometry('500x300')

pygame.mixer.init()

menubar=Menu(root)
root.config(menu=menubar)

songs=[]
current_song=''
paused=False
playVisible=[True]
pauseVisible=[False]

def loadMusic():
    global current_song
    root.directory=filedialog.askdirectory()

    songs.clear()
    songList.delete(0,END)

    for song in os.listdir(root.directory):
        name, ext=os.path.splitext(song)
        if ext=='.mp3':
            songs.append(os.path.join(root.directory,song))

    for song in songs:
        songList.insert(END,os.path.basename(song))
    
    if songs:  
        songList.selection_set(0)
        current_song = songs[0] 

def updateBtn():
    if playVisible[0]:
        pauseBtnn.pack_forget()
        prevBtnn.pack_forget()
        nextBtnn.pack_forget()
        
        prevBtnn.pack(side=LEFT,expand=False,padx=10,pady=5)
        playBtnn.pack(side=LEFT,expand=False,padx=10,pady=5)
        nextBtnn.pack(side=LEFT,expand=False,padx=10,pady=5)
    else:
        playBtnn.pack_forget()
        prevBtnn.pack_forget()
        nextBtnn.pack_forget()

        prevBtnn.pack(side=LEFT,expand=False,padx=10,pady=5)
        pauseBtnn.pack(side=LEFT,expand=False,padx=10,pady=5)
        nextBtnn.pack(side=LEFT,expand=False,padx=10,pady=5)

def playMusic():
    global current_song,paused
    pauseVisible[0]=True
    playVisible[0]=False
    updateBtn()

    if songs: 
        if paused:
            pygame.mixer.music.unpause()
            paused=False
        else:
            try:
                current_song=songs[songList.curselection()[0]]
            except IndexError:
                songList.selection_set(0)
                current_song=songs[0]

            pygame.mixer.music.load(current_song)
            pygame.mixer.music.play()
        

def pauseMusic():
    global paused
    pauseVisible[0]=False
    playVisible[0]=True
    updateBtn()

    pygame.mixer.music.pause()
    paused=True

def nextMusic():
    global current_song,paused
    updateBtn()

    if songs:
        index=(songs.index(current_song)+1)%len(songs)
        songList.select_clear(0,END)
        songList.selection_set(index)
        current_song=songs[index]
        paused=False
        playMusic()

def prevMusic():
    global current_song,paused
    updateBtn()

    if songs:
        index=(songs.index(current_song)-1)%len(songs)
        songList.select_clear(0,END)
        songList.selection_set(index)
        current_song=songs[index]
        paused=False
        playMusic()

def volUp():
    pass

def volDown():
    pass

organizeMenu=Menu(menubar,tearoff=False)
organizeMenu.add_command(label='Select Folder',command=loadMusic)
menubar.add_cascade(label='Organise', menu=organizeMenu)

#UI of list of songs
songList=Listbox(root,bg="black",fg='white',width='100',height=15)
songList.pack(fill=BOTH, expand=True)


#importing Button images
playBtn=PhotoImage(file='PYTHON/MusicPlayer/images/play.png')
pauseBtn=PhotoImage(file='PYTHON/MusicPlayer/images/pause.png')
nextBtn=PhotoImage(file='PYTHON/MusicPlayer/images/next.png')
prevBtn=PhotoImage(file='PYTHON/MusicPlayer/images/previous.png')
#volUpBtn=PhotoImage(file='images/volup.png')
#volDownBtn=PhotoImage(file='images/voldown.png')

contFrame=Frame(root)
contFrame.pack(pady=10)

btnContainer=Frame(contFrame)
btnContainer.pack(anchor='center')

playBtnn=Button(contFrame,image=playBtn,borderwidth=0,command=playMusic)
pauseBtnn=Button(contFrame,image=pauseBtn,borderwidth=0,command=pauseMusic)
nextBtnn=Button(contFrame,image=nextBtn,borderwidth=0,command=nextMusic)
prevBtnn=Button(contFrame,image=prevBtn,borderwidth=0,command=prevMusic)

prevBtnn.pack(side=LEFT,expand=False,padx=10,pady=5)
playBtnn.pack(side=LEFT,expand=False,padx=10,pady=5)
nextBtnn.pack(side=LEFT,expand=False,padx=10,pady=5)




root.mainloop()

