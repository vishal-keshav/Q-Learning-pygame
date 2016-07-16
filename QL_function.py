from utility import *
"""State is represented by four tuple [ball_type,ball_x,ball_y,nball_x]
    ball_type = {0:negative ball, 1:positive ball}
    ball_x = [0,1,2,3] x-coordinate of ball_type ball
    ball_y = [0,1,2,3] y-coordinate of ball_type ball
    nball_y = [0,1,2,3] y-coordinate of neutral ball, x-coordinate is fixed"""

"""Action is represnted by one digit
    -1 : move left
    0  : stay at the same place
    +1 : move right """

"""ball_type is represented by a digit
    -1 : negative ball
    +1 : positive ball"""

"""State transition function takes current state and action as input
    output is set of reachable states"""
def state_transition(state,action):
    #if new ball_type ball is being generated
    output_state = []
    nball_x = state[3]
    if state[2] == 3:
        ball_y= 0
        nball_x = clamp(nball_x + action,0,3)
        for ball_x in range(0,4):
            for ball_type in range(-1,2,2):
                output_state.append((ball_type,ball_x,ball_y,nball_x))
    else:
        ball_y = state[2]+1
        nball_x = clamp(nball_x + action,0,3)
        ball_x = state[1]
        ball_type = state[0]
        output_state.append((ball_type,ball_x,ball_y,nball_x))
    return output_state

"""Reward of being in certain state is evaluated by balls coordinate
    and ball_type"""
def reward(state):
    if state[2] == 3 and state[1] == state[3]:
        #ball_type itself defines the reward
        return state[0]
    else:
        return 0

"""Transition probability defines the chaces of ending up in a state
    if certain action is taken on a certain state"""
def transition_probability(current_state,action,next_state):
    """if ball is in last row, then any move leading to some state
        will be uniform as random number generator utilized is uniform
        in nature"""
##  Commented code runs faster
##    if current_state[2] == 3:
##        return (1/8)
##    else:
##        if next_state[0] == state_transition(current_state,action):
##            return 1
##        else:
##            return 0
    possible_states = state_transition(current_state,action)
    if next_state in possible_states:
        probability =  1.0/len(possible_states)
    else:
        probability = 0
    return probability

"""Testing for different test cases"""
##print(state_transition((-1,0,1,3),+1))
##print(state_transition((+1,2,0,2),-1))
##print(state_transition((+1,0,3,0),-1))
##print(state_transition((-1,1,3,1),0))
##print (transition_probability((-1,0,1,3),+1,(-1,0,2,3)))
##print (transition_probability((-1,0,1,3),+1,(-1,1,1,3)))
##print (transition_probability((-1,0,1,3),+1,(-1,0,2,2)))
##print (transition_probability((+1,1,3,1),0,(-1,3,0,1)))
##print (transition_probability((+1,1,3,1),0,(-1,3,2,1)))
##print (transition_probability((+1,1,3,1),-1,(-1,1,0,0)))
##print (reward((-1,0,1,3)))
##print (reward((+1,1,3,1)))
