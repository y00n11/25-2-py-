#44
'''
사용자로부터  2 이상 9 이하의 양수(숫자) 2개(i, j) 를 입력받아서
이중반복문을 돌면서 i와 j의 곱이 30 이상인 경우의 총 합을 출력. 
단 user-defined function를 이용.
'''

i=int(input('num 1(2~9 random):'))
j=int(input('num 2(2~9 random):'))

def sum_ij(i,j):
    result=0
    #2부터 시작 고정
    for x in range(2,i+1):
        for xx in range(2, j+1):
            if x*xx >=30:
                result += x*xx
    return result
print('30 up:', sum_ij(i,j))