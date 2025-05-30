import requests

TOKEN = '7744950402:AAFCHuop-UcdBQMTeTperMbg-_sI2NO3KF4'
CHAT_ID = '6202631349'

def enviar_alerta(mensagem):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": mensagem}
    requests.post(url, data=data)
