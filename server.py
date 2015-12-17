import zmq
import time
import sys
port =  sys.argv[ 1 ]
int( port )
context = zmq.Context()
socket = context.socket( zmq.REP )
socket.bind( "tcp://*:%s" % port )
while True:
    message = socket.recv()
    print "Received request: " , message
    socket.send( "response" )
