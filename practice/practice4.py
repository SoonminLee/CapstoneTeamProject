import cv2
import pyzbar.pyzbar as pyzbar
from playsound import playsound
import pandas as pd
import requests
from bs4 import BeautifulSoup
import re  


my_code = "8801043015639"
  # 바코드를 입력 받아 품목보고번호를 검색
BAR_CD = my_code
url = 'http://openapi.foodsafetykorea.go.kr/api/14adc49a10ff4df2a831/I2570/xml/1/5/BRCD_NO=' + BAR_CD
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
result = requests.get(url)
soup = BeautifulSoup(result.content, 'lxml-xml')
items = soup.find_all("I2570")
# 파싱한 내용에서 품목보고번호만 추출
print(url)
row = []
for item in items:
    row.append(parse())
string = str(row)
Produtnumbers = re.sub(r'[^0-9]', '', string)
print(Produtnumbers)

# 품목보고번호를 입력 받아 영양성분을 검색 후 제품명과 영양성분 csv파일로 출력
url = 'http://apis.data.go.kr/B553748/CertImgListService/getCertImgListService'
params ={
'serviceKey' : 'IyQg8I2dXbv8kkUs2Gki35cm64Cu+xaUWkNCsFipH3WWV6/iZD4HHrq4v+ykezvft92l9H5S0zULIYrQonfaUA==',
'prdlstReportNo' : Produtnumbers
 }

def parse():
        try:
          PRODLSTNM = item.find("prdlstNm").get_text()
          nutrient = item.find("nutrient").get_text()
          return {
            "제품명":PRODLSTNM,
            "영양성분":nutrient,
        }
        except AttributeError as e:
          return {
            "제품명":None,
            "영양성분":None
        }

result = requests.get(url, params=params)
soup = BeautifulSoup(result.content, 'lxml-xml')
items = soup.find_all("item")
print(items)

row = []
for item in items:
      row.append(parse())
df = pd.DataFrame(row)
df.to_csv("Testtt.csv",mode='w', encoding="EUC-KR")