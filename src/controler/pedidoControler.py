from model.pedido import Pedido

class PedidoControler:
    @staticmethod
    def insert_into_pedidos(database_name: str, data):
        return Pedido.insert_into_pedidos(database_name, data)

    @staticmethod
    def search_in_pedidos_all(database_name: str):
        resultado_bruto = Pedido.search_in_pedidos_all(database_name)
        resultado_obj = []
        for row in resultado_bruto:
            pedido = Pedido(
                status=row[1],
                delivery=bool(row[2]),
                endereco=row[3],
                date=row[4],
                valor_total=row[5]
            )
            resultado_obj.append(pedido)
        return resultado_obj

    @staticmethod
    def search_in_pedidos_id(database_name: str, indice: int):
        return Pedido.search_in_pedidos_id(database_name, indice)

    @staticmethod
    def update_pedido_status_id(database_name: str, indice: int, status: int):
        status_map = {1: "preparo", 2: "pronto", 3: "entregue"}
        novo_status = status_map.get(status)
        if not novo_status:
            return False
        return Pedido.update_pedido_status(database_name, indice, novo_status)

    @staticmethod
    def get_id_all(database_name: str):
        resultado_raw = Pedido.get_id_all(database_name)
        return [row[0] for row in resultado_raw]
