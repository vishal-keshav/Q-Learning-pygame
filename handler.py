from utility import *

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
