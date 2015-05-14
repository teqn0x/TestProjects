#!/usr/bin/python


import sys,os,socket

def main():

    #Arguments given are IP and port

    argList = sys.argv

    if len(argList) == 1:
        sys.exit('Give IP and port as arguments')
    elif len(argList) == 2:
        tcp_ip   = argList[1].split(":")[0]
        tcp_port = argList[1].split(":")[1]
    elif len(argList) == 3:
        tcp_ip   = argList[1]
        tcp_port = argList[2]
    else:
        sys.exit('Too many arguments given')
    

    buffersize = 1024
    message = input('Type a message to send')


    sock = socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.connect((tcp_ip,tpc_port))
    sock.send(message)
    data = sock.recv(buffersize)
    sock.close()

    print 'Received data:', data

if __name__ == "__main__":
    main()


    
    
    
