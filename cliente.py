import socket
HOST = '192.168.128.1' # Endereco IP do Servidor
PORT = 5000 # Porta que o Servidor esta
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dest = (HOST, PORT)
print('Para sair use CTRL+X\n')
msg = raw_input("Digite sua mensagem: ")

while msg <> '\x18':
    udp.sendto(msg, dest)
    msg = raw_input("Digite sua mensagem: ")

udp.close()
