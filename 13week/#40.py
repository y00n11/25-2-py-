#40
'''
사용자로부터 숫자를 입력받아서 3의 배수일 때만 출력.
단, user-defined function를 이용.
'''

num=int(input('num?:'))

def Pr_num(num):
    if num%3 ==0:
        print('3의 배수 맞음')
    else:
        print('3의 배수 아님')
Pr_num(num)