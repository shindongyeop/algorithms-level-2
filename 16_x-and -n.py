def solution(x, n):
    answer = []
    for i in range (1, n+1):
        Y = x * i
        answer.append(Y)
    return answer