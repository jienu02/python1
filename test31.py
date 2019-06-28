##p.207 컴프리헨션

print("#1")
numList = []

print("이거를")

for num in range(1,6):
    numList.append(num)
print(numList)


print("이렇게")


numList = [num for num in range(1, 6)]
print(numList)


##p.209 페이지복사
##같은 메모리를 공유

print("")
print("#2")

oldList = ['짜장면', '탕수육', '군만두']
newList = []
newList = oldList
print(newList)
oldList[0] = '짬뽕'
oldList.append('깐풍기')

print(newList)

##p.210 페이지복사
##다른 메모리 사용 [:]

print("")
print("#3")

oldList = ['짜장면', '탕수육', '군만두']
newList = []
newList = oldList[:]

print(newList)
print(oldList)

oldList[0] = '짬뽕'
oldList.append('깐풍기')

print(newList)
print(oldList)
