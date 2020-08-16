import socket
import os

target_host = "localhost"
target_port = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((target_host, target_port))

mensagem = "/home/anderson/dados.txt"
b = bytes(mensagem, 'utf-8')
client.send(b)
arquivo = open('/home/anderson/Área de Trabalho/file.txt', 'w')

while 1: 
	resposta = client.recv(1024)
	if not resposta:
		break
	dados = resposta.decode('utf-8')
	print(resposta)
	arquivo.write(dados)

"""for i in arquivo.readlines():
	i.decode("utf-8")
	print(i)"""

arquivo.close()
client.close()