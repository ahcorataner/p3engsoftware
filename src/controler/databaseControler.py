from model.database import Database

class DatabaseControler:
    @staticmethod
    def conect_database(database_name: str) -> object:
        """
        Responsável por criar uma conexão com o banco de dados.

        :param database_name: Nome do banco.
        :return: Conexão com o banco.
        """
        Database(database_name)
        conn = Database.conect_database(database_name)
        return conn

    @staticmethod
    def create_table_itens(conn: object) -> bool:
        """
        Cria a tabela de itens, caso não exista.

        :param conn: Conexão com o banco.
        :return: Resultado da criação.
        """
        return Database.create_table_itens(conn)

    @staticmethod
    def create_table_pedidos(conn: object) -> bool:
        """
        Cria a tabela de pedidos, caso não exista.

        :param conn: Conexão com o banco.
        :return: Resultado da criação.
        """
        return Database.create_table_pedidos(conn)

    @staticmethod
    def create_table_itens_pedidos(conn: object) -> bool:
        """
        Cria a tabela de itens_pedidos, caso não exista.

        :param conn: Conexão com o banco.
        :return: Resultado da criação.
        """
        return Database.create_table_itens_pedidos(conn)
