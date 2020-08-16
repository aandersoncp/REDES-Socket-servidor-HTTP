from socket import*
import os
import os.path

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
		for i in arq.readlines():
			if( j == 0):
				msg = 'HTTP/1.1 200 OK\n\n' + i.decode()
			else:
				msg = i.decode()
			j = j + 1
			novoSocket.send(bytes(msg, 'utf-8'))
	else: 
		msg = 'HTTP/1.1 200 OK\n\n404 Not Found'
		novoSocket.send(bytes(msg, 'utf-8'))

	print("Arquivo enviado!")
	arq.close()
	novoSocket.close()