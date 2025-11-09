#표준 입력으로 임의의 숫자 5개를 입력받은 후, 리스트로 형변환한 후 마지막 두 개 값 삭제
nums=list(map(int,input("임의 숫자 5개 입력:").split()))
del nums[-2:]
print(nums)