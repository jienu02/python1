## 3차 배열 문자 넣기
# [3단][6단][9단][12단]
# [][][][]
# [][][][]
# [][][][]
# [][][][]

list1 = []
list2 = []
list3 = []
value = 0
result = ""

for i in range(0, 5):
    for k in range(0, 4):
        value += 3
        for j in range(0, 9):
            result = "%d x %d = %d  " % (value, j+1, value*(j+1))
            list3.append(result)
        list2.append(list3)
        list3 = []
    list1.append(list2)
    list2 = []

for i in range(0, 5):
    for k in range(0, 4):
        print("%s" % list1[i][k], end="")
    print("")

print(len(list1))