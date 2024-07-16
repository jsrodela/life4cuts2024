# Server
# 단일 클라이언트

import socket

host = "0.0.0.0"  # 모든 네트워크 접근 허락, 127.0.0.1로 설정할 시 로컬에서만 접근 가능
port = 7777  # 임의의 값임. 안쓰는 포트 찾아서 연결필요

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 소켓생성

sock.bind((host, port))  # 바인딩,
# "안에 호스트", port = 7777

sock.listen()  # 접속대기

c_sock, addr = sock.accept()  # 접속수락


read_data = c_sock.recv(1024) # 데이터 수신
life4cuts_link = "링크"
c_sock.send(life4cuts_link.encode('ascii'))



c_sock.close()
sock.close()