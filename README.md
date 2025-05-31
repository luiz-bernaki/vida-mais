🏥 Projeto Integrador – Sistema de Monitoramento e Segurança Cibernética para a Clínica VidaMais

📖 Introdução
A Clínica VidaMais, situada em uma cidade de pequeno porte com cerca de 12 mil habitantes, atua com atendimento médico e psicológico por meio de 6 unidades. Recentemente, a clínica sofreu tentativas de invasão digital ao seu sistema de agendamentos online, o que evidenciou diversas vulnerabilidades críticas:

🚫 Falta de controle sobre acessos e tentativas de login
🚫 Nenhum mecanismo de detecção de ameaças
🚫 Ausência total de alertas ou respostas automáticas
🚫 Dados sensíveis expostos a riscos

🔐 Pensando nisso, desenvolvemos um sistema de segurança cibernética e monitoramento para resolver esses problemas e garantir a integridade dos dados e serviços da clínica.

🎯 Objetivos
✔️ Monitorar acessos e tentativas de login
✔️ Detectar comportamentos suspeitos automaticamente
✔️ Enviar alertas por Telegram em tempo real
✔️ (Opcional) Bloquear IPs via firewall
✔️ Disponibilizar um painel web simples de acompanhamento

🛠️ Tecnologias Utilizadas
🐍 Python + Flask (servidor web)
🛢️ MongoDB ou arquivos locais (armazenamento de logs)
🤖 Telegram Bot (alertas automáticos)
🖥️ HTML + Bootstrap (painel web)
🧱 UFW ou iptables (bloqueio de IPs maliciosos)
📄 logging (geração de registros)

📁 Estrutura do Projeto

projeto-clinica/
├── app.py # Backend Flask
├── detector.py # Regras de detecção
├── alerta.py # Envio de alerta para Telegram
├── firewall.py # (Opcional) Bloqueio de IP
├── templates/
│ └── dashboard.html # Página de dashboard
├── logs/
│ └── acessos.log # Arquivo com os registros
└── requirements.txt

💡 Como Funciona
📥 Cada tentativa de login é registrada com IP e horário.
🧠 O sistema analisa o histórico de acessos:
+3 tentativas em 1 minuto → comportamento suspeito.
🚨 Um alerta é enviado automaticamente via Telegram.
👁️ O painel web exibe as informações.
🔒 O IP pode ser bloqueado (opcional).

🧑‍💻 Exemplo: Registro de Login
Arquivo: app.py

@app.route('/login', methods=['POST'])
def login():
ip = request.remote_addr
usuario = request.form['usuario']
hora = datetime.now()

python
Copiar
Editar
logging.info(f"{hora} - Tentativa de login de {usuario} via IP {ip}")

alerta = verificar_ameaca(ip)

return f"Login recebido. {alerta}"
🧠 Lógica de Detecção
Arquivo: detector.py

def verificar_ameaca(ip):
agora = time.time()
acessos[ip].append(agora)
acessos[ip] = [t for t in acessos[ip] if agora - t < 60]

python
Copiar
Editar
if len(acessos[ip]) > 3:
    enviar_alerta(f"ALERTA: IP {ip} com mais de 3 acessos em 1 minuto!")
    return f"Alerta gerado para IP {ip}."

return "Acesso normal."
📢 Envio de Alerta por Telegram
Arquivo: alerta.py

def enviar_alerta(mensagem):
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
data = {"chat_id": CHAT_ID, "text": mensagem}
requests.post(url, data=data)

🔐 (Opcional) Bloqueio de IP
Arquivo: firewall.py

def bloquear_ip(ip):
os.system(f"sudo iptables -A INPUT -s {ip} -j DROP")

🧪 Como Executar

Instale as dependências:

pip install -r requirements.txt

Inicie o servidor:

python app.py

Acesse no navegador:

http://localhost:5000/

Simule acessos no formulário.
Ex: 4 acessos rápidos → gera alerta no Telegram.

📊 Dashboard Web

Página simples de visualização:

✅ Tentativas de login
✅ Acessos suspeitos
✅ Ação corretiva

🧭 Central de Gerenciamento Adicionada

A equipe também desenvolveu uma Central de Gerenciamento Web 💻 para visualização em tempo real dos seguintes dados:

👥 Usuários logados atualmente

📋 Lista de todos os usuários cadastrados

📌 Histórico de tentativas de login com status (sucesso ou falha)

🔔 Alertas detalhados (ex: “Usuário Luiz errou a senha 3 vezes em 1 minuto!”)

❌ Botões de remoção manual de usuários

Essa central torna o gerenciamento da segurança mais prático e transparente para o time de TI da clínica.

📸 Exemplo de interface (inserido no relatório em Word)

✅ Resultados Obtidos
✨ Sistema funcionando com:

Monitoramento em tempo real

Detecção de ataques simples (força bruta)

Alertas automáticos via bot

Registros organizados e interpretáveis

Base para expansão futura

🚀 Próximos Passos

Armazenar dados em banco de dados real (MongoDB ou PostgreSQL)

Adicionar autenticação com senha segura e 2FA

Exibir logs e métricas em gráficos com Chart.js ou Kibana

👥 Contribuidores

👨‍💻 Luiz Gustavo Bernaki
👨‍💻 Fernando Pessoni de Mendonça
👩‍💻 Letícia da Cruz
👩‍💻 Isabeli Flauzino

🎓 Projeto desenvolvido no programa: Talento Tech
