from controler.pedidoControler import PedidoControler
from controler.itemControler import ItemControler

class Janela2:
    @staticmethod
    def mostrar_janela2(database_name: str):
        print("\n------ Consulta e Atualização de Pedido ------")
        print("1 - Consultar pedido por ID")
        print("2 - Listar todos os pedidos + faturamento")
        print("3 - Atualizar status de pedido")
        try:
            escolha = int(input("→ Digite o número da opção desejada: ").strip())
        except ValueError:
            print("❌ Entrada inválida.")
            return

        if escolha == 1:
            try:
                indice = int(input("🔍 Digite o ID do pedido: "))
                pedido_info = PedidoControler.search_in_pedidos_id(database_name, indice)
                if not pedido_info or isinstance(pedido_info, str):
                    print("❌ Pedido não encontrado.")
                    return
                itens = ItemControler.search_into_itens_pedidos_id(database_name, indice)
                print(f"\nResumo do Pedido #{indice}:")
                for item in itens:
                    print(f"  - Tipo: {item[2]} | Sabor: {item[0]} | Descrição: {item[3]} | R$ {item[1]:.2f}")
                print(f"\n🧾 Total de itens: {len(itens)}")
                print(f"📌 Status: {pedido_info[0][1]}")
                print(f"📦 Delivery: {pedido_info[0][2]}")
                print(f"🏠 Endereço: {pedido_info[0][3]}")
                print(f"📅 Data: {pedido_info[0][4]}")
                print(f"💰 Valor: R$ {pedido_info[0][5]:.2f}")
            except Exception:
                print("❌ Erro ao carregar pedido.")

        elif escolha == 2:
            pedidos = PedidoControler.search_in_pedidos_all(database_name)
            faturamento = 0
            print("\n📄 Lista de Pedidos:")
            for i, pedido in enumerate(pedidos, start=1):
                endereco = pedido.endereco or "Não informado"
                print(f"{i} - Status: {pedido.status} | Delivery: {pedido.delivery} | Endereço: {endereco} | R$ {pedido.valor_total:.2f}")
                faturamento += pedido.valor_total
            print(f"\n💸 Faturamento total: R$ {faturamento:.2f}")

        elif escolha == 3:
            try:
                indice = int(input("📍 Digite o ID do pedido para atualizar: "))
                pedido_info = PedidoControler.search_in_pedidos_id(database_name, indice)
                if not pedido_info:
                    print("❌ Pedido não encontrado.")
                    return
                novo_status = int(input("Escolha novo status: 1-preparo | 2-pronto | 3-entregue: "))
                if novo_status not in [1, 2, 3]:
                    print("❌ Status inválido.")
                    return
                atualizado = PedidoControler.update_pedido_status_id(database_name, indice, novo_status)
                print("✅ Status atualizado com sucesso!" if atualizado else "❌ Falha ao atualizar.")
            except ValueError:
                print("❌ Entrada inválida.")
        else:
            print("⚠️ Opção não reconhecida.")
