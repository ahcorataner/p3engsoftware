from controler.pedidoControler import PedidoControler
from controler.itemControler import ItemControler

class RelatorioControler:
    @staticmethod
    def preparar_dados_relatorio(database_name: str) -> dict:
        pedidos_ids = PedidoControler.get_id_all(database_name)
        pedidos_detalhados = PedidoControler.search_in_pedidos_all(database_name)
        dados_relatorio = []
        faturamento_total = 0

        for id_pedido, pedido in zip(pedidos_ids, pedidos_detalhados):
            itens = ItemControler.search_into_itens_pedidos_id(database_name, id_pedido)
            dados_relatorio.append({
                "id": id_pedido,
                "data": pedido.date,
                "valor": pedido.valor_total,
                "itens": itens
            })
            faturamento_total += pedido.valor_total

        return {
            "pedidos": dados_relatorio,
            "faturamento_total": round(faturamento_total, 2)
        }
