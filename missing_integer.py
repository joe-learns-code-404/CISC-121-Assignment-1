# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    A.sort()
    min = 1
    for x in range(len(A)):
        if A[x] == min:
            min += 1
    return min
