#45
'''
a = [1, 2, 3, 4, 5] 리스트를 함수의 입력으로 받아서 
리스트 값의 누적 합을 출력. 
단 user-defined function를 이용.
'''

#사용자 입력 x 함수 입력 o
a = [1, 2, 3, 4, 5]

def A(a):
    result=0
    for i in a:
        result+=i
    return result

print('sum a:', A(a))

