from flask import Flask, request, render_template, redirect, send_file
from banco import criar_banco, adicionar_usuario, buscar_usuario, contar_usuarios, listar_usuarios, remover_usuario
from alerta import enviar_alerta
import time
from collections import defaultdict
import csv

app = Flask(__name__)
criar_banco()

tentativas = defaultdict(list)
usuarios_logados = []
tentativas_login = []
alertas_enviados = 0
alertas_detalhados = []

@app.route('/')
def index():
    return render_template('dashboard.html')

@app.route('/login', methods=['POST'])
def login():
    global alertas_enviados

    nome = request.form.get('usuario')
    senha = request.form.get('senha')

    usuario = buscar_usuario(nome)

    if not usuario:
        return "Usuário não cadastrado. <a href='/cadastro'>Cadastre-se aqui</a>"

    if senha != usuario[2]:
        tentativas_login.append((nome, "falha"))
        agora = time.time()
        tentativas[nome].append(agora)
        tentativas[nome] = [t for t in tentativas[nome] if agora - t < 60]

        if len(tentativas[nome]) >= 3:
            msg = f"ALERTA: Usuário {nome} errou a senha 3 vezes em 1 minuto!"
            enviar_alerta(msg)
            alertas_enviados += 1
            alertas_detalhados.append(msg)
            return "Senha incorreta! Alerta enviado."

        return "Senha incorreta! Tente novamente."

    usuarios_logados.append(nome)
    tentativas_login.append((nome, "sucesso"))

    # Se for admin, vai direto para o painel
    if nome == "admin" and senha == "1234":
        total_usuarios = contar_usuarios()
        usuarios = listar_usuarios()
        return render_template('painel.html',
                               usuarios=usuarios_logados,
                               tentativas=tentativas_login,
                               alertas=alertas_enviados,
                               total_usuarios=total_usuarios,
                               todos_usuarios=usuarios,
                               alertas_detalhados=alertas_detalhados)

    # Outros usuários: mensagem simples
    return "Login realizado com sucesso."

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form.get('usuario')
        senha = request.form.get('senha')
        adicionar_usuario(nome, senha)
        return redirect('/')
    return render_template('cadastro.html')

@app.route('/painel', methods=['GET', 'POST'])
def painel():
    if request.method == 'POST':
        admin_user = request.form.get('admin')
        admin_pass = request.form.get('senha')

        if admin_user == "admin" and admin_pass == "1234":
            total_usuarios = contar_usuarios()
            usuarios = listar_usuarios()
            return render_template('painel.html',
                                   usuarios=usuarios_logados,
                                   tentativas=tentativas_login,
                                   alertas=alertas_enviados,
                                   total_usuarios=total_usuarios,
                                   todos_usuarios=usuarios,
                                   alertas_detalhados=alertas_detalhados)
        else:
            return "Acesso negado"

    return render_template('painel_login.html')

@app.route('/remover_usuario', methods=['POST'])
def remover_usuario_route():
    nome = request.form.get('nome')
    remover_usuario(nome)
    return redirect('/painel')

@app.route('/gerar_planilha', methods=['POST'])
def gerar_planilha():
    with open('relatorio.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Usuário', 'Status'])
        for t in tentativas_login:
            writer.writerow([t[0], t[1]])
        writer.writerow([])
        writer.writerow(['Total de Alertas', alertas_enviados])

    return send_file('relatorio.csv', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
