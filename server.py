import socket
from _thread import *
from game import Game

import pickle

server = "IP"
port = 5555

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

try:
    s.bind((server,port))
except socket.error as e:
    str(e)

s.listen(2)
print("Wating for connection...")


gameServer = Game()
def threadedClient(conn,player):
    conn.send(str.encode(str(player)))
    reply = ""
    while True:
        try:
            data = conn.recv(2048).decode()

            if not data:
                print("Disconnected")
                break
            else:
                if data[0] == "P":
                    gameServer.mousePos = int(data[1:])
                elif data[0] == "M":
                    gameServer.makeMove(int(data[1:]),player)
                    if gameServer.checkWin():
                        gameServer.winningTurn = player
                elif data == "R":
                    gameServer.reset()

                reply = gameServer

                print("Recieved: ", data)
                print("Sending: ", reply)

                conn.sendall(pickle.dumps(reply))
        except:
            break

    print("Disconnedted")
    conn.close()


currentPlayer = 0
while True:
    conn,addr = s.accept()
    print("Connected to : ",addr)
    if currentPlayer == 1:
        gameServer.ready = True
    start_new_thread(threadedClient,(conn,currentPlayer))
    currentPlayer += 1
