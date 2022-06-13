from tkinter.filedialog import *
from tkinter import *
import os
import shutil

def copia():
    source = str(f'{entrada_origem.get()}').lower().strip()
    destino = str(f'{entrada_destino.get()}').lower().strip()
    arq = open(r'C:\Users\Wilson\Desktop\teste1\matriz.txt')

    lista_arquivos = os.listdir(source)
    txt = arq.read()

    for arquivos in lista_arquivos:
        if arquivos in txt:
            shutil.copy2(f'{source}', f'{destino}')


janela = Tk()

janela.title('Transferência de arquivos')

texto_titulo = Label(janela, text='Transferência de arquivos', font='Verdana 14 bold')
texto_titulo.grid(column=1, row=0, padx=5, pady=5)

texto_entrada = Label(janela, text='Origem')
texto_entrada.grid(column=0, row=1, padx=5, pady=5)
entrada_origem = Entry(janela)
entrada_origem.grid(column=1, row=1, padx=5, pady=5)

texto_destino = Label(janela, text='Destino')
texto_destino.grid(column=0, row=2, padx=5, pady=5)
entrada_destino = Entry(janela)
entrada_destino.grid(column=1, row=2, padx=5, pady=5)

'''txt_arquivo = Label(janela, text='Arquivo TXT')
txt_arquivo.grid(column=0, row=3, padx=5, pady=5)
entrada_txt = Entry(janela)
entrada_txt.grid(column=1, row=3, padx=5, pady=5)'''

bt_exe = Button(janela, text='Executar', command=copia)
bt_exe.grid(column=1, row=4, padx=5, pady=5)

janela.geometry('400x300+200+200')
janela.mainloop()
