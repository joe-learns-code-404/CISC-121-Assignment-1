def solution(A):
    A.sort() # organize the array so the values are order numerically
    C = 0 # initiallize holder
    if len(A) == 1: # check for short arrays
        if A[0] == 1:
            # if array's single value is 1, then the missing element is 2
            C = 2
        else:
            # if array's single value is NOT 1, then missing element is the value - 1
            C = A[0] - 1
    elif len(A) == 0: # check for EMPTY arrays
        C = 1
    else:
        # loop to search through entire array and compare each value to the previous
        for x in range(1, len(A)):
            # if the numbers are not assending by one, assign the missing element to C
            if A[x] != A[x - 1] + 1:
                C = A[x] - 1
                break # stop loop so C value isn't changed
            else:
                # if the missing element is the last element
                if A[0] == 1:
                    C = A[len(A) - 1] + 1
                # if the array is only two integers long, missing element is the first one
                elif len(A) == 2:
                    C = A[0] - 1
                else:
                    # the default :D
                    C = 1
    return C
