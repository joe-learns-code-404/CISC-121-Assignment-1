# A is the array that a user can assign to the function
# K is the amount of times that the user wants to rotate the array
def solution(A, K):
    # to check if the array is empty or not
    if len(A) == 0:
        return A
    else:
        for x in range(K): # going through the array K amount of times
            hold = A[len(A) - 1] # storing the last value of the array
            A.insert(0, hold) # putting the last element in the array at the front
            A.pop(len(A) - 1) # removing the end value now that it has been 'moved' to the front
        return A # returning the modified array

# testing solution
print(solution([3, 8, 9, 7, 6], 3))
