#!/usr/bin/python
#-*- coding:utf-8 -*
#@Time 2018/7/18 10:10
#@Author sym
#@File .py
#@SoftWare PyCharm

import socket
import struct
import cv2
import numpy
import os
import datetime
import time
while 1:
    host = '127.0.0.1'#host要改成服务器地址
    port = 8889#要和recvive.py里的端口保持一致
    fmt = '128si'
    send_buffer = 4096
    nowTime = datetime.datetime.now().strftime('%Y%m%d_%H_%M_%S')
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    filepath = "pic.jpg"#要上传的文件的路径
    filename = str(nowTime) + os.path.split(filepath)[1]
    filesize = os.path.getsize(filepath)
    print("filename:" + filename + "\nfilesize:" + str(filesize))
    head = struct.pack(fmt, filename.encode(), filesize)
    print("\nhead size:" + str(head.__len__()) + "\n" + str(head))
    sock.sendall(head)
    restSize = filesize
    fd = open(filepath, 'rb')
    count = 0
    while restSize >= send_buffer:
        data = fd.read(send_buffer)
        sock.sendall(data)
        restSize = restSize - send_buffer
        print(str(count) + " ")
        count = count + 1
    data = fd.read(restSize)
    sock.sendall(data)
    fd.close()
    print("successfully sent")
    time.sleep(3)
