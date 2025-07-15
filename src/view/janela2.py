# 🛠️ Manutenção técnica por Luis Felipe Paiva em 15/07/2025: melhorias na lógica de consulta e atualização de pedidos

from controler.pedidoControler import PedidoControler
from controler.itemControler import ItemControler

class Janela2:
    @staticmethod
    def mostrar_janela2(database_name: str):
        print("\n🔄 ------ Consulta e Atualização de Pedidos ------")
        print("1️⃣  - Consultar pedido por ID")
        print("2️⃣  - Listar todos os pedidos + faturamento")
        print("3️⃣  - Atualizar status de um pedido")

        try:
            escolha = int(input("👉 Digite o número da opção desejada: ").strip())
        except ValueError:
            print("❌ Entrada inválida. Use apenas números.")
            return

        if escolha == 1:
            try:
                indice = int(input("🔍 Informe o ID do pedido que deseja consultar: "))
                pedido_info = PedidoControler.search_in_pedidos_id(database_name, indice)
                if not pedido_info or isinstance(pedido_info, str):
                    print("❌ Pedido não encontrado.")
                    return

                itens = ItemControler.search_into_itens_pedidos_id(database_name, indice)

                print(f"\n📦 Resumo do Pedido #{indice}:")
                for item in itens:
                    print(f"  🍕 Tipo: {item[2]} | Sabor: {item[0]} | Descrição: {item[3]} | Preço: R$ {item[1]:.2f}")
                print(f"\n🧾 Total de itens: {len(itens)}")
                print(f"📌 Status: {pedido_info[0][1]}")
                print(f"🚚 Delivery: {'Sim' if pedido_info[0][2] else 'Não'}")
                print(f"🏠 Endereço: {pedido_info[0][3]}")
                print(f"📅 Data: {pedido_info[0][4]}")
                print(f"💰 Valor Total: R$ {pedido_info[0][5]:.2f}")
            except Exception:
                print("❌ Erro ao carregar informações do pedido.")

        elif escolha == 2:
            pedidos = PedidoControler.search_in_pedidos_all(database_name)
            faturamento = 0
            print("\n📋 Lista de todos os pedidos:")
            for i, pedido in enumerate(pedidos, start=1):
                endereco = pedido.endereco if pedido.endereco else "Não informado"
                print(f"{i}️⃣ - Status: {pedido.status} | Delivery: {'Sim' if pedido.delivery else 'Não'} | Endereço: {endereco} | Total: R$ {pedido.valor_total:.2f}")
                faturamento += pedido.valor_total
            print(f"\n💸 Faturamento acumulado: R$ {faturamento:.2f}")

        elif escolha == 3:
            try:
                indice = int(input("🛠️ Digite o ID do pedido que deseja atualizar: "))
                pedido_info = PedidoControler.search_in_pedidos_id(database_name, indice)
                if not pedido_info:
                    print("❌ Pedido não encontrado.")
                    return

                print("\n📌 Selecione o novo status:")
                print("1 - Em preparo")
                print("2 - Pronto")
                print("3 - Entregue")
                try:
                    novo_status = int(input("Escolha: "))
                    status_map = {1: "preparo", 2: "pronto", 3: "entregue"}
                    status_novo = status_map.get(novo_status)
                    if not status_novo:
                        print("❌ Status inválido.")
                        return

                    atualizado = PedidoControler.update_pedido_status(database_name, indice, status_novo)
                    print("✅ Status atualizado com sucesso!" if atualizado else "❌ Não foi possível atualizar o status.")
                except ValueError:
                    print("❌ Entrada inválida. Digite um número de 1 a 3.")
            except ValueError:
                print("❌ Entrada inválida para ID.")
        else:
            print("⚠️ Opção não reconhecida. Tente novamente.")
