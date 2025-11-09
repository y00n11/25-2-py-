#표준 입력으로 임의의 숫자 5개를 입력받은 후, enumerate를 이용하여 101번 index부터 5개 값 출력

nums=list(map(int,input("임의 숫자 5개 입력:").split()))
for idx, v in enumerate(nums, start=101):
    print(idx, v)