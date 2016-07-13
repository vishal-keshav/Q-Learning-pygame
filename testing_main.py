import os
import pygame as pg
from text_log import *
"""Utility functons"""
def maxim(a,b):
    if a > b:
        return a
    else:
        return b

def minim(a,b):
    if a < b:
        return a
    else:
        return b


"""Event handler"""
def handle_event(event, pg, x, y):
    if event.type == pg.KEYDOWN:
        if event.key == pg.K_LEFT:
            x = x - 50
        if event.key == pg.K_RIGHT:
            x = x + 50
        if event.key == pg.K_UP:
            y = y - 50
        if event.key == pg.K_DOWN:
            y = y + 50
    if event.type == pg.MOUSEMOTION:
        (x,y) = event.pos
        (x,y) = (x-50,y-50)

    #check if object does not cross boundry
    x = maxim(x,0)
    x = minim(x,500)
    y = maxim(y,0)
    y = minim(y,500)
    return (x,y)
        

"""Draw function"""
def draw(obj,disp,x_pos,y_pos):
    disp.blit(obj,(x_pos,y_pos))

""" Setting import variables which has to be utilized
in initialized game window"""
pg.init()
"""Set windows property"""
disp_height = 600
disp_width = 600
disp_dim = (disp_height,disp_width)
#Background in RGB
bg_color = (255,255,255)

disp = pg.display.set_mode(disp_dim)
pg.display.set_caption('RAPIDO')

"""Clock controls fps"""
clk = pg.time.Clock()

"""Objects on window"""
path = os.path.join("resources", "ball1.jpg")
ball_image = pg.image.load(path)
ball_y = 0.7*disp_height
ball_x = 0.45*disp_width

"""Game loop"""
abort = False
while not abort:
    #Capture all events
    for event in pg.event.get():
        if event.type == pg.QUIT:
            abort = True
        #print(event)
        """Handling differnet events"""
        (ball_x,ball_y) = handle_event(event,pg,ball_x,ball_y)
        
    #update the game window, set fps
    disp.fill(bg_color)
    log = "pos_x: " + str(ball_x) + ", pos_y: " + str(ball_y) 
    display_msg(log, pg, disp)
    draw(ball_image,disp,ball_x,ball_y)
    pg.display.update()
    clk.tick(30)

""" We have come out of game logic loop"""
pg.quit()
quit()
