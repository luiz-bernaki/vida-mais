import requests

TOKEN = '7744950402:AAFCHuop-UcdBQMTeTperMbg-_sI2NO3KF4'
CHAT_ID = '6202631349'

def enviar_alerta(mensagem):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": mensagem}
<<<<<<< HEAD
    requests.post(url, data=data)
=======
    response = requests.post(url, data=data)
    print(response.text)  # Isso vai mostrar se deu certo ou não
>>>>>>> 6e665a87b702563a9747773e5538a73d587e0d2c
