"""
Rendezvous server that connects nodes.
"""

from typing import List
from model.proto.server_pb2 import *
from model.proto.server_pb2_grpc import ServerStub, ServerServicer, add_ServerServicer_to_server

import grpc
import concurrent.futures as futures
from threading import Thread, Lock
from time import sleep

PING_INTERVAL = 2
SERVER_PORT = 5000
CLIENT_PORT = 5001

class PingService(ServerServicer):
   def ping(self, request: PingServerRequest, context) -> PingServerReply:
      """"Response to ping by rend server"""
      return PingServerReply()


# NOTE:
# create a disconnect_ method
class RendServer(PingService):
   def __init__(self):
      self.ip_list: List[str] = []
      self.lock = Lock()

   def initiate_connection(self, request, context):
      client_ip = context.peer()
      print(f"{client_ip} has connected")
      self.lock.acquire()
      if client_ip not in self.ip_list:
         self.ip_list.append(context.peer())
      self.lock.release()
      return InitiateConnectionReply()

   # remote calls this
   def get_ip_list(self, request, context):
      return GetIpListReply(ip_list=self.ip_list)      


   def ping_peers(self):
      disconnected_ips = []
      """Pings all the peers in ip_list and checks which ones are still connected. If disconnected, removed from ip_list"""
      self.lock.acquire()
      for ip in self.ip_list:
         tmp_client = ServerStub(channel = grpc.insecure_channel(ip))
         try:
            tmp_client.ping_server(PingServerRequest())
         except grpc.RpcError as e:
            disconnected_ips.append(ip)
      for ip in disconnected_ips:
         print(f"{ip} has disconnected")  # NOTE
         if ip in self.ip_list:
            self.ip_list.remove(ip)
      self.lock.release()


if __name__ == "__main__":
   # self.server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
   # service = Network(self.model, self.new_block_callback)
   # add_NetworkServicer_to_server(service, self.server)
   # self.server.add_insecure_port('0.0.0.0'+MINER_PORT)

   ### TESTING
   # client = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
   # client_service = RendServer()
   # add_ServerServicer_to_server(client_service, client)
   # client.add_insecure_port('0.0.0.0:5001')
   # channel = grpc.insecure_channel("%5B::1%5D:5000")
   # client = ServerStub(channel)
   # client.initiate_connection(InitiateConnectionRequest())

   ### SERVER
   server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
   server_service = RendServer()
   add_ServerServicer_to_server(server_service, server)
   server.add_insecure_port(f"0.0.0.0:{SERVER_PORT}")

   global_lock = Lock()

   t1 = Thread(target=server.start)
   t1.start()

   while True:
      sleep(PING_INTERVAL)
      server_service.ping_peers()
      print("round of pinging sucess") # NOTE
