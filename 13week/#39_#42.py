#39 and #42
'''
사용자로부터 양수(숫자)를 입력받아서
0부터 해당 숫자 포함까지 홀수를 출력. 
단, user-defined function를 이용.
'''

num=int(input('num?:'))

def Pr_num(num):
    for i in range (0,num+1):
        if i%2==1:
            print(i,end='  ')
print(Pr_num(num))