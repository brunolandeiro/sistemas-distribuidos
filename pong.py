from socket import *
import random

s = socket ()

host = "192.168.100.35"
porta = 8753
s.bind ((host, porta))
s.listen (10)

ping = "ping"

(conn, cliente) = s.accept ()
print ("Recebi a conexao de "+str(cliente))

while True:

	data = conn.recv (4096)
	sdata = data.decode("utf-8")
	if(sdata.upper() == "PING" ):
		conn.send (str.encode ("PONG", "UTF-8"))
	else:
		conn.send (str.encode ("Não reconheço "+sdata, "UTF-8"))

conn.close
