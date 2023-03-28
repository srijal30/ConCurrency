# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import schema_pb2 as schema__pb2


class NetworkStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.announce_block = channel.unary_unary(
                '/messages.Network/announce_block',
                request_serializer=schema__pb2.AnnounceBlockRequest.SerializeToString,
                response_deserializer=schema__pb2.AnnounceBlockReply.FromString,
                )
        self.send_block = channel.unary_unary(
                '/messages.Network/send_block',
                request_serializer=schema__pb2.SendBlockRequest.SerializeToString,
                response_deserializer=schema__pb2.SendBlockReply.FromString,
                )
        self.send_transaction = channel.unary_unary(
                '/messages.Network/send_transaction',
                request_serializer=schema__pb2.SendTransactionRequest.SerializeToString,
                response_deserializer=schema__pb2.SendTransactionReply.FromString,
                )
        self.get_block = channel.unary_unary(
                '/messages.Network/get_block',
                request_serializer=schema__pb2.GetBlockRequest.SerializeToString,
                response_deserializer=schema__pb2.GetBlockReply.FromString,
                )
        self.request_transaction = channel.unary_unary(
                '/messages.Network/request_transaction',
                request_serializer=schema__pb2.RequestTransactionRequest.SerializeToString,
                response_deserializer=schema__pb2.RequestTransactionReply.FromString,
                )


class NetworkServicer(object):
    """Missing associated documentation comment in .proto file."""

    def announce_block(self, request, context):
        """/ CLIENT SENDS
        announce block from client to server
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def send_block(self, request, context):
        """send block from client to server
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def send_transaction(self, request, context):
        """send transaction from client to server
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def get_block(self, request, context):
        """/ CLIENT RECEIVES
        receive block from server to client
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def request_transaction(self, request, context):
        """receive transaction from server to client
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_NetworkServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'announce_block': grpc.unary_unary_rpc_method_handler(
                    servicer.announce_block,
                    request_deserializer=schema__pb2.AnnounceBlockRequest.FromString,
                    response_serializer=schema__pb2.AnnounceBlockReply.SerializeToString,
            ),
            'send_block': grpc.unary_unary_rpc_method_handler(
                    servicer.send_block,
                    request_deserializer=schema__pb2.SendBlockRequest.FromString,
                    response_serializer=schema__pb2.SendBlockReply.SerializeToString,
            ),
            'send_transaction': grpc.unary_unary_rpc_method_handler(
                    servicer.send_transaction,
                    request_deserializer=schema__pb2.SendTransactionRequest.FromString,
                    response_serializer=schema__pb2.SendTransactionReply.SerializeToString,
            ),
            'get_block': grpc.unary_unary_rpc_method_handler(
                    servicer.get_block,
                    request_deserializer=schema__pb2.GetBlockRequest.FromString,
                    response_serializer=schema__pb2.GetBlockReply.SerializeToString,
            ),
            'request_transaction': grpc.unary_unary_rpc_method_handler(
                    servicer.request_transaction,
                    request_deserializer=schema__pb2.RequestTransactionRequest.FromString,
                    response_serializer=schema__pb2.RequestTransactionReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'messages.Network', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Network(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def announce_block(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/messages.Network/announce_block',
            schema__pb2.AnnounceBlockRequest.SerializeToString,
            schema__pb2.AnnounceBlockReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def send_block(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/messages.Network/send_block',
            schema__pb2.SendBlockRequest.SerializeToString,
            schema__pb2.SendBlockReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def send_transaction(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/messages.Network/send_transaction',
            schema__pb2.SendTransactionRequest.SerializeToString,
            schema__pb2.SendTransactionReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def get_block(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/messages.Network/get_block',
            schema__pb2.GetBlockRequest.SerializeToString,
            schema__pb2.GetBlockReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def request_transaction(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/messages.Network/request_transaction',
            schema__pb2.RequestTransactionRequest.SerializeToString,
            schema__pb2.RequestTransactionReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
