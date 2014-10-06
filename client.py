import socket

def encrypt(x):
    y = []
    for i in range(len(x)):
        y.append(chr(ord(x)+ 1))
    y = str(y)

    return y

def e(x):
    return ''.join([chr(ord(a)+ 1) for a in x])

HOST = '10.4.4.2'    # The remote host
PORT = 50008              # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

results = []

#Password
s.send(e("Hello World"))
data = s.recv(1024)
results.append(data)


    



    
s.close()

