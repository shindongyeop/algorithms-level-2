def solution(n):
    answer = 0
    array = str(n)
    new = "".join(sorted(array, reverse = True))
    answer = int(new)
    return answer

print(solution(21345))