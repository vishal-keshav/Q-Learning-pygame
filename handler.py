from utility import *
from MDP import *

"""Event handler"""
def collision(x1,y1,x2,y2):
    if (x1==x2) and (y1==y2):
        return True
    return False

def handle_event(event,pg,x,y):
    if event.type == pg.KEYDOWN:
        if event.key == pg.K_LEFT:
            x = maximum(x-1,0)
        if event.key == pg.K_RIGHT:
            x = minimum(x+1,3)
    return (x,y)

action_output = learn()

def handle_event_agent(ball_type,x,y,b_x):
    return (clamp(b_x + int(action_output[ball_type][x][y][b_x]),0,3),3)
        
