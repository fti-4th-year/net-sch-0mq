import zmq
import time
import sys
import random
from threading import Thread
from time import sleep
port =  sys.argv[ 1 ]
int( port )
repeaters = 0
repeater_id = 0
def repeater_func( arg ):
	global repeaters
	context = zmq.Context()
	socket = context.socket( zmq.REQ )
	socket.connect( "tcp://localhost:%s" % port )
	while True:
		rand = random.random()
		if rand < 0.2:
			repeaters = repeaters - 1
			#print "repeater killed:" , arg
			return
		socket.send( "request from %s" % arg )
		message = socket.recv()
		time.sleep( rand )
def create_repeater():
	global repeater_id
	repeater_id = repeater_id + 1
	thread = Thread( target = repeater_func , args = ( repeater_id , ) )
	thread.setDaemon( True )
	thread.start()
	return thread

if __name__ == "__main__":
	try:
		while True:
			#repeaters.append( create_repeater() )
			rand = random.random()
			if rand < 0.4:
				create_repeater()
				repeaters = repeaters + 1
				print "repeaters count:" , repeaters
			sleep( 0.1 )
	except KeyboardInterrupt:
		raise
    
