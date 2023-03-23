from tkinter import *
import pygame, sys
from pygame.locals import *
from tkinter import filedialog
#from PIL import ImageTk, Image
#import os

pygame.init() 
def openFileSong():
    cancion = filedialog.askopenfilename() 
    print(cancion)
    pygame.mixer.music.load(cancion)
           
def playSong():
    pygame.mixer.music.play()

def stopSong():
    pygame.mixer.music.stop()

def resumeSong():
    pygame.mixer.music.unpause()
    
def pauseSong():
    pygame.mixer.music.pause()
    
def volumenUp():
    levelup=pygame.mixer.music.get_volume() +0.1
    print(levelup)
    pygame.mixer.music.set_volume(levelup)

def volumenDown():
    leveldown=pygame.mixer.music.get_volume() -0.1
    print(leveldown)
    pygame.mixer.music.set_volume(leveldown)

raiz = Tk()
raiz.title("Reproductor")
raiz.geometry("600x400")
raiz.resizable(0,0)
framePrincipal = Frame(raiz, bg="#CC3")
framePrincipal.pack(fill="both", expand=1)

Reproductorr = Label(framePrincipal, text="Reproductor MP3", font=("Arial", 20, "bold"), bg="#000", fg="#fbfbfb")
Reproductorr.place(relx=0.30,rely=0.30)

Reproductorr = Label(framePrincipal, text="SPOTY-CHAFF", font=("Arial", 20, "bold"), bg="#000", fg="#fbfbfb")
Reproductorr.place(relx=0.33,rely=0.20)

botonabrir = Button(framePrincipal, text="Abrir cancion", bg="#222", fg="#fbfbfb", font=("Roboto", 10, "bold"), width=12, height=2, command=openFileSong)
botonabrir.place(relx=0.04, rely=0.5)

bottondale = Button(framePrincipal, text="reproducir", bg="#FF0000", fg="#fbfbfb", font=("Roboto", 10, "bold"), width=12, height=2, command=playSong) 
bottondale.place(relx= 0.22, rely=0.5)

bottonparar = Button(framePrincipal, text="Parar", bg="#222", fg="#fbfbfb", font=("Roboto", 10, "bold"), width=12, height=2, command=stopSong)
bottonparar.place(relx= 0.40, rely=0.5)

bottoncontinuar = Button(framePrincipal, text="Continuar", bg="#FF0000", fg="#fbfbfb", font=("Roboto", 10, "bold"), width=12, height=2, command=resumeSong)
bottoncontinuar.place(relx= 0.58, rely=0.5)

bottonPausa = Button(framePrincipal, text="Pausar", bg="#222", fg="#fbfbfb", font=("Roboto", 10, "bold"), width=12, height=2, command=pauseSong)
bottonPausa.place(relx= 0.76, rely=0.5)

bottonVolumenmas = Button(framePrincipal, text="Volumen +", bg="#222", fg="#fbfbfb", font=("Roboto", 10, "bold"), width=12, height=2, command=volumenUp)
bottonVolumenmas.place(relx= 0.15, rely=0.8)

bottonVolumenbajo = Button(framePrincipal, text="Volumen -", bg="#222", fg="#fbfbfb", font=("Roboto", 10, "bold"), width=12, height=2, command=volumenDown)
bottonVolumenbajo.place(relx= 0.69, rely=0.8)

raiz.mainloop()

