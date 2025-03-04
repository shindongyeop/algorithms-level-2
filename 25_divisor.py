def solution(arr, divisor):
    answer = []
    for i in range(len(arr)):
        print(f'i is: {i}')
        if arr[i] % divisor == 0:
            answer.append(arr[i])
            print(f'answer is: {answer}')
    if len(answer) == 0:
        return [-1]
    else:
        return sorted(answer)
        
print(solution([5,9,7,10], 5))

def solution(arr, divisor):
    answer = []
    for i in range(len(arr)):
        print(f'i is: {i}')
        if arr[i] % divisor == 0:
            answer.append(arr[i])
            print(f'answer is: {answer}')
    if len(answer) > 0:
        return sorted(answer)
    else:
        return [-1]