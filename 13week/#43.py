#43
'''
사용자로부터 0보다 크거나 같은 정수 n을 입력받아  
n! (펙토리얼) 계산해서 출력. 
단 user-defined function를 이용.
'''

#재귀함수 버전
num=int(input('num?:'))

def factorial(num):
    if num==0 or num ==1:
        return 1
    else:
        return num*factorial(num-1)

print('n!:', factorial(num))


#whlie 버전
num = int(input('num?: '))

def factorial(num):
    result = 1
    i = 1
    while i <= num:
        result *= i
        i += 1
    return result

print('n!:', factorial(num))
