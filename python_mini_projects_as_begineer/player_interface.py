import tkinter as tk
from tkinter import filedialog
import pygame

pygame.mixer.init()


root=tk.Tk()
root.title("Music Player")
root.geometry("400x200")


current_song = ""

def load_song():
    global current_song
    current_song = filedialog.askopenfilename(filetypes=[("MP3 files", "*.mp3")])
    if current_song:
        song_label.config(text="Playing" +current_song.split("/")[-1])
        pygame.mixer.music.load(current_song)
        pygame.mixer.music.play()
def play_song():
    if current_song:
        pygame.mixer.music.unpause()
def pause_song():
    if current_song:
        pygame.mixer.music.pause()
def stop_song():
    if current_song:
        pygame.mixer.music.stop()
        song_label.config(text="no song available")    

# ui elememts
song_label=tk.Label(root,text="no song available",fg="blue")
song_label.pack(pady=10)

load_btn=tk.Button(root,text="Load Song",command=load_song)
load_btn.pack(pady=5)

play_btn=tk.Button(root,text="Play",command=play_song)
play_btn.pack(pady=5)

pause_btn=tk.Button(root,text="Pause",command=pause_song)
pause_btn.pack(pady=5)

stop_btn=tk.Button(root,text="Stop",command=stop_song)
stop_btn.pack(pady=5)

root.mainloop()
