import socket


def socket_connect():
    # 1、创建TCP套接字
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 2、链接服务器
    while True:
        try:
            server_ip = input('请输入服务器ip：')
            server_port = int(input('请输入服务器port：'))
            res = tcp_socket.connect_ex((server_ip, server_port))
            # 0表示连接成功，其他连接错误
            if res:
                print(f'服务器连接失败！请重新连接！')
                break
        except Exception as e:
            print(e)
            print('服务器连接错误！请重新输入：')
            break
        return tcp_socket


def main():
    while True:
        tcp_socket = socket_connect()
        if tcp_socket:
            while True:
                msg = input('请输入要发送的内容/quit断开连接：')
                if msg == 'quit':
                    print('已断开！')
                    tcp_socket.close()
                    break
                else:
                    # 3、收发信息
                    tcp_socket.send(msg.encode('gbk'))
                    rcv_msg = tcp_socket.recv(1024*1024*1024).decode('gbk')
                    print(rcv_msg)
                    # rcv_msg2 = tcp_socket.recv(1024 * 1024 * 1024).decode('gbk')
                    # print(rcv_msg2)
                    # 4、关闭套接字


if __name__ == '__main__':
    main()
