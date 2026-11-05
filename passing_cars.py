def solution(A):
    count = 0
    for x in range(len(A)): # check for cars going east (0 values)
        if A[x] == 0:
            for y in range(x, len(A)): # check for cars going west after the current spot of east travelling cars, so there aren't double counts
                if A[y] == 1:
                    count += 1 # increase count if the cars pass each other
    return count
