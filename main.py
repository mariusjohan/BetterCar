import pygame as pyg
import os
import random

# Settings for the program
fps = 60

pyg.init()

def load():
    global screen, track
    display_size = [1920, 1080]

    screen = pyg.display.set_mode(display_size, flags=pyg.SCALED, vsync=1)
    
    # Load og skaler billedet 'track1.png' til skærmens størrelse
    track = pyg.image.load(os.path.join('tracks', 'track1.png')).convert_alpha()
    track = pyg.transform.scale(track, display_size)    

if __name__ == "__main__":
    running = True
    clock = pyg.time.Clock()
    while running:
        clock.tick(fps)

        # Event listener...
        for event in pyg.event.get():
            if event.type == pyg.QUIT: # User closed the window
                running = False # Stop the loop

        pyg.display.update() #update entire screen