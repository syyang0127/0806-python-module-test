import examCalculator


s1 = int(input('1과목 점수 :'))
s2 = int(input('1과목 점수 :'))
s3 = int(input('1과목 점수 :'))



print('총점 : ',examCalculator.getTotalScore(s1,s1,s3))
print('평균 : ',examCalculator.getAverageScore(s1,s2,s3))
print('P/F : ',examCalculator.getPassFail(s1,s2,s3))