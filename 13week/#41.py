#41
'''
사용자로부터 숫자 4개를 입력받은 후
최댓값과 최솟값을 계산. 
단 user-defined function를 이용.
함수의 매개변수는 점수 4개를 받고, 최댓값과 최솟값을 리턴.
'''
nums=list(map(int,input('input 4 nums:').split()))

def maxmin_num(n1,n2,n3,n4):
    nums=[n1,n2,n3,n4]
    return max(nums), min(nums)

max_val, min_val=maxmin_num(*nums)
print('최댓값:', max_val, '최소값:', min_val)
