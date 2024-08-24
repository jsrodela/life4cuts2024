# 2024 잠신네컷

## 클라이언트 - svelte
- 인원수 (사진 매수) 입력
- 5초 간격으로 사진 촬영 (웹)
- 촬영된 사진을 프레임에 합성
- 합성된 사진을 base64로 인코딩
- socketio 로 서버로 전송

## 서버 - python
- socketio로 사진 & 인원수 수신
- file-gq 서버에서 미리 코드를 받아 QR코드 생성
- QR코드를 프레임에 합성
- 완성된 사진을 인원수대로 인쇄
- 완성된 사진을 file-gq 서버에 코드와 같이 업로드

### json 형식으로 송/수신
- people : 인원수
- photo : base64로 인코딩된 사진

### 사용 모듈
- pycups
- pillow
- qrcode
- requests
- python-socketio
- eventlet
