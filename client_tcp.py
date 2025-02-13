aimport socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.settimeout(3)

try:
    client.connect(('site.com.br', 80))
    client.send(b'GET / HTTP/2\nhost: site.com.br\n\n\n')
    pacotes_recebidos = client.recv(1024).decode()
    print('Cliente TCP - n0body V1.3.0')
    print('--------------------------------')
    print(pacotes_recebidos)

except Exception as error:
    print('---> Algo está errado!')
    print('--------------------------------')
    print(error)
    print('--------------------------------')