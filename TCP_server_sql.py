import jingdong_finally as jd
import socket


def main():
    jd1 = jd.JD()
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    tcp_server_socket.bind(('', 8080))
    tcp_server_socket.listen(100)
    while True:
        print('服务器-->192.168.18.35:8080<--已就绪，等待主机连接...')
        client_socket, client_addr = tcp_server_socket.accept()
        print(f'客户端{client_addr[0]}:{client_addr[1]}已连接')
        while True:
            try:
                data = client_socket.recv(1024).decode('gbk')
                res = jd1.exe_sql(data)
                if data:
                    print(data)
                    client_socket.send(f'已接收"{data}"\n- - - - - - - - - -\n结果为：\n{str(res)}\n- - - - - - - - - -'.encode('gbk'))
                else:
                    client_socket.close()
                    print(f'客户端{client_addr[0]}:{client_addr[1]}已断开')
                    break
            except ConnectionResetError as e:
                print(e)
                print(f'客户端{client_addr[0]}:{client_addr[1]}已断开')
                break
    tcp_server_socket.close()


if __name__ == "__main__":
    main()
