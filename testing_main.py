import os
import pygame as pg
import random
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

"""Block crosses each other"""
def crossover(x1,y1,x2,y2):
    if (y1<y2+100) and (y1+100>y2) and (x1<x2+100) and (x1+100>x2):
        return True
    return False

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
path = os.path.join("resources", "ball2.jpg")
negative_ball = pg.image.load(path)
path = os.path.join("resources", "ball3.jpg")
positive_ball = pg.image.load(path)
ball_y = 0.7*disp_height
ball_x = 0.45*disp_width
nball_x = 0
nball_y = 0
draw_ball = 0
##pball_x = 0
##pball_y = 0
points = 0
bool_draw = True
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
    #log = "pos_x: " + str(ball_x) + ", pos_y: " + str(ball_y)
    log = "points: " + str(points)
    display_msg(log, pg, disp)
    
    if nball_y > 600:
        nball_y = -5
        nball_x = random.randrange(0,500)
        draw_ball = random.randrange(0,2)
        bool_draw = True
    
    nball_y = nball_y + 20
    draw(ball_image,disp,ball_x,ball_y)
    if crossover(ball_x, ball_y, nball_x, nball_y):
        if draw_ball <=0 and bool_draw:
            points = points - 1
            #print(points)
        elif draw_ball >0 and bool_draw:
            points = points + 1
            #print(points)
        bool_draw = False
        
    elif draw_ball <= 0 and bool_draw:
        draw(negative_ball,disp,nball_x,nball_y)
    elif draw_ball > 0 and bool_draw:
        draw(positive_ball,disp,nball_x,nball_y)
    
    pg.display.update()
    clk.tick(45)

""" We have come out of game logic loop"""
pg.quit()
quit()
