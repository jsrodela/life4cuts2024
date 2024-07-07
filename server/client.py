##### 단일 클라이언트 ######
import socket

host = "localhost"
port = 7777

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try  :
    
    sock.connect((host, port))

    life4cuts_link = sock.recv(1024)
    print(f"인생네컷 링크: {life4cuts_link.decode('ascii')}")
    #프린트를 실제로 프론트엔드에서 구현해야
    #지금은 그냥 프린트하는걸로만 함
    
    
except Exception as e:
    print(f"Error: {e}")

finally  :
    sock.close()