from typing import List
from model.proto.server_pb2 import *
from model.proto.server_pb2_grpc import ServerStub, ServerServicer, add_ServerServicer_to_server

import grpc
import concurrent.futures as futures
from threading import Thread, Lock
from time import sleep

from rend_server import PingService, RendServer

PING_INTERVAL = 2
SERVER_PORT = 5000
CLIENT_PORT = 5001

# TODO port issue
if __name__ == "__main__":
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    server_service = RendServer()
    add_ServerServicer_to_server(server_service, server)
    server.add_insecure_port(f"0.0.0.0:{CLIENT_PORT}")
    
    # initiate connection
    announcer = ServerStub(channel = grpc.insecure_channel(f"localhost:{SERVER_PORT}"))
    announcer.initiate_connection(InitiateConnectionRequest())

    # start the listener
    server.start()
    server.wait_for_termination()

    pass