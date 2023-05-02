# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import model.proto.schema_pb2 as schema__pb2


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
        self.announce_transaction = channel.unary_unary(
                '/messages.Network/announce_transaction',
                request_serializer=schema__pb2.AnnounceTransactionRequest.SerializeToString,
                response_deserializer=schema__pb2.AnnounceTransactionReply.FromString,
                )
        self.get_block = channel.unary_unary(
                '/messages.Network/get_block',
                request_serializer=schema__pb2.GetBlockRequest.SerializeToString,
                response_deserializer=schema__pb2.GetBlockReply.FromString,
                )
        self.get_transaction = channel.unary_unary(
                '/messages.Network/get_transaction',
                request_serializer=schema__pb2.GetTransactionRequest.SerializeToString,
                response_deserializer=schema__pb2.GetTransactionReply.FromString,
                )
        self.get_chain_length = channel.unary_unary(
                '/messages.Network/get_chain_length',
                request_serializer=schema__pb2.GetChainLengthRequest.SerializeToString,
                response_deserializer=schema__pb2.GetChainLengthReply.FromString,
                )
        self.get_chain = channel.unary_unary(
                '/messages.Network/get_chain',
                request_serializer=schema__pb2.GetChainRequest.SerializeToString,
                response_deserializer=schema__pb2.GetChainReply.FromString,
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

    def announce_transaction(self, request, context):
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

    def get_transaction(self, request, context):
        """receive transaction from server to client
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def get_chain_length(self, request, context):
        """receive length of chain from other servers
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def get_chain(self, request, context):
        """receive missing blocks??
        receive all block hashes in the blockchain... in the future allow a partition
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
            'announce_transaction': grpc.unary_unary_rpc_method_handler(
                    servicer.announce_transaction,
                    request_deserializer=schema__pb2.AnnounceTransactionRequest.FromString,
                    response_serializer=schema__pb2.AnnounceTransactionReply.SerializeToString,
            ),
            'get_block': grpc.unary_unary_rpc_method_handler(
                    servicer.get_block,
                    request_deserializer=schema__pb2.GetBlockRequest.FromString,
                    response_serializer=schema__pb2.GetBlockReply.SerializeToString,
            ),
            'get_transaction': grpc.unary_unary_rpc_method_handler(
                    servicer.get_transaction,
                    request_deserializer=schema__pb2.GetTransactionRequest.FromString,
                    response_serializer=schema__pb2.GetTransactionReply.SerializeToString,
            ),
            'get_chain_length': grpc.unary_unary_rpc_method_handler(
                    servicer.get_chain_length,
                    request_deserializer=schema__pb2.GetChainLengthRequest.FromString,
                    response_serializer=schema__pb2.GetChainLengthReply.SerializeToString,
            ),
            'get_chain': grpc.unary_unary_rpc_method_handler(
                    servicer.get_chain,
                    request_deserializer=schema__pb2.GetChainRequest.FromString,
                    response_serializer=schema__pb2.GetChainReply.SerializeToString,
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
    def announce_transaction(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/messages.Network/announce_transaction',
            schema__pb2.AnnounceTransactionRequest.SerializeToString,
            schema__pb2.AnnounceTransactionReply.FromString,
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
    def get_transaction(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/messages.Network/get_transaction',
            schema__pb2.GetTransactionRequest.SerializeToString,
            schema__pb2.GetTransactionReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def get_chain_length(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/messages.Network/get_chain_length',
            schema__pb2.GetChainLengthRequest.SerializeToString,
            schema__pb2.GetChainLengthReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def get_chain(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/messages.Network/get_chain',
            schema__pb2.GetChainRequest.SerializeToString,
            schema__pb2.GetChainReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
