def solution(x):
    myStr = list(str(x)) #10 -> ['1', '0']
    myNum = x 
    myNum2 = 0
    for i in range(len(myStr)): 
        myNum2 += int(myStr[i])
    return myNum % myNum2 == 0


    print(solution(10)) #True
    print(solution(12)) #True
    print(solution(13)) # False