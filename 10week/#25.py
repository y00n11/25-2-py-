#다음과 같이 표준입력으로 키와 해당 값들을 각각 입력받은 후
# dictionary로 만들고 출력


keys = input().split()  
values = list(map(int, input().split()))  
result = dict(zip(keys, values))

result.pop('alpha')
result.pop('delta')
print(result)