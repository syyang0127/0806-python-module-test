def printAverageScore(*s1):
    #매개 변수의 개수가 정해지지 않았을때 *를 붙인다.

    print(type(s1))
    
    totalScore=0
    cnt = len(s1)
    
    for score in s1:
        totalScore += score
        
    print('총점 :',totalScore, '점')
    print('평점 :',totalScore/cnt, '점')
    print('----------------------------')
    
printAverageScore(80,90,70)
printAverageScore(80,90,70,100)
printAverageScore(80,90,70,95,86)

