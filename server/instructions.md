밑 서버/클라이언트 부분에서는 소켓 통신을 사용:

소켓 통신:TCP 통신이 기본이 되는데, 이는 입출력 바이트 스트림을 통한 문자, 배열 전송을 함
양쪽에서 데이터 전송할수 있다는 장점이 있음.

소켓은 서버와 클라이언트의 역할로 나뉨

서버                                클라이언트
1.소켓 생성                         1.소켓생성
2.바인딩 bind()                     2.바인딩 해도 그만 안해도 그만
3.접속 대기 listen()                3.접속 시도(connect())
4.접속 수락 accept()                4.
5.데이터 송/수신 send()/recv()      5.데이터 송/수신 send()/recv()
6.접속종료 close()                  6.접속종료 close()

##서버##

import socket

host = "0.0.0.0" -모든 네트워크 접근 허락, 127.0.0.1로 설정하면 그 컴퓨터에서만 접근 가능
port = 7777 - 리소스 모니터 -> tcp 연결 탭에서 안쓰는 포트 찾아서 연결 해야함. 나는 임의로 7777로 한거

1.소켓 생성
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
->tcp통신은 SOCK_STREAM, UDP는 SOCK_DGRAM

2.바인딩
sock.bind((host,port))

3.접속 대기
sock.listen()

4.접속 수락
c_sock, addr = sock.accept()
->여기서 c_sock은 바이트 주고받는 역할, addr은 접근 허락하는 역할

5.데이터 수신
read_data = c_sock.recv(1024)     ##->1024는 받는 바이트의 양
life4cuts_link = "링크"       ##->"https://www.example.com" 형식으로 올 것
c_sock.send(life4cuts_link.encode('ascii'))

6.접속종료
c_sock.close()
sock.close()

socket() : 소켓 만들기
bind() : IP주소와 소켓을 묶기
listen() : 클라이언트의 소켓 기다리기
accept() : 클라이언트의 접속 요청 수락하기
send() / recv() : 데이터를 전송하거나 받기
close() : 소켓 닫기


##클라이언트##

import socket


host = "localhost"
port = 7777

1.소켓생성
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

3.접속 시도
try :
    sock.connect((host,port))

    5.데이터 송/수신
    life4cuts_link = sock.recv(1024)
    print(f"인생네컷 링크:{life4cuts_link.decode('ascii)}")

except Exception as e:
    print(f"Error : {e}")

finally :
    6.소켓종료
    sock.close()