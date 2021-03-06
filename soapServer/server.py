"""
Example soap server using spyne.
Run with
   uwsgi --http :8000 \
         --wsgi-file soap_server.py \
         --virtualenv ~/.pyenv/versions/3.5.2/envs/zeep \
         -p 10
"""
import time

from spyne import Application, ServiceBase, Unicode, rpc
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
import random
import os


class ExampleService(ServiceBase):

    @rpc(Unicode,Unicode, _returns=Unicode)
    def slow_request(ctx, creditcardNumber, username):
        number = random.random()
        if(number < 0.95):
            return "Yes"
        else:
            return "No"

application = Application(
    services=[ExampleService],
    tns='http://namratha.org/',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11())

application = WsgiApplication(application)

if __name__ == '__main__':
    import logging

    from wsgiref.simple_server import make_server

    logging.basicConfig(level=logging.DEBUG)
    logging.getLogger('spyne.protocol.xml').setLevel(logging.DEBUG)

    logging.info("listening to http://127.0.0.1:8080")
    logging.info("wsdl is at: http://localhost:8000/?wsdl")

    server = make_server('0.0.0.0', 8080, application)
    print(server.server_port)
    print(server.server_name)
    print(server.server_address)
    server.serve_forever()