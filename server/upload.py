import json
import qrcode
import requests
from PIL.Image import Image

VIDEO_SERVER_URL = 'https://jamsin-file.kro.kr'

def pre_code(): # 공유코드 사전 생성
    try:
        r = requests.post(VIDEO_SERVER_URL + "/pre_code")
        response = json.loads(r.content)

        match response['status']:
            case 'success':
                code = response['code']
                print('Received code', code)
                return code
            case _:
                print('Invalid response from file server;', r.raw)
                return None
    except Exception as ex:
        print("Exception while sending to file server;", ex)
        return None

def gen_qrcode(code: int) -> Image: # 미리 받은 공유코드로 QR코드 생성
    qrc = qrcode.QRCode(
        version=1,
        error_correction=qrcode.ERROR_CORRECT_M,
        box_size=3,
        border=1
    )
    qrc.add_data(VIDEO_SERVER_URL + '/receive?code=' + str(code))
    img = qrc.make_image(back_color=(255, 255, 255), fill_color=(0, 0, 0))
    print("Generated qr code" + str(code))
    return img

def post_file(code: int, path): # 완성된 파일 업로드
    try:
        files = {'file': open(path, 'rb')}
        values = {'code': code}

        r = requests.post(VIDEO_SERVER_URL + "/post_file", files=files, data=values)
        response = json.loads(r.content)
        match response['status']:
            case 'success':
                print('Image file upload complete')
                return True
            case _:
                print('Invalid response from file server;', r.raw)
                return False
    except Exception as ex:
        print("Exception while sending to file server;", ex)
        return False
