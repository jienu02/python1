##p.181 리스트 값 늘리기

print("#1")

aa = []

print(aa)
print(len(aa))

aa.append(0)
print(aa)
print(len(aa))

aa.append(0)
print(aa)
print(len(aa))

aa.append(0)
print(aa)
print(len(aa))

aa.append(0)
print(aa)
print(len(aa))


##int형 글자수

print("")
print("#2")

c = 125
print("int 형 글자수 : ", len(str(c)))

##p.i85 리스트 값 출력

print("")
print("#3")

aa = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(aa[0:3])
print(aa[2:4])
print(aa[2:])
print(aa[:2])


##리스트 값 바꾸기
aa = [1, 2, 3, 4, 'A', 'B', 6, 7, 8, 9]


print("")
print("#4")

aa[4:5] = "A", "B"
print(aa)