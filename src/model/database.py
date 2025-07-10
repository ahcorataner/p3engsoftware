import sqlite3
from sqlite3 import Error

class Database:
    def __init__(self, name: str) -> None:
        self.name = name
        try:
            conn = sqlite3.connect(self.name)
            conn.execute('PRAGMA foreign_keys = ON;')
        except Error as e:
            print(f"Erro ao inicializar o banco: {e}")

    @staticmethod
    def conect_database(database_name: str):
        try:
            conn = sqlite3.connect(database_name)
            return conn
        except Error as e:
            print(f"Erro na conexão com o banco: {e}")
            return None

    @staticmethod
    def create_table_itens(cursor):
        try:
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS Itens (
                    IdItens INTEGER PRIMARY KEY AUTOINCREMENT,
                    Nome VARCHAR(30),
                    Preco REAL,
                    Tipo VARCHAR(30),
                    Descricao VARCHAR(255),
                    CONSTRAINT Produto_Unique UNIQUE (Nome)
                );
            ''')
            return True
        except Error as e:
            print(f"Erro ao criar tabela Itens: {e}")
            return False

    @staticmethod
    def create_table_pedidos(cursor):
        try:
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS Pedidos (
                    IdPedido INTEGER PRIMARY KEY AUTOINCREMENT,
                    Status VARCHAR(30) NOT NULL,
                    Delivery INTEGER,
                    Endereco VARCHAR(100),
                    date VARCHAR(30),  -- CORRIGIDO: nome da coluna agora é 'date'
                    ValorTotal REAL NOT NULL
                );
            ''')
            return True
        except Error as e:
            print(f"Erro ao criar tabela Pedidos: {e}")
            return False

    @staticmethod
    def create_table_itens_pedidos(cursor):
        try:
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS ItensPedidos (
                    Id INTEGER PRIMARY KEY AUTOINCREMENT,
                    IdPedido INTEGER NOT NULL,
                    IdItem INTEGER NOT NULL,
                    FOREIGN KEY(IdPedido) REFERENCES Pedidos(IdPedido),
                    FOREIGN KEY(IdItem) REFERENCES Itens(IdItens)
                );
            ''')
            return True
        except Error as e:
            print(f"Erro ao criar tabela ItensPedidos: {e}")
            return False
