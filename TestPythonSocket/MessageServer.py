#!/usr/bin/python

import sys,os,socket

def main():

    argList = sys.argv

    if argList == 1:
        sys.exit('Give IP and port to listen to')
    elif argList == 2:
        tcp_ip   = argList[1].split(":")[0]
        tcp_port = argList[1].split(":")[1]
    elif argList == 3:
        tcp_ip   = argList[1]
        tcp_port = argList[2]
    else:
        sys.exit('Too many arguments are given')

    buffersize = 20
    sock = socket.socket(socket.AF_NET,socket.SOCK_STREAM)
    sock.bind((tcp_ip,tcp_port))
    sock.listen(1)

    conn, addr = sock.accept()

    print 'Connection address:', addr
    while True:
        data = conn.recv(BUFFER_SIZE)

        if not data: break
        print "Received data:", data
        conn.send(data)
    conn.close()

    if __name__ == "__main__":
        main()

