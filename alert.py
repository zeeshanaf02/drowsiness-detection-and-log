import pygame

def alert():
    pygame.mixer.music.load('alert.wav')  # Path to your alert sound file
    pygame.mixer.music.play(-1)  # Play the sound indefinitely

def stop_alert():
    pygame.mixer.music.stop()