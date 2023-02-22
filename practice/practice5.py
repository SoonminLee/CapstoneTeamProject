import pandas
from bs4 import BeautifulSoup
import requests

CommerceInfor = {}

namelist = []
bacode = "8801062628476"
url = 'http://openapi.foodsafetykorea.go.kr/api/14adc49a10ff4df2a831/C005/xml/1/5/BAR_CD='+ bacode
result = requests.get(url)
soup = BeautifulSoup(result.content, 'lxml-xml')
print(url)
name = soup.find_all('PRDLST_NM')

for code in name:
    namelist.append(code.text)

CommerceInfor['PRDLST_NM'] = namelist

df = pandas.DataFrame(CommerceInfor)

# df.to_excel("bacode_to_PRDLST_NM.xlsx")
df.to_excel("bababababab.xlsx")

# 참고 자료 : https://pjs21s.github.io/openapi/