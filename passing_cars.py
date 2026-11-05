# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    zeros = []
    ones = []
    for x in range(len(A)):
        if A[x] == 0:
            zeros.append(A[x])
        else:
            ones.append(A[x])
    if len(zeros) == 0 or len(ones) == 0:
        return 0
    else:
        return len(zeros) + len(ones)
