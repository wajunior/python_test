from urllib import request

url = 'http://intranet.macponta.com.br/intranet/public/uploads/documentos/4b8a8a3309f879d626c5a3fa7ea8d583.pdf'  # atribui o link do arquivo em uma variável
local = r'C:\Users\Wilson\Desktop\teste1\PCD.pdf'  # atribui o local de salvar em uma variavel

request.urlretrieve(url, local)  # executa o download
