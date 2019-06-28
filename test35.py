##p.261 code 09-10


##함수 선언 부분##

import test36

def para3_func(v1, v2, v3):
    result = 0
    result = v1 + v2 + v3
    return result

##전역 변수 선언##
hqp =0

##메인 코드 부분##
hap = test36.para2_func(10, 20)
print("매개변수가 2개인 함수를 호출한 결과 ==> %d" % hap)
hap = para3_func(10, 20, 30)
print("매개변수가 3개인 함수를 호출한 결과 ==> %d" % hap)
