import pygame as pg

""" Setting import variables which has to be utilized
in initialized game window"""
pg.init()
disp = pg.display.set_mode((600,600))
pg.display.set_caption('RAPIDO')
clk = pg.time.Clock()

#By default, game is on
abort = False
while not abort:
    #Capture all events
    for event in pg.event.get():
        if event.type == pg.QUIT:
            abort = True
        print(event)
    #update the game window, set fps
    pg.display.update()
    clk.tick(15)

""" We have come out of game logic loop"""
pg.quit()
quit()
