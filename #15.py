#표준 입력으로 임의의 숫자 10개를 입력받은 후, list로 형변환 후 최저값과 최고값을 구함

nums=list(map(int,input("임의 숫자 10개 입력:").split()))
print("최저값:",min(nums))
print("최고값:",max(nums))
