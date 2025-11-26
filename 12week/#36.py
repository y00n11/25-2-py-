#한글 출력 오류로 영문으로 작성합니다

a={100,200,300,400,500}
b={100,200,300,400,500}

if a >= b and a <= b: 
    print('DONGSI')
elif a >= b:
    print('SANGWI')
elif a <= b:
    print('BUBUN')

'''
또는 
if a >= b and a <= b: # a와 b가 완전히 같을 경우
    print('동시')
elif a >= b:
    print('상위')
elif a <= b:
    print('부분')

'''
