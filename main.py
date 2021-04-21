import pandas as pd
from twilio.rest import Client

# pandas -> Biblioteca para trabalhar com planilhas - pip install pandas
# openpyxl -> Biblioteca para trabalhar com planilhas
# twilio -> Biblioteca para envio de SMS

# Your Account SID from twilio.com/console
account_sid = "ACf0a5e06e0e3a431bdf6a4d29c57108fe"
# Your Auth Token from twilio.com/console
auth_token  = "c362c62fb0639f0ce70751f5aad14abf"

client = Client(account_sid, auth_token)

# Passo a passo de solução

# Abrir os 6 arquivos em Excel
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000).any():
        mesatual = mes
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, "Vendas"].values[0]
        print(f'No mês {mes} encontrou alguem com mais de 55000')
        message = client.messages.create(
            to="+5521972877118",
            from_="+12622394836",
            body=f'O vendedor {vendedor} realizou no mes de {mesatual} R$ {vendas} de vendas. Parabens!')

        print(message.sid)

print(f'O vendedor {vendedor} realizou no mes de {mesatual} R$ {vendas} de vendas')


# Para cada arquivo:

# Verificar se algum valor na coluna de vendas é maior que 55.000

# Se for maior que 55.000 -> Enviar um SMS com o Nome, o mês e as vendas do vendedor

# Caso não seja maior do que 55.000 não fazer nada

