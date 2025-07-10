from sqlite3 import Error
from model.database import Database

class Item:
    def __init__(self, nome: str, preco: float, tipo: str, descricao: str) -> None:
        self.nome = nome
        self.preco = preco
        self.tipo = tipo
        self.descricao = descricao

    @staticmethod
    def mostrar_itens_menu(database_name: str):
        try:
            with Database.conect_database(database_name) as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM Itens;")
                return cursor.fetchall()
        except Error as e:
            print(f"Erro ao mostrar itens do menu: {e}")
            return []

    @staticmethod
    def insert_into_item(database_name: str, data):
        try:
            with Database.conect_database(database_name) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT INTO Itens (Nome, Preco, Tipo, Descricao) VALUES (?, ?, ?, ?);
                ''', (data.nome, data.preco, data.tipo, data.descricao))
                conn.commit()
                return True
        except Error as e:
            print(f"Erro ao inserir item: {e}")
            return False

    @staticmethod
    def insert_into_itens_pedidos(database_name: str, data):
        try:
            with Database.conect_database(database_name) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT INTO ItensPedidos (IdPedido, IdItem) VALUES (?, ?);
                ''', (data[0], data[1]))
                conn.commit()
                return True
        except Error as e:
            print(f"Erro ao vincular item a pedido: {e}")
            return False

    @staticmethod
    def search_into_itens_pedidos_id(database_name: str, indice: int):
        try:
            with Database.conect_database(database_name) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    SELECT i.Nome, i.Preco, i.Tipo, i.Descricao
                    FROM Pedidos p
                    LEFT JOIN ItensPedidos ip ON ip.IdPedido = p.IdPedido
                    LEFT JOIN Itens i ON ip.IdItem = i.IdItens
                    WHERE p.IdPedido = ?;
                ''', (indice,))
                return cursor.fetchall()
        except Error as e:
            print(f"Erro ao buscar itens do pedido: {e}")
            return []

    @staticmethod
    def valor_item(database_name: str, indice: int):
        try:
            with Database.conect_database(database_name) as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT Preco FROM Itens WHERE IdItens = ?;", (indice,))
                return cursor.fetchall()
        except Error as e:
            print(f"Erro ao buscar valor do item: {e}")
            return []

    @staticmethod
    def search_item_id(database_name: str, indice: int):
        try:
            with Database.conect_database(database_name) as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT Nome, Tipo, Descricao, Preco FROM Itens WHERE IdItens = ?;", (indice,))
                return cursor.fetchall()
        except Error as e:
            print(f"Erro ao buscar item por ID: {e}")
            return []
