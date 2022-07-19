import win32com.client as win32

outlook = win32.Dispatch('outlook.application')
email = outlook.CreateItem(0)

lista_emails = open(r'C:\Users\Wilson\Desktop\teste1\lista_de_emails.txt')
em = lista_emails.read()

email.To = em.rstrip()
email.Subject = 'Teste de e-mail'
email.HTMLBody = f'Teste de e-mail'

email.Send()
