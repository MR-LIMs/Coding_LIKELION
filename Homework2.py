weight_kg=float(input('몸무게(kg)를 입력하세요: '))
height_m=float(input('키(m)를 입력하세요: '))

bmi=weight_kg/(height_m**2)

if bmi <= 18.5:
    print('저체중')
elif 18.5 < bmi <= 23:
    print('정상체중')
elif 23 < bmi <= 25:
    print('과체중')
elif 24 < bmi <= 30:
    print('비만')
elif 30 < bmi:
    print('고도비만')
