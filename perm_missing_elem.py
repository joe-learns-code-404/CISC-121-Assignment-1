# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    A.sort()
    C = 0
    if len(A) == 1:
        if A[0] == 1:
            C = 2
        else:
            C = A[0] - 1
    elif len(A) == 0:
        C = 1
    else:
        for x in range(1, len(A)):
            if A[x] != A[x - 1] + 1:
                C = A[x] - 1
            else:
                if A[0] == 1:
                    C = A[len(A) - 1] + 1
                else:
                    C = 1
    return C
