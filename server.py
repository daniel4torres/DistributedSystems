#Distributed Systems
        #De Jesús Moreno Yolanda
        #Herrera Godina Adriana Jocelyn
        #Sanchez Torres Sergio Daniel

import socket #network interface
import threading

#A pair we'll use
host = '127.0.0.1'
port = 55555

#We're gonna use an Internet socket and we're gonna use 'host' and 'port' as address
#Also, we'll use Stream for the TCP protocol
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#For connection data, we will need references
#Logic connections
server.bind((host, port))
server.listen()

#Lists
clients = []
nicknames = []

#FUNCTIONS
#Send the message to the clients
def broadcast(message):
    for client in clients:
        client.send(message)

#Send the message to the clients
def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f'{nickname} has left the chat :(\n'.encode("utf-8"))
            nicknames.remove(nickname)
            break

#Server can accept and manage the connections
def receiveMessages():
    while True:
        client, address = server.accept()
        print(f'Connected with {str(address)}')

        client.send('NICK'.encode("utf-8"))
        nickname = client.recv(1024).decode("utf-8")

        #Adding
        nicknames.append(nickname)
        clients.append(client)

        print(f"Client's nickname: {nickname}")
        broadcast(f"{nickname} connected to the chat!\n".encode("utf-8"))
        client.send("Connected to the server!".encode("utf-8"))

        thread = threading.Thread(target=handle, args=(client,)) #we call the constructor with his arguments, the function 'handle' and handle's arguments
        thread.start()


print("Server running! :D")
receiveMessages()