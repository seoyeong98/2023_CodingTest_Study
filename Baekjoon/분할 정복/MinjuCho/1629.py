import  sys
input = sys.stdin.readline
A, B, C = map(int, input().split())

def multiply(A, N):
    if N == 1:
        return A % C
    else:
        result = multiply(A, N // 2)
        if N % 2 == 0:
            return (result * result) % C
        else:
            return (result * result * A) % C

print(multiply(A, B))


# 틀린 풀이
import  sys
input = sys.stdin.readline
A, B, C = map(int, input().split())

def multiply(A, N):
    if N == 1:
        return A % C
    else:
        half = N // 2
        if N % 2 == 0:
            result = multiply(A, half)
        else:
            result = multiply(A, half) * A
        return result * result % C

print(multiply(A, B))
