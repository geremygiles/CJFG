import pygame
from classes import in_game_assets_and_stats as ighas

pygame.mixer.init()
pygame.mixer.music.stop()
pygame.mixer.music.load("assets/sounds/in_game.ogg")
pygame.mixer.music.play(-1)

def game_time(window, stage_size):
    if stage_size is "small":
        window.blit(ighas.s_stage_render, (0, 0))