def solution(num):
    count = 0
    while num != 1:
        print(f'num is: {num}')
        if (num % 2 == 0):
            print(f'num before num / 2 operation is: {num}')
            num = num / 2
            print(f'num after num / 2 operation is: {num}')
            count += 1
            print(f'count is incremented to: {count}')
        else:
            print(f'num before num * 3 + 1 operation is: {num}')
            num = num * 3 + 1
            print(f'num after num * 3 + 1 operation is: {num}')
            count += 1
            print(f'count is incremented to: {count}')
            
        if count == 500:
            return -1
    return count

print(solution(6))