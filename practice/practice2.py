import pandas
from bs4 import BeautifulSoup
import requests

CommerceInfor = {}

namelist = []
desc_kor = '크런키'
url = 'http://openapi.foodsafetykorea.go.kr/api/14adc49a10ff4df2a831/I2790/xml/1/5/DESC_KOR='+ desc_kor
result = requests.get(url)
soup = BeautifulSoup(result.content, 'lxml-xml')

name = soup.find_all('DESC_KOR')

for code in name:
    namelist.append(code.text)

CommerceInfor['DESC_KOR'] = namelist

df = pandas.DataFrame(CommerceInfor)

df.to_excel("ssssss.xlsx")


# 참고 자료 : https://pjs21s.github.io/openapi/