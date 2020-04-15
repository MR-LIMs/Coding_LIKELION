multi_table={}
for x in range(1,10):
    table=[]
    for y in range(1,10):
        table.append(x*y)
    multi_table[str(x)+'단']=table

for i in range(1,10):
    print(str(i)+'단:', str(multi_table[str(i)+'단'])[1:-1])
    print(str(i)+'단:', multi_table[str(i)+'단'])


data = [1, 2, 3, 4, 5]
str(data)[1:-1]
print(str(data)[1:-1])


a=[1,2,3,4]
for i in range(0,4):
    print(a[0+i])


#구구단 프로그램
multi_table = {}

for x in range(1,10):
    for y in range(1,10):
        multi_table[str(x)+'x'+str(y)] = x*y

print(multi_table)

x=input('첫번째 숫자를 입력하세요 : ')
y=input('두번째 숫자를 입력하세요 : ')

print(str(x)+'x'+str(y)+':', multi_table[str(x)+'x'+str(y)])

#구구단 1단부터 9단까지 출력
multi_table={}
for x in range(1,10):
    table=[]
    for y in range(1,10):
        table.append(x*y)
    multi_table[str(x)+'단']=table

for i in range(1,10):
    print(str(i)+'단:', multi_table[str(i)+'단'])