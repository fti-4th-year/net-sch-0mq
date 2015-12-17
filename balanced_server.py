import zmq
import time
import sys
from threading import Thread
port =  sys.argv[ 1 ]
int( port )
url = "inproc://workers"

context = zmq.Context()
frontend = context.socket(zmq.ROUTER)
backend = context.socket(zmq.DEALER)
frontend.bind("tcp://*:%s" % port)
backend.bind(url)

def responser_func( url , rid ):
	socket = context.socket( zmq.REP )
	socket.connect( url )
	while True:
		message = socket.recv()
		print "Received request: " , message , " in " , rid
		socket.send( "response from %i" % rid )
def create_responser( url , rid ):
	thread = Thread( target = responser_func , args = ( url , rid , ) )
	#thread.setDaemon( True )
	thread.start()
	return thread

for i in range(5):
	create_responser(url,i)

zmq.device(zmq.QUEUE, frontend, backend)

clients.close()
workers.close()
context.term()
