import socket
from _thread import *
import pickle
from message import Message
from jetpack import Jetpack
import time
from map import Map

mapSource = 'grafikaDoGry/map2.txt'
server = "192.168.8.126"
port = 5555
winWidth = 800
winHeight = 600
map = Map(mapSource, 4, (220, 47, 10), winWidth, winHeight)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)

print("Waiting for a connection, Server Started")

connected = set()
messages = {}
currentPlayer = 0



def threaded_client(conn, player):

    while currentPlayer < 2:
        pass

    try:
        messReceived = pickle.loads(conn.recv(4096))
        messages[player] = messReceived

        while len(messages) < 2:
            pass

        messToSend = Message(0, 0, 0)
        if player == 1:
            messToSend.player = messages[0].player
            conn.sendall(pickle.dumps(messToSend))
        else:
            messToSend.player = messages[1].player
            conn.sendall(pickle.dumps(messToSend))

    except error as e:
        print(e)


    while True:
        try:
            messReceived = pickle.loads(conn.recv(4096))
            messages[player] = messReceived

            if not messReceived:
                print("Dissconected")
                break
            else:
                if player == 1:
                    messToSend = messages[0]
                else:
                    messToSend = messages[1]

                print("Received", messToSend)
                print("Sending", messReceived)


            conn.sendall(pickle.dumps(messToSend))

        except error:
            print(error)

    print("Lost connection")

    conn.close()

def countdown(time_sec):
    while time_sec:
        time.sleep(1)
        time_sec -= 1



def jetpack_timer(time_sec):
    while True:
        countdown(time_sec)
        jetpack = Jetpack(map)
        if len(messages) > 0:
            messages[0].jetpack= jetpack
            messages[1].jetpack = jetpack
        print("jeb jetpackiem he he")



start_new_thread(jetpack_timer, (5,))

while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1