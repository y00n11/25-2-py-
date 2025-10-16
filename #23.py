#본인의 성을 영어로 입력받은 후, 소문자로 바꾼 후 길이 10을 기준으로 오른쪽 정렬 후 출력

name = input()
result = name.lower().rjust(10)
print(result)