import requests
from bs4 import BeautifulSoup
import pandas as pd

desc_kor = '가자미조림'

url =  'http://openapi.foodsafetykorea.go.kr/api/14adc49a10ff4df2a831/I2790/xml/1/5/DESC_KOR='+ desc_kor


def parse():
    try:
        NUTR_CONT1 = item.find("NUTR_CONT1").get_text()
        NUTR_CONT2 = item.find("NUTR_CONT2").get_text()
        NUTR_CONT3 = item.find("NUTR_CONT3").get_text()
        NUTR_CONT4 = item.find("NUTR_CONT4").get_text()
        NUTR_CONT5 = item.find("NUTR_CONT5").get_text()
        NUTR_CONT6 = item.find("NUTR_CONT6").get_text()
        NUTR_CONT7 = item.find("NUTR_CONT7").get_text()
        NUTR_CONT8 = item.find("NUTR_CONT8").get_text()
        NUTR_CONT9 = item.find("NUTR_CONT9").get_text()
        return {
            "열량(kcal)":NUTR_CONT1,
            "탄수화물(g)":NUTR_CONT2,
            "단백질(g)":NUTR_CONT3,
            "지방(g)":NUTR_CONT4,
            "당류(g)":NUTR_CONT5,
            "나트륨(mg)":NUTR_CONT6,
            "콜레스테롤(mg)":NUTR_CONT7,
            "포화지방(g)":NUTR_CONT8,
            "트랜스지방(g)":NUTR_CONT9
        }
    except AttributeError as e:
        return {
            "열량(kcal)":None,
            "탄수화물(g)":None,
            "단백질(g)":None,
            "지방(g)":None,
            "당류(g)":None,
            "나트륨(mg)":None,
            "콜레스테롤(mg)":None,
            "포화지방(g)":None,
            "트랜스지방(g)":None
        }

result = requests.get(url)
soup = BeautifulSoup(result.content, 'lxml-xml')
items = soup.find_all("I2790")
print(items)

row = []
for item in items:
    row.append(parse())
df = pd.DataFrame(row)
df.to_excel("DESC_KOR_to_NutritionFacts.xlsx")