import json, base64
from PIL import Image
from io import BytesIO
import printer # 프린트 모듈
import upload # QR코드 및 업로드 모듈
import combine # 사진 & 프레임 합성 함수
from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return "SocketIO Server is running!"


# 메시지 이벤트 핸들러
@socketio.on('message')
def message(data):

    data = json.loads(data)
    print(data)
    people = data.people # int
    photo = data.photo # base64 string
    frame = data.frame # int
    photo = Image.open(BytesIO(base64.b64decode(photo)))

    print(f'인원수: {people}, 프레임: {frame}')

    '''
    photo = [data.p1, data.p2, data.p3, data.p4] # base64 string
    for i in range(4): # base64 로 받은 이미지 디코딩
        photo[i] = Image.open(BytesIO(base64.b64decode(photo[i])))
    '''

    code = upload.pre_code()
    qrcode = upload.gen_qrcode(code)

    print(f'공유코드: {code}')

    final_image = combine.combine_photo(photo, qrcode, frame)
    final_image.save(f'./media/final-{code}.png', 'png')

    printer.print_printer(f'./media/final-{code}.png', people, code)
    upload.post_file(code, f'./media/final-{code}.png')

# 실행할 때 웹 소켓 서버 시작
if __name__ == '__main__':
    socketio.run(app, host='localhost', port=4000)