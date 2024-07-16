####다중 클라이언트 전용 ####



import socket

host = "localhost"
port = 7777

# 소켓 객체 생성
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # 서버에 연결
    sock.connect((host, port))

    # 서버에 데이터 전송
    message = "Hello, server!"
    sock.send(message.encode('ascii'))

    # 서버로부터 데이터 수신 (1024 바이트)
    life4cuts_link = sock.recv(1024)
    print(f"인생네컷 링크: {life4cuts_link.decode('ascii')}")
    
except Exception as e:
    # 오류 발생 시 오류 메시지 출력
    print(f"Error: {e}")

finally:
    # 소켓 닫기
    sock.close()
