#Distributed Systems
        #De Jesús Moreno Yolanda
        #Herrera Godina Adriana Jocelyn
        #Sanchez Torres Sergio Daniel
import socket
import threading

host = '127.0.0.1'
port = 55555

nickname = input("Choose your nickname: ")
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

def receive():
    while True:
        try:
            message = client.recv(1024).decode("utf-8") #we'll receive data, about 1024 bytes
            if message == 'NICK':
                client.send(nickname.encode("utf-8"))
            else:
                print(message)

        except:
            print("Error")
            client.close()
            break

#Send messages to server
def write():
    while True:
        message = f'{nickname}: {input("")}' #to get the whole text
        client.send(message.encode("utf-8"))

receiveThread = threading.Thread(target=receive)
receiveThread.start()

writeThread = threading.Thread(target=write)
writeThread.start()
