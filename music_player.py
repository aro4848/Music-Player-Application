import os
import pygame
from tkinter import Tk, filedialog
from tkinter.ttk import Frame, Button, Label, Progressbar, Style


pygame.init()



root = Tk()
root.title("Sophisticated Music Player")

# Function to open and load music file
def open_file():
    filepath = filedialog.askopenfilename(title="Select Music File", filetypes=[("Audio Files", "*.mp3 *.wav")])
    if filepath:
        play_music(filepath)
        update_song_info(filepath)

# Create GUI elements
style = Style()
style.configure("TButton", padding=(0, 5))

open_button = Button(root, text="Open Music File", command=open_file)
open_button.pack(pady=10)

song_title_label = Label(root, text="Song Title:")
song_title_label.pack()

song_artist_label = Label(root, text="Artist:")
song_artist_label.pack()

song_progress = Progressbar(root, orient="horizontal", mode="determinate")
song_progress.pack(fill="x", padx=20, pady=10)

# Create a pygame mixer to handle audio playback
pygame.mixer.init()

def play_music(file):
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    update_song_info(file)
    update_progress()

def pause_music():
    pygame.mixer.music.pause()

def unpause_music():
    pygame.mixer.music.unpause()

def stop_music():
    pygame.mixer.music.stop()
    song_progress["value"] = 0

def update_progress():
    song_duration = pygame.mixer.Sound(file).get_length()
    progress_interval = int(song_duration) * 1000  # Update every second

    def update():
        current_time = pygame.mixer.music.get_pos() / 1000
        song_progress["value"] = (current_time / song_duration) * 100
        root.after(progress_interval, update)

    update()


def update_song_info(file):
    song = pygame.mixer.Sound(file)
    tags = song.get_tags()

    title = tags.get("title", "Unknown Title")
    artist = tags.get("artist", "Unknown Artist")

    song_title_label.config(text=f"Song Title: {title}")
    song_artist_label.config(text=f"Artist: {artist}")


play_button = Button(root, text="Play", command=play_music)
play_button.pack(side="left", padx=10)

pause_button = Button(root, text="Pause", command=pause_music)
pause_button.pack(side="left", padx=10)

unpause_button = Button(root, text="Unpause", command=unpause_music)
unpause_button.pack(side="left", padx=10)

stop_button = Button(root, text="Stop", command=stop_music)
stop_button.pack(side="left", padx=10)


root.mainloop()


