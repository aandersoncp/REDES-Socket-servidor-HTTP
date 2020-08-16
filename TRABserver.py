from socket import*
import os

serverPort = 5000
host = "localhost"

serverSocket = socket(AF_INET,SOCK_STREAM) #Cria o socket TCP
serverSocket.bind((host ,serverPort)) 

serverSocket.listen(1) #Esperando uma requisição
print("Servidor pronto para receber!\n")

while 1:
	novoSocket, addr = serverSocket.accept()
	dados = novoSocket.recv(1024)
	dados.decode("utf-8")
	print(dados)
	arq = open(dados, 'rb')
	for i in arq.readlines():
		novoSocket.send(i)
	print("Arquivo enviado!")
	arq.close()
	novoSocket.close()