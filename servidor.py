from socket import *
import random

s = socket ()

host = "192.168.100.35"
porta = 8753
s.bind ((host, porta))
s.listen (10)
chave=13
(conn, cliente) = s.accept ()
print ("Recebi a conexao de "+str(cliente))
while True:
	data = conn.recv (4096)
	msg = data.decode("utf-8")
	msg = msg.upper()
	resp = "";
	letras = 'ABCDEFGHIJKLMNOPQRSTUVXYZ'
	for letra in msg:
		if(letra in letras):
			num = letras.find(letra)
			num = num + chave
		if(num >= len(letras)):
			num = num - len(letras)
		elif(num < 0):
			num = num + len(letras)
			resp = resp + letras[num]
		else:
			resp = resp + letra
	conn.send (str.encode (resp, "UTF-8"))
conn.close