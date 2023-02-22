from bs4 import BeautifulSoup
import requests

# 입력받은 음식이름이 포함된 식품명 목록을 불러오는 코드
CommerceInfor = {}

text_namelist = []
desc_kor = '가자미'
url = 'http://openapi.foodsafetykorea.go.kr/api/14adc49a10ff4df2a831/I2790/xml/1/5/DESC_KOR='+ desc_kor
result = requests.get(url)
soup = BeautifulSoup(result.content, 'lxml-xml')

name = soup.find_all('DESC_KOR')
# print(name)
for code in name:
    text_namelist.append(code.text)

CommerceInfor['DESC_KOR'] = text_namelist

text_namelist = list(set(text_namelist))
print(text_namelist)


# 참고 자료 : https://pjs21s.github.io/openapi/