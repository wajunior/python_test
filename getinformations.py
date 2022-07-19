import getpass
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(('8.8.8.8', 80))
file = open(r'C:\Users\Wilson\Desktop\teste1\b.txt', 'w')  # escolhe o arquivo que será gravado os dados

user = getpass.getuser()  # grava os dados do usuário na variavel user
arq = file.write(user)  # grava os dados do usuário da variavel user no arquivo txt acima
x = file.write(s.getsockname()[0])  # grava os dados do IP da variavel s no arquivo txt acima

print(user)
print(s.getsockname()[0])

