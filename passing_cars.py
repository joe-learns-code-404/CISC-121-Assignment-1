# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    count = 0
    for x in range(len(A)):
        if A[x] == 0:
            for y in range(x, len(A)):
                if A[y] == 1:
                    count += 1
    return count
