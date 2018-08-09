#!/usr/bin/python
#@Time 2018/7/18 10:10
#@Author sym
#@File receive.py
#@SoftWare PyCharm
# �����Ƿ��ڷ����������ڽ����ļ���host�޸ĳ���Ӧ�ĵ�ַ ���ڷ����������м��ɣ����ܵ��ļ������ڴ˳���ͬһĿ¼��
import socket
import struct
import datetime
# host = "10.154.15.209" #localhost
host = "127.0.0.1" #localhost
port = 8889  #port
fmt = '128si'
recv_buffer = 4096
listenSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listenSock.bind((host, port))

def receive():
    try:
        nowTime=datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
        listenSock.listen(5)
        conn, addr = listenSock.accept()
        headsize = struct.calcsize(fmt)
        head = conn.recv(headsize)
        filename = struct.unpack(fmt, head)[0].decode().rstrip('\0')
        filename = filename
        filesize = struct.unpack(fmt, head)[1]
        #print("filename:" + filename + "\nfilesize:" + str(filesize))
        recved_size = 0
        fd = open(filename, 'wb')
        count = 0
        while True:
            data = conn.recv(recv_buffer)
            recved_size = recved_size + len(data)
            fd.write(data)
            if recved_size == filesize:
                break
            fd.close()
            print('get it')
    except:
        receive()


while True:
    try:
        print('-----------start------------')
        receive()
    except:
        print('-----------restart------------')
        receive()
