##필요 시 사용
##위 서버 코드보다 간략화했지만 동시에 복잡하기 때문에 쓰일 일은 없음
##쓰일 일 없으************


import socket

host = "0.0.0.0"
port = 7777

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host,port))
server_socket.listen()

while True : 
    client_socket, client_address = server_socket.accept()
    
    
    try : 
        data = client_socket.recv(1024).decode('ascii')
        if not data:
            continue
        
        life4cuts_link = "링크"
        client_socket.send(life4cuts_link.encode('ascii'))
    except Exception as e:
        print(f"오류: {e}")
    finally :
        client_socket.close()
        
