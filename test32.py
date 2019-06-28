##p.225 문자열

ss = "파이썬최고"
print(ss)

print(ss[0])
print(ss[1:3])
print(ss[3:])
print(ss[1:4])

print("")
ss1 = ss.replace('파이썬', '클라우드')
print(ss1)

tel = '010-4088-0116'
newTel = tel.replace('-', '')
print(newTel)

print("")

ss2 = ss * 3
print(ss2)
print(len(ss2))

ss = "AbCdE1Gh1"

ss1 = ss.upper()
print(ss1)

ss2 = ss.lower()
print(ss2)

ss3 = ss.swapcase()
print(ss3)

ss4 = ss.title()
print(ss4)


if len(ss) > 8:
    print("아이디를 다시 설정하세요.")


ss = " 달려라 하니 "


print(">"+ss.strip()+"<")
