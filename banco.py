import sqlite3

def criar_banco():
    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            senha TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def adicionar_usuario(nome, senha):
    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO usuarios (nome, senha) VALUES (?, ?)', (nome, senha))
    conn.commit()
    conn.close()

def buscar_usuario(nome):
    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM usuarios WHERE nome = ?', (nome,))
    usuario = cursor.fetchone()
    conn.close()
    return usuario
