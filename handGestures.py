import cv2 as cv
import mediapipe as mp


def pressSpace(handPos,handedness):
    # Retrieve coordinates using .get() to avoid KeyError
    x8, y8 = handPos.get(8, (0, 0))
    x6, y6 = handPos.get(6, (0, 0))
    x12, y12 = handPos.get(12, (0, 0))
    x10, y10 = handPos.get(10, (0, 0))
    x16, y16 = handPos.get(16, (0, 0))
    x14, y14 = handPos.get(14, (0, 0))
    x20, y20 = handPos.get(20, (0, 0))
    x18, y18 = handPos.get(18, (0, 0))
    x4,y4 = handPos.get(4, (0, 0))
    x1,y1 = handPos.get(1, (0, 0))
    flag=False
    if handedness == 'Right' and x4>x1: flag=True
    elif handedness == 'Left' and x1>x4: flag=True
    # Check if the thumb and other landmarks meet the conditions
    if y8 > y6 and y12 > y10 and y16 > y14 and y20 > y18 and flag:
        return True
    return False
def pressRight(handPos,handedness):
    if handedness == 'Left':
        x8, y8 = handPos.get(8, (0, 0))
        x6, y6 = handPos.get(6, (0, 0))
        x12, y12 = handPos.get(12, (0, 0))
        x10, y10 = handPos.get(10, (0, 0))
        x16, y16 = handPos.get(16, (0, 0))
        x14, y14 = handPos.get(14, (0, 0))
        x20, y20 = handPos.get(20, (0, 0))
        x18, y18 = handPos.get(18, (0, 0))
        x4,y4 = handPos.get(4, (0, 0)) #thumbtip
        x5,y5 = handPos.get(5, (0, 0))
        if y8 > y6 and y12 > y10 and y16 > y14 and y20 > y18 and x4>x5:
            return True
    else : return False

def pressLeft(handPos,handedness):
    if handedness == 'Right':
        x8, y8 = handPos.get(8, (0, 0))
        x6, y6 = handPos.get(6, (0, 0))
        x12, y12 = handPos.get(12, (0, 0))
        x10, y10 = handPos.get(10, (0, 0))
        x16, y16 = handPos.get(16, (0, 0))
        x14, y14 = handPos.get(14, (0, 0))
        x20, y20 = handPos.get(20, (0, 0))
        x18, y18 = handPos.get(18, (0, 0))
        x4,y4 = handPos.get(4, (0, 0)) #thumbtip
        x5,y5 = handPos.get(5, (0, 0))
        if y8 > y6 and y12 > y10 and y16 > y14 and y20 > y18 and x4<x5:
            return True
    else : return False

def pressUp(handPos,handedness):
    if handedness == 'Right':
        x8, y8 = handPos.get(8, (0, 0))
        x6, y6 = handPos.get(6, (0, 0))
        x12, y12 = handPos.get(12, (0, 0))
        x10, y10 = handPos.get(10, (0, 0))
        x16, y16 = handPos.get(16, (0, 0))
        x14, y14 = handPos.get(14, (0, 0))
        x20, y20 = handPos.get(20, (0, 0))
        x18, y18 = handPos.get(18, (0, 0))
        x4, y4 = handPos.get(4, (0, 0))
        x1, y1 = handPos.get(1, (0, 0))
        if y8 < y6 and y12 > y10 and y16 > y14 and y20 > y18 and x4<x1: return True
    return False
def pressDown(handPos,handedness):
    if handedness == 'Left':
        x8, y8 = handPos.get(8, (0, 0))
        x6, y6 = handPos.get(6, (0, 0))
        x12, y12 = handPos.get(12, (0, 0))
        x10, y10 = handPos.get(10, (0, 0))
        x16, y16 = handPos.get(16, (0, 0))
        x14, y14 = handPos.get(14, (0, 0))
        x20, y20 = handPos.get(20, (0, 0))
        x18, y18 = handPos.get(18, (0, 0))
        x4, y4 = handPos.get(4, (0, 0))
        x1, y1 = handPos.get(1, (0, 0))
        if y8 < y6 and y12 > y10 and y16 > y14 and y20 > y18 and x4>x1: return True
    return False