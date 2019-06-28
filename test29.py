##p.204 code 07-09

print("#1")

import operator

trainDic, trainList = {}, []

trainDic = {'Thomas':'토마스', 'Edward':'에드워드', 'Henry':'헨리','Gothon':'고든', 'James':'제임스'}
trainList = sorted(trainDic.items(), key = operator.itemgetter(0))

print(trainList)



##p.204 code 07-10

print("")
print("#2")

foods = {"떡볶이": "오뎅", "짜장면": "단무지", "라면": "김치", "피자": "피클", "맥주": "땅콩", "치킨": "치킨무", "삼겹살": "상추"}

while True:
    myfood = input(str(list(foods.keys()))+" 중 좋아하는 음식은?")
    if myfood in foods:
        print("<%s> 궁합 음식은 <%s>입니다." % (myfood, foods.get(myfood)))
    elif myfood == "끝":
        break
    else:
        print("그런 음식이 없습니다. 확인해 보세요.")