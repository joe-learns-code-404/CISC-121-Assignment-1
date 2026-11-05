def solution(A):
    A.sort() # organize array so for loop can search it easier
    min = 1 # ensure that, even when there are negative values in the array, the lowest POSITIVE missing integer can is 1, not 0
    for x in range(len(A)):
        if A[x] == min:
            min += 1 # up the missing integer since the previous was found and redo for loop with new number
    return min # return the final value after searching entire array
