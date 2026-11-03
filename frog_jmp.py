# import math library to use math.ceil()
import math

def solution(X, Y, D):
    # check that you won't divide by 0
    if X == Y or D == 0:
        return 0
    else:
        distance = Y - X # get distance left to travel
        return math.ceil(distance / D) # round UP to nearest positve integer
