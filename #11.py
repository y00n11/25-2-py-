#표준 입력으로 임의의 숫자 5개를 입력받은 후, 리스트로 형변환. 
nums= list(map(int,input("임의 숫자 5개 입력(1):").split()))
print(nums)

#표준 입력으로 임의의 문자 1개를 입력받은 후, 위에서 만든 리스트 끝에 추가
nums2= list(map(int,input("임의 숫자 5개 입력(2):").split()))
nums2.append(int(input("추가할 문자 1개 입력: ")))
print(nums2)