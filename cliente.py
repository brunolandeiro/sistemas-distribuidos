from socket import  *
import random
import threading
import sys

s = socket ()
servidor="192.168.100.35"
porta=8753
s.connect((servidor, porta))
print ("Conectado ao servidor %s:%d"%(servidor,porta))

while True:
	eca = 'eca'
	while eca != 'sair':
		eca = input("Digite uma msg:")

		print(eca)
		s.send (str.encode (eca, "UTF-8"))

		resp = s.recv (4096)
		sresp = resp.decode ("UTF-8")
		print ("Mensagem criptografada: "+sresp)

s.close ()