##p.67 test4-test7

## *을 1부터 5까지 출력하세요.

print("#1")

for i in range(0, 5):
    for j in range(0, i+1):
        print("*", end="")

    print("")


print("")
print("#3")

a = "*"

for i in range(0, 5):
    print(a)
    a += "*"

print("")


## *을 입력받은 숫자만큼 출력

print("")
print("#2")

a = int(input("숫자를 입력하세요 : "))

for i in range(0, a):
    for j in range(0, i+1):
        print("*", end="")

    print("")




