import pandas
from bs4 import BeautifulSoup
import requests
import cv2
from playsound import playsound
import pyzbar.pyzbar as pyzbar


# 바코드를 영양성분표로
def barcode_to_foodname():
    # 카메라로 바코드를 추출
    a = 0
    used_codes = []
    data_list = []

    try:
        f = open("qr_barcode_data.txt", "r", encoding="utf8")
        data_list = f.readlines()
    except FileNotFoundError:
        pass
    else:
        f.close()

    cap = cv2.VideoCapture(0)
    cap.set(3, 640)
    cap.set(4, 480)

    for i in data_list:
        used_codes.append(i.rstrip('\n'))

    while a == 0:
        success, frame = cap.read()
        for code in pyzbar.decode(frame):
            cv2.imwrite('qr_barcode_image.png', frame)
            my_code = code.data.decode('utf-8')
            if my_code not in used_codes:
                print("인식 성공 : ", my_code)
                playsound("qrbarcode_beep.mp3")
                used_codes.append(my_code)

                f2 = open("qr_barcode_data.txt", "w", encoding="utf8")
                f2.write(my_code+'\n')
                f2.close()
                a += 1
            elif my_code in used_codes:
                print("이미 인식된 코드 입니다")
                playsound('qrbarcode_beep.mp3')
            else:
                pass
        # esc키 눌렀을시 종료
        key = cv2.waitKey(1)
        if key == 27:
            break
        cv2.imshow('QRcode Barcode Scan', frame)
        cv2.waitKey(1)

    barcode = my_code
#   barcode = "8801062628476"

    url = 'http://openapi.foodsafetykorea.go.kr/api/14adc49a10ff4df2a831/C005/xml/1/5/BAR_CD=' + barcode

    def parse():
        try:
            PRDLST_NM = item.find("PRDLST_NM").get_text()

            return {
                "음식이름": PRDLST_NM,
            }
        except AttributeError as e:
            return {
                "음식이름": None,
            }

    result = requests.get(url)
    soup = BeautifulSoup(result.content, 'lxml-xml')
    items = soup.find_all("C005")
    print(items)

    row = []
    for item in items:
        row.append(parse())
    coin_list = []
    for i in range(0, len(row)):
        coin_list.append(row[i]['음식이름'])
    product_name = ''.join(coin_list)
    product_name = product_name.replace(" ","_")
    print(product_name)


    CommerceInfor = {}

    namelist = []
    url = 'http://openapi.foodsafetykorea.go.kr/api/14adc49a10ff4df2a831/I2790/xml/1/5/DESC_KOR=' + product_name
    result = requests.get(url)
    soup = BeautifulSoup(result.content, 'lxml-xml')
    print(url)
    name = soup.find_all('DESC_KOR')
    print(name)
    for code in name:
        namelist.append(code.text)

    CommerceInfor['음식이름'] = namelist
    print(list(set(namelist)))

barcode_to_foodname()
# 참고 자료 : https://pjs21s.github.io/openapi/
