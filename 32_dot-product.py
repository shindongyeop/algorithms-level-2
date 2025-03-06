def solution(a, b):
    answer = []
    n = len(a)
    for i in range(n):
        answer.append(a[i] * b[i])
    return sum(answer)