from socket import  *
import random
import threading
import sys

s = socket ()
servidor="192.168.100.35"
porta=8753
s.connect((servidor, porta))
print("Bem vindo ao jogo PING - PONG!")
print ("Conectado ao servidor %s:%d"%(servidor,porta))

while True:
	eca = 'eca'
	while eca != 'sair':
		eca = input("Digite PING para jogar:")

		print(eca)
		s.send (str.encode (eca, "UTF-8"))

		resp = s.recv (4096)
		sresp = resp.decode ("UTF-8")
		print (sresp)

s.close ()