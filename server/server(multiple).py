# Server
# 다중 클라이언트

import socket
import threading

def handle_client(c_sock, addr):
    print(f"{addr}에서 접속되었습니다.")
    try:
        # 데이터 수신
        read_data = c_sock.recv(1024)
        if read_data:
            print(f"수신된 데이터: {read_data.decode('ascii')}")

            # 응답 데이터 전송
            life4cuts_link = "링크"
            c_sock.send(life4cuts_link.encode('ascii'))
        else:
            print("수신된 데이터가 없습니다.")
    except Exception as e:
        print(f"오류: {e}")
    finally:
        # 통신 종료
        c_sock.close()
        print(f"{addr}와의 연결이 종료되었습니다.")

def main():
    host = "0.0.0.0"
    port = 7777

    # 소켓 생성
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 바인딩
    server_socket.bind((host, port))
    
    # 접속 대기
    server_socket.listen()
    print(f"서버가 {port} 포트에서 대기 중입니다...")

    while True:
        # 접속 수락
        c_sock, addr = server_socket.accept()
        
        # 클라이언트 처리를 위한 새로운 스레드 생성
        client_thread = threading.Thread(target=handle_client, args=(c_sock, addr))
        client_thread.start()

if __name__ == "__main__":
    main()
