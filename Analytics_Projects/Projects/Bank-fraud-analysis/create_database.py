import sqlite3

# Cria / conecta ao banco de dados "banco.db"
conexao = sqlite3.connect("banco.db")
cursor = conexao.cursor()

# Criação das tabelas
cursor.execute('''
CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    cpf TEXT NOT NULL UNIQUE,
    renda REAL
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS transacoes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cliente_id INTEGER,
    valor REAL,
    tipo TEXT,
    data TEXT,
    FOREIGN KEY(cliente_id) REFERENCES clientes(id)
);
''')

conexao.commit()
conexao.close()

print("Banco de dados criado com sucesso!")