import pygame as pyg
import os
import random

# Settings for the program
fps = 60
screen = None

pyg.init()

if __name__ == "__main__":
    running = True
    clock = pyg.time.Clock()
    while running:
        clock.tick(fps)

        # Event listener...
        for event in pyg.event.get():
            if event.type == pyg.QUIT:  # User closed the window
                running = False  # Stop the loop

        pyg.display.update()  # update entire screen
