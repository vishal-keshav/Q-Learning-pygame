from resource import *
from handler import *
import random


"""Game loop"""
def start_game():
    abort = False
    x = 0
    y = 0
    b_x = 0
    b_y = 3
    ball_type = 0
    points = 0
    while not abort:
        #Capture all events
        for event in pg.event.get():
            if event.type == pg.QUIT:
                abort = True
            #print(event)
            """Handling differnet events"""
            (b_x,b_y) = handle_event(event,pg,b_x,b_y)
            
        disp.fill(bg_color)
        
        if y > 3:
            y = 0
            x = random.randrange(0,4)
            ball_type = random.randrange(0,2)
        
        draw(neutral_ball,disp,pos_x[b_x],pos_y[b_y])
        if collision(b_x, b_y, x, y):
            if ball_type == 0:
                points = points - 1
                #print(points)
            elif ball_type == 1:
                points = points + 1
                #print(points)
            
        elif ball_type == 0:
            draw(negative_ball,disp,pos_x[x],pos_y[y])
        elif ball_type == 1:
            draw(positive_ball,disp,pos_x[x],pos_y[y])
        y = y+1
        pg.display.update()
        clk.tick(4)

"""Define end game"""
def end_game():
    pg.quit()
    quit()
