# import math library
import math

def solution(X, Y, D):
    # Y divided by D will show how many jumps are required of the frog to complete its path
    jumps = math.ceil(Y / D) # round up decimal to nearest whole number
    return jumps
