import pandas
from bs4 import BeautifulSoup
import requests


# 식품명으로 영양성분 불러오는 코드
CommerceInfor = {}
namelist = []
sizelist = []
kcallist = []
carbohydratelist = []
proteinlist = []
fatlist = []
saccharidelist = []
natriumlist = []
cholesterollist = []
saturated_fatlist = []
trans_fatlist = []

desc_kor = '가자미'

url = 'http://openapi.foodsafetykorea.go.kr/api/14adc49a10ff4df2a831/I2790/xml/1/5/DESC_KOR='+ desc_kor
result = requests.get(url)
soup = BeautifulSoup(result.content, 'lxml-xml')
# print(url)
name = soup.find_all('DESC_KOR') #음식이름
size = soup.find_all('SERVING_SIZE') #총내용량
kcal = soup.find_all('NUTR_CONT1') # 칼로리
carbohydrate = soup.find_all('NUTR_CONT2') #탄수화물
protein = soup.find_all('NUTR_CONT3') # 단백질
fat = soup.find_all('NUTR_CONT4') # 지방
saccharide = soup.find_all('NUTR_CONT5') #당류
natrium = soup.find_all('NUTR_CONT6') #나트륨
cholesterol = soup.find_all('NUTR_CONT7') #콜레스테롤
saturated_fat = soup.find_all('NUTR_CONT8') # 포화지방
trans_fat = soup.find_all('NUTR_CONT9') #트랜스지방

for code in name:
    namelist.append(code.text)
for code in size:
    sizelist.append(code.text)
for code in kcal:
    kcallist.append(code.text)
for code in carbohydrate:
    carbohydratelist.append(code.text)
for code in protein:
    proteinlist.append(code.text)
for code in fat:
    fatlist.append(code.text)
for code in saccharide:
    saccharidelist.append(code.text)
for code in natrium:
    natriumlist.append(code.text)
for code in cholesterol:
    cholesterollist.append(code.text)
for code in saturated_fat:
    saturated_fatlist.append(code.text)
for code in trans_fat:
    trans_fatlist.append(code.text)

CommerceInfor['음식이름'] = namelist
CommerceInfor['총내용량'] = sizelist
CommerceInfor['칼로리[kcal]'] = kcallist
CommerceInfor['탄수화물[g]'] = carbohydratelist
CommerceInfor['당류[g]'] = saccharidelist
CommerceInfor['단백질[g]'] = proteinlist
CommerceInfor['지방[g]'] = fatlist
CommerceInfor['포화지방[g]'] = saturated_fatlist
CommerceInfor['트랜스지방[g]'] = trans_fatlist
CommerceInfor['콜레스테롤[mg]'] = cholesterollist
CommerceInfor['나트륨[mg]'] = natriumlist

# df = pandas.DataFrame(CommerceInfor)
# duf = df.drop_duplicates(['음식이름'])
# duf.to_excel("Foodname_to_NutritionFacts.xlsx")


df = pandas.DataFrame(CommerceInfor)
duf = df[(df['음식이름'] == desc_kor)]
duf = duf.drop_duplicates(['음식이름'],keep='last')
print(duf)
# duf.to_excel("Foodname_to_NutritionFacts.xlsx")


# df.to_excel("Foodname_to_NutritionFacts1.xlsx")


# 참고 자료 : https://pjs21s.github.io/openapi/