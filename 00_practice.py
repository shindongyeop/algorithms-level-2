def solution(num):
    count = 0
    while num != 1:
        if num % 2 == 0:
            num = num / 2
            print(f'num after /2 = {num}')
        else:
            num = (num * 3) + 1
        if count == 500:
            return -1
    return count