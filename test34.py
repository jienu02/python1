##p.257 code 09-07 globar 예약어

##함수 선언 부분##
def func1():
    global a    #이 함수 안에서 a는 전역 변수
    a = 10
    print("func1()에서 a값 %d" % a)

def func2():
    print("func2()에서 a값 %d" % a)

def telcheck(tel):
    if len(tel) == 11:
        return True
    else:
        return False

##함수 변수 선언 변수##
a = 20      #전역변수


##메인 코드 부분##
print(a)
func1()
func2()

result = False
tel1="공일공-4088-0116"
tel2="010-4088-0116"
tel3=input("전화번호를 입력하세요 : ")

tel3=tel3.replace('-','')
result = telcheck(tel3)

if result == True:
    print("전화번호 형식에 맞음")
else:
    print("형식에 맞지 않음")

