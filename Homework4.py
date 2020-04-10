print("★ 구구단을 출력합니다.")
for y in range(0, 10):
    for x in range(2, 10):
        if y == 0:
            print(str(x)+'단', end='\t'*2)
        else:
            print(x, "X", y, "=", x*y, end='\t')
    print("")  