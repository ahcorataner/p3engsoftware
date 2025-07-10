# Manutenção: Cícero Tasso - revisão em 10/07/2025

from sqlite3 import Error
from model.database import Database

class Pedido:
    def __init__(self, status: str, delivery: bool, endereco: str, date: str, valor_total: float) -> None:
        self.status = status
        self.delivery = delivery
        self.endereco = endereco
        self.date = date
        self.valor_total = valor_total

    @staticmethod
    def insert_into_pedidos(database_name: str, data: object) -> bool:
        """
        Insere um novo pedido no banco de dados.
        """
        try:
            with Database.conect_database(database_name) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT INTO Pedidos (Status, Delivery, Endereco, date, ValorTotal)
                    VALUES (?, ?, ?, ?, ?);
                ''', (data.status, int(data.delivery), data.endereco, data.date, data.valor_total))
                conn.commit()
                return True
        except Error as e:
            print(f"❌ Erro ao inserir pedido: {e}")
            return False

    @staticmethod
    def search_in_pedidos_all(database_name: str) -> list:
        """
        Busca todos os pedidos no banco.
        """
        try:
            with Database.conect_database(database_name) as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM Pedidos ORDER BY IdPedido ASC;")
                return cursor.fetchall()
        except Error as e:
            print(f"❌ Erro ao buscar todos os pedidos: {e}")
            return []

    @staticmethod
    def search_in_pedidos_id(database_name: str, indice: int) -> list:
        """
        Busca um pedido específico pelo ID.
        """
        try:
            with Database.conect_database(database_name) as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM Pedidos WHERE IdPedido = ?;", (indice,))
                return cursor.fetchall()
        except Error as e:
            print(f"❌ Erro ao buscar pedido por ID: {e}")
            return []

    @staticmethod
    def update_pedido_status(database_name: str, indice: int, status: str) -> bool:
        """
        Atualiza o status de um pedido específico.
        """
        try:
            with Database.conect_database(database_name) as conn:
                cursor = conn.cursor()
                cursor.execute("UPDATE Pedidos SET Status = ? WHERE IdPedido = ?;", (status, indice))
                conn.commit()
                return True
        except Error as e:
            print(f"❌ Erro ao atualizar status do pedido: {e}")
            return False

    @staticmethod
    def get_id_all(database_name: str) -> list:
        """
        Retorna todos os IDs dos pedidos.
        """
        try:
            with Database.conect_database(database_name) as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT IdPedido FROM Pedidos ORDER BY IdPedido ASC;")
                return cursor.fetchall()
        except Error as e:
            print(f"❌ Erro ao buscar IDs dos pedidos: {e}")
            return []
