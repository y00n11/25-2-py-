#표준 입력으로 물품 가격 여러 개가 문자열 한 줄로 입력되고, 각 가격은 ;(세미콜론)으로 구분되어 있음


prices_input = input()
prices = list(map(int, prices_input.split(';')))
prices.sort(reverse=True)

for price in prices:
    print(str(price).rjust(9))