import socket
from _thread import *
import pickle


server = "192.168.8.126"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)

print("Waiting for a connection, Server Started")

connected = set()
players = []
currentPlayer = 0



def threaded_client(conn, player):

    while currentPlayer < 2:
        pass

    temp = ""
    try:

        playerTemp = pickle.loads(conn.recv(4096))
        players.append(playerTemp)

        print(playerTemp)
        temp = players[0]
        print(temp)

        conn.send(pickle.dumps(temp))
        #if player == 1:
         #   conn.sendall(pickle.dumps(players[0]))
        #else:
         #   conn.sendall(pickle.dumps(players[1]))
    except error as e:
        print(e)


    reply = ""
    while True:
        try:
            data = pickle.loads(conn.recv(4096))
            players[player] = data
            if not data:
                print("Dissconected")
                break
            else:
                if player == 1:
                    reply = players[0]
                else:
                    reply = players[1]

                print("Received", data)
                print("Sending", reply)

            conn.sendall(pickle.dumps(reply))

        except:
            break

    print("Lost connection")

    conn.close()



while True:
    conn, addr = s.accept()
    print("Connected to:", addr)


    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1