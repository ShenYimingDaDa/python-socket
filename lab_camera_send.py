#!/usr/bin/python
#-*- coding:utf-8 -*-
import socket
import struct
import cv2
import numpy
import os
import datetime

filedir=''
filestore=''
# host = '115.159.206.149'
# host = '192.168.2.230'
host='127.0.0.1'
port = 8899
fmt = '128si'
send_buffer = 4096
# filedir='F:\\Demo04\\.metadata\\.plugins\\org.eclipse.wst.server.core\\tmp0\\wtpwebapps\\AgriBigDataSys\\audioImgs\\lab\\'
# filedir='D:\\A_project\\传视频照片\\'
# filestore='D:\\SocketReceive\\lab\\'

def send(filename):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host, port))
        filepath = "pic.jpg"
        filename =filename
        filesize = os.path.getsize(filepath)
        head = struct.pack(fmt, filename.encode(), filesize)
        sock.sendall(head)
        restSize = filesize
        fd = open(filepath,'rb')
        count = 0
        while restSize >= send_buffer:
            data = fd.read(send_buffer)
            sock.sendall(data)
            restSize = restSize - send_buffer
           # print(str(count)+" ")
            count = count + 1
        data = fd.read(restSize)
        sock.sendall(data)
        fd.close()
        print("successfully sent")
    except :
        now=datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
        photo('{time}.jpg'.format(time=now))
        # print("ConnectionError")
        # send(filename)
def photo(filestore):
            cameraCapture = cv2.VideoCapture(0)
            # cameraCapture = cv2.VideoCapture(0)

            success, frame = cameraCapture.read()

            cv2.waitKey(3020)
            success, frame = cameraCapture.read()
            cv2.imwrite('filestore.jpg',frame) #存储为图像
            # cv2.imwrite("/home/pi/camera/USB1/%s.jpeg" %now,frame)
            cameraCapture.release()

while(1):
    for i in range(1,13):
        now=datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
        try:
            photo("pic.jpg")
            send('{dir}{time}.jpg'.format(dir=filedir,time=i))
            print("yes0")
        # except:
        except:
            print("ConnectionError")
            photo('{time}.jpg'.format(time=now))
            # send(filename)
            send('{time}.jpg'.format(time=i))
        if i == 12:
            try:
                photo("pic.jpg")
                send('{dir}{time}.jpg'.format(dir=filedir,time=i))
                send('{dir}{time}.jpg'.format(dir=filestore,time=now))
                print("yes1")

            except:
                # photo('/home/pi/camera/USB2/{time}.jpg'.format(time=now))
                print("ConnectionError")
                photo('{time}.jpg'.format(time=now))
                send('{dir}{time}.jpg'.format(dir=filedir,time=i))
                send('{dir}{time}.jpg'.format(dir=filestore,time=now))
