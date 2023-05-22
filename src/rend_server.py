"""
Rendezvous server that connects nodes.
"""

from typing import List
from model.proto.server_pb2 import *
from model.proto.server_pb2_grpc import ServerStub, ServerServicer, add_ServerServicer_to_server


class PingServer(ServerServicer):
   def ping_server(self, request: PingServerRequest, context) -> PingServerReply:
      """"Response to ping by rend server"""
      return PingServerReply()


class RendServer(PingServer):
   def __init__(self):
      self.ip_list: List[str] = []

   def initiate_connection(self, request, context):
      print(context.peer())
      # ip = choice(ip_list)
      # channel = grpc.insecure_channel(ip+MINER_PORT)
      # client = NetworkStub(channel)
      return InitiateConnectionReply()

   def get_ip_list(self, request, context):
      return super().get_ip_list(request, context)


import grpc
import concurrent.futures as futures
from threading import Thread
if __name__ == "__main__":
   # self.server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
   # service = Network(self.model, self.new_block_callback)
   # add_NetworkServicer_to_server(service, self.server)
   # self.server.add_insecure_port('0.0.0.0'+MINER_PORT)

   client = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
   client_service = RendServer()
   add_ServerServicer_to_server(client_service, client)
   client.add_insecure_port('0.0.0.0:5001')

   server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
   server_service = RendServer()
   add_ServerServicer_to_server(server_service, server)
   server.add_insecure_port('0.0.0.0:5000')

   t1 = Thread(target=server.start)
   t1.start()

   t2 = Thread(target=client.start)
   t2.start()

   channel = grpc.insecure_channel("%5B::1%5D:5000")
   client = ServerStub(channel)
   client.initiate_connection(InitiateConnectionRequest())

   pass