import socket

HOST = '192.168.128.1' # Endereco IP do Servidor
PORT = 6500 # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)
print 'Para sair use CTRL+X\n'
msg = raw_input("Digite sua mensagem: ")
while msg <> '\x18':
    tcp.send (msg)
    msg = raw_input("Digite sua mensagem: ")
tcp.close()
