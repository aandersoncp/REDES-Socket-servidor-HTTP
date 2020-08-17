from socket import*
import os.path
import datetime
import time
import os

serverPort = 5000
host = "localhost"

serverSocket = socket(AF_INET,SOCK_STREAM) #Cria o socket TCP
serverSocket.bind((host ,serverPort)) 

serverSocket.listen(1) #Esperando uma requisição
print("Servidor pronto para receber!\n")

def caminho_arquivo(dados):
	fim = dados.find("HTTP")
	i = 4
	caminho = ""
	while(i < fim - 1):
		caminho = caminho + dados[i]
		i = i + 1
	return caminho

while 1:
	novoSocket, addr = serverSocket.accept()
	dados = novoSocket.recv(2048).decode()
	caminho = caminho_arquivo(dados)
	
	if(os.path.exists(caminho)):
		arq = open(caminho, 'rb')
		j = 0
		data = str(datetime.datetime.now())
		tamanho = str(os.path.getsize(caminho))
		for i in arq.readlines():
			if( j == 0):
				msg = 'HTTP/1.1 200 OK\nConnection: close\nDate: ' + str(datetime.datetime.now()) + '\nLast-Modified: ' + time.ctime(os.path.getmtime(caminho)) + '\nContent-length: ' + str(os.path.getsize(caminho)) + '\nContent-type: text\n\n' + i.decode()
			else:
				msg = i.decode()
			j = j + 1
			novoSocket.send(bytes(msg, 'utf-8'))
		print("Arquivo enviado!")
		arq.close()
	else: 
		msg = 'HTTP/1.1 200 OK\nConnection: close\nDate: \n' + str(datetime.datetime.now()) + '\nServer: (############)' + '\n\n404 Not Found'
		novoSocket.send(bytes(msg, 'utf-8'))
		print("Arquivo enviado!")

	novoSocket.close()