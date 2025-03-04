def solution(absolutes, signs):
    answer = 0
    for i in range(len(absolutes)):
        if signs[i] == True:
           answer += absolutes[i]
        else:
           answer -= absolutes[i]        
    return answer

def solution2(absolutes, signs):
    for i in range(len(absolutes)):
        if signs[i] == False:
            absolutes[i] = -absolutes[i]
    return sum(absolutes)