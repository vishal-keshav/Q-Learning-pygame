import os
import pygame as pg

"""Define resources and its parameters"""
window_height = 400
window_width = 400
window_dim = (window_height,window_width)

bg_color = (255,255,255)

object_height = 100
object_width = 100

#intialize window
pg.init()
disp = pg.display.set_mode(window_dim)
pg.display.set_caption('ABOT')

clk = pg.time.Clock()

path = os.path.join("resources", "ball1.jpg")
neutral_ball = pg.image.load(path)
path = os.path.join("resources", "ball2.jpg")
negative_ball = pg.image.load(path)
path = os.path.join("resources", "ball3.jpg")
positive_ball = pg.image.load(path)

pos_x = [0,100,200,300]
pos_y = [0,100,200,300]

def draw(obj,disp,x_pos,y_pos):
    disp.blit(obj,(x_pos,y_pos))

