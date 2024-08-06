def convertUnit(lenMm):
    unitDic = {}
    unitDic['cm'] = lenMm * 0.1
    unitDic['m'] = lenMm * 0.001
    unitDic['inch'] = lenMm * 0.03937
    unitDic['ft'] = lenMm * 0.003281
    
    #print(unitDic)

    return unitDic

def printLength(originalData, lengths):
    for len in lengths.keys():
        print(originalData,'mm-->',lengths[len],len)
                                  #->딕셔너리의 key값

# unitDic가 key:value 를 리턴 받음