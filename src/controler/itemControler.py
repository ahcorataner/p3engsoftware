# Manutenção: Weslly Silveira - tarefa concluída em 11/07/2025

from model.item import Item

class ItemControler:
    @staticmethod
    def mostrar_itens_menu(database_name: str):
        return Item.mostrar_itens_menu(database_name)

    @staticmethod
    def insert_into_item(database_name: str, data):
        return Item.insert_into_item(database_name, data)

    @staticmethod
    def insert_into_itens_pedidos(database_name: str, data):
        return Item.insert_into_itens_pedidos(database_name, data)

    @staticmethod
    def search_into_itens_pedidos_id(database_name: str, indice: int):
        return Item.search_into_itens_pedidos_id(database_name, indice)

    @staticmethod
    def valor_item(database_name: str, indice: int):
        return Item.valor_item(database_name, indice)

    @staticmethod
    def search_item_id(database_name: str, indice: int):
        return Item.search_item_id(database_name, indice)

    @staticmethod
    def create_item(data: list):
        if not all(data) or len(data) < 4:
            return False
        try:
            return Item(data[0], float(data[1]), data[2], data[3])
        except Exception as e:
            print(f"Erro ao criar item: {e}")
            return False
