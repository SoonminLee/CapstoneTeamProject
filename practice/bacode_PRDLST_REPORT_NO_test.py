import pandas as pd
import requests
from bs4 import BeautifulSoup
import re

a = open('C:\PythonWorkSpace\qr_barcode_data.txt', 'r')
Barcode_num = a.read().strip() 
print(Barcode_num)

apikey = '14adc49a10ff4df2a831'
startRow = '1'
endRow = '5'
BAR_CD = Barcode_num
keyId = 'I2570'


url = 'http://openapi.foodsafetykorea.go.kr/api/' + apikey + '/' + keyId + '/xml/' + str(startRow) + '/' + str(endRow) + '/BRCD_NO=' + BAR_CD
print(url)

def parse():
    try:
        PRDLST_REPORT_NO = item.find("PRDLST_REPORT_NO").get_text()
        
        return {
            PRDLST_REPORT_NO
        }
    except AttributeError as e:
        return {
            None
        }
#
result = requests.get(url)
soup = BeautifulSoup(result.content, 'lxml-xml')
items = soup.find_all("I2570")
print(items)

# 파싱한 내용에서 품목보고번호만 추출
row = []
for item in items:
  row.append(parse())

# 숫자만 추출
# str1 = str(row)
# reg = int(''.join(list(filter(str.isdigit, str1))))
# print(reg)
# 숫자만 추출

string = str(row)
numbers = re.sub(r'[^0-9]', '', string)
print(numbers)

# 추출된 숫자를 txt에 저장
f = open("Prdlst_Report_Number.txt", "w", encoding="utf8")
f.write(str(numbers))
f.close()