# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import shop.grpc_ecommerce.protobufs.onlineshopping_pb2 as onlineshopping__pb2


class BuyerActionsStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.createAccount = channel.unary_unary(
                '/BuyerActions/createAccount',
                request_serializer=onlineshopping__pb2.AccountCreationRequest.SerializeToString,
                response_deserializer=onlineshopping__pb2.AccountCreationResponse.FromString,
                )
        self.login = channel.unary_unary(
                '/BuyerActions/login',
                request_serializer=onlineshopping__pb2.AccountLoginRequest.SerializeToString,
                response_deserializer=onlineshopping__pb2.AccountCreationRequest.FromString,
                )
        self.search = channel.unary_unary(
                '/BuyerActions/search',
                request_serializer=onlineshopping__pb2.SearchProductRequest.SerializeToString,
                response_deserializer=onlineshopping__pb2.SearchProductResponse.FromString,
                )
        self.getProducts = channel.unary_unary(
                '/BuyerActions/getProducts',
                request_serializer=onlineshopping__pb2.GetProduct.SerializeToString,
                response_deserializer=onlineshopping__pb2.SearchProductResponse.FromString,
                )
        self.addToCart = channel.unary_unary(
                '/BuyerActions/addToCart',
                request_serializer=onlineshopping__pb2.GetProduct.SerializeToString,
                response_deserializer=onlineshopping__pb2.SearchProductResponse.FromString,
                )


class BuyerActionsServicer(object):
    """Missing associated documentation comment in .proto file."""

    def createAccount(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def login(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def search(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getProducts(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def addToCart(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_BuyerActionsServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'createAccount': grpc.unary_unary_rpc_method_handler(
                    servicer.createAccount,
                    request_deserializer=onlineshopping__pb2.AccountCreationRequest.FromString,
                    response_serializer=onlineshopping__pb2.AccountCreationResponse.SerializeToString,
            ),
            'login': grpc.unary_unary_rpc_method_handler(
                    servicer.login,
                    request_deserializer=onlineshopping__pb2.AccountLoginRequest.FromString,
                    response_serializer=onlineshopping__pb2.AccountCreationRequest.SerializeToString,
            ),
            'search': grpc.unary_unary_rpc_method_handler(
                    servicer.search,
                    request_deserializer=onlineshopping__pb2.SearchProductRequest.FromString,
                    response_serializer=onlineshopping__pb2.SearchProductResponse.SerializeToString,
            ),
            'getProducts': grpc.unary_unary_rpc_method_handler(
                    servicer.getProducts,
                    request_deserializer=onlineshopping__pb2.GetProduct.FromString,
                    response_serializer=onlineshopping__pb2.SearchProductResponse.SerializeToString,
            ),
            'addToCart': grpc.unary_unary_rpc_method_handler(
                    servicer.addToCart,
                    request_deserializer=onlineshopping__pb2.GetProduct.FromString,
                    response_serializer=onlineshopping__pb2.SearchProductResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'BuyerActions', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class BuyerActions(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def createAccount(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/BuyerActions/createAccount',
            onlineshopping__pb2.AccountCreationRequest.SerializeToString,
            onlineshopping__pb2.AccountCreationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def login(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/BuyerActions/login',
            onlineshopping__pb2.AccountLoginRequest.SerializeToString,
            onlineshopping__pb2.AccountCreationRequest.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def search(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/BuyerActions/search',
            onlineshopping__pb2.SearchProductRequest.SerializeToString,
            onlineshopping__pb2.SearchProductResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getProducts(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/BuyerActions/getProducts',
            onlineshopping__pb2.GetProduct.SerializeToString,
            onlineshopping__pb2.SearchProductResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def addToCart(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/BuyerActions/addToCart',
            onlineshopping__pb2.GetProduct.SerializeToString,
            onlineshopping__pb2.SearchProductResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
