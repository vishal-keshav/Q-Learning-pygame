"""Log file"""
import pygame as pg

def display_msg(text,pg,disp):
    text_font = pg.font.Font('freesansbold.ttf',16)
    surface = text_font.render(text,True, (0,0,0))
    surface_area = surface.get_rect()
    surface_area.center = (100,20)
    disp.blit(surface,surface_area)

    
