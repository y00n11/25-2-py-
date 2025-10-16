#list comprehension을 이용하여 1부터 20까지 중 홀수 출력

nums= [ i for i in range(1,21) if i%2 ==1]
print(nums)

'''
또는 range(1,21,2)
'''