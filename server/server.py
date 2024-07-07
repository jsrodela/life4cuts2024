##### 서버 ######


###1111 : 소켓생성###
##2222  : 바인딩-(80번 http 443번 https) 사용하지 않는 포트 연결해야 함, 7777로 설정###
##33333 : 접속대기
##44444 : 접속 수락
##55555 : 데이터 수신
##66666 : 통신종료

import socket

###아래는 서버###
host = "0.0.0.0"
port = 7777

#1 소켓생성
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#2 바인딩
sock.bind((host,port))
#"안에 호스트",7777 = port

#3 접속대기
sock.listen()

#4 접속수락
c_sock, addr = sock.accept()

##위 addr은 대기 전용/주고받는거는 c_sock

#5 데이터 수신
read_data = c_sock.recv(1024)
life4cuts_link = "링크"
c_sock.send(life4cuts_link.encode('ascii'))
##메모리 양은 1024로 함

#수신:format(read_data))

c_sock.close()
sock.close()