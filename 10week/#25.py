keys = input().split()  
values = list(map(int, input().split()))  
result = dict(zip(keys, values))

result.pop('alpha')
result.pop('delta')
print(result)