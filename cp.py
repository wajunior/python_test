import os
import shutil

ori = r'C:\Users\Wilson\Desktop\teste1'  # obtem o caminho de origem
dest = r'C:\Users\Wilson\Desktop\teste2'  # obtem o caminho de destino
lista_arquivos = os.listdir(ori)  # lista o diretório de origem ex: comando "dir"
arq = open(ori + r'\matriz.txt')  # lê o conteudo do arquivo matriz.txt
linhas = arq.read()  # armazena o conteudo de matrix.txt em uma variável

for arquivo in lista_arquivos:  # percorre o diretório de origem listrando os arquivos dele
    if arquivo in linhas:  # condição se o conteudo do "arquivo" tem dentro do conteudo da "matriz.txt"
        shutil.copy2(ori + f'\{arquivo}', dest + f'\{arquivo}')  # se sim, copia o conteudo para a pasta de destino.
