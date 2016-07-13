import os
import pygame as pg


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
    #update the game window, set fps
    disp.fill(bg_color)
    draw(ball_image,disp,ball_x,ball_y)
    pg.display.update()
    clk.tick(15)

""" We have come out of game logic loop"""
pg.quit()
quit()
