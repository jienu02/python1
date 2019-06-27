## *을 5부터 1까지 출력하세요.

print("#1")

for i in range(5, 0, -1):
    for j in range(1, i+1):
        print("*", end="")

    print("")


## *을 입력받은 숫자만큼 출력

print("")
print("#2")

a = int(input("숫자를 입력하세요 : "))

for i in range(a, 0, -1):
    for j in range(1, i+1):
        print("*", end="")

    print("")


print("")
print("#3")

for i in range(0,5):
    for j in range(5-i):
        print("*", end="")
    print("")