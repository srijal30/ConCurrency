from typing import List
from networking import socket
from flask import Flask, request
from threading import threading
import time

#((TESTINGGGG)) Checks if port is in use, otherwise, single node network will try to send a request to an inactive port
# probably want to get rid of this later, since we are going to be using a central server (rendzevous???)
# note: only works for localhost!!!

def is_port_in_use(ip: str, port: str) -> bool:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex((ip + ":" + port)) == 0

def peer_list_heartbeat() -> None:
    for ip in peer_list:
        if not (is_port_in_use(ip, "50001")):
           peer_list.remove(ip)
           print("removed ip")

def pulse(start : bool) -> None:
    while start:
        if (int(time.time()/60000000000) % 5 == 0):
            peer_list_heartbeat()



t1 = threading.Thread(target=pulse(), args=(True))
t1.start()


app = Flask(__name__)

peer_list: List[str] = []

@app.route("/api/get_nodes")
def get_node_list():
    return peer_list

@app.route("/api/connect")
def connect_peer():
    ip: str = request.remote_addr
    if ip not in peer_list:
        peer_list.append(ip)
    return ip

# NOTE: THIS IS NOT IDEAL, CHANGE TO HEARBEAT


if __name__ == "__main__":
    app.run(host="0.0.0.0")
