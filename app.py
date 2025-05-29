from flask import Flask, request, render_template, redirect
from banco import criar_banco, adicionar_usuario, buscar_usuario
from alerta import enviar_alerta
import time
from collections import defaultdict

app = Flask(__name__)
criar_banco()

tentativas = defaultdict(list)  # {nome: [timestamp, timestamp, ...]}

@app.route('/')
def index():
    return render_template('dashboard.html')

@app.route('/login', methods=['POST'])
def login():
    nome = request.form.get('usuario')
    senha = request.form.get('senha')

    usuario = buscar_usuario(nome)

    if not usuario:
        return "Usuário não cadastrado. <a href='/cadastro'>Cadastre-se aqui</a>"

    if senha != usuario[2]:
        agora = time.time()
        tentativas[nome].append(agora)
        tentativas[nome] = [t for t in tentativas[nome] if agora - t < 60]

        if len(tentativas[nome]) >= 3:
            enviar_alerta(f"ALERTA: Usuário {nome} errou a senha 3 vezes em 1 minuto!")
            return "Senha incorreta! Alerta enviado."

        return "Senha incorreta! Tente novamente."

    return f"Bem-vindo, {nome}!"

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form.get('usuario')
        senha = request.form.get('senha')

        from banco import adicionar_usuario
        adicionar_usuario(nome, senha)

        return redirect('/')
    return render_template('cadastro.html')

if __name__ == '__main__':
    app.run(debug=True)
