import json, base64
from PIL import Image
from io import BytesIO
import print # 프린트 모듈
import upload # QR코드 및 업로드 모듈
import combine # 사진 & 프레임 합성 함수
import socketio

# Socket.IO 서버 생성
sio = socketio.Server()

# 연결 이벤트 핸들러
@sio.event
def connect(sid, environ):
    print('클라이언트가 연결되었습니다:', sid)

# 메시지 이벤트 핸들러
@sio.event
def message(sid, data):
    data = json.loads(data)
    people = data.people # int
    frame = data.frame # int
    photo = [data.p1, data.p2, data.p3, data.p4] # base64 string
    for i in range(4): # base64 로 받은 이미지 디코딩
        photo[i] = Image.open(BytesIO(base64.b64decode(photo[i])))
    code = upload.pre_code()
    qrcode = upload.gen_qrcode(code)
    final_image = combine.combine_photo(photo, qrcode, frame)
    final_image.save(f'./media/final-{code}.png', 'png')
    print.print_printer(f'./media/final-{code}.png', people)
    upload.post_file(code, f'./media/final-{code}.png')

# 실행할 때 웹 소켓 서버 시작ß
if __name__ == '__main__':
    app = socketio.WSGIApp(sio)
    socketio.server.SocketIOServer(('localhost', 8000), app).serve_forever()