import requests
from bs4 import BeautifulSoup
import pandas as pd
# 19690086003422
a = open('C:\PythonWorkSpace\Prdlst_Report_Number.txt', 'r')
prdlst_report_number = a.read().strip() # 품목보고번호 197604870051
print(prdlst_report_number)

url = 'http://apis.data.go.kr/B553748/CertImgListService/getCertImgListService'
params ={
'serviceKey' : 'IyQg8I2dXbv8kkUs2Gki35cm64Cu+xaUWkNCsFipH3WWV6/iZD4HHrq4v+ykezvft92l9H5S0zULIYrQonfaUA==',
'prdlstReportNo' : prdlst_report_number
 }
print(url)

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
df.to_csv("Nutrition_Facts.csv",mode='w', encoding="EUC-KR")