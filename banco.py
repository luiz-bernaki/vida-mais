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

def contar_usuarios():
    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(*) FROM usuarios')
    total = cursor.fetchone()[0]
    conn.close()
    return total

def listar_usuarios():
    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()
    cursor.execute('SELECT nome FROM usuarios')
    usuarios = cursor.fetchall()
    conn.close()
    return [u[0] for u in usuarios]

def remover_usuario(nome):
    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM usuarios WHERE nome = ?', (nome,))
    conn.commit()
    conn.close()
