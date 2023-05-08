from typing import List
from flask import Flask, request

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
    return "success"

@app.route("/api/disconnect")
def disconnect_peer():
    ip: str = request.remote_addr
    if ip in peer_list:
        peer_list.remove(ip)
    return "success"

if __name__ == "__main__":
    app.run(host="0.0.0.0")