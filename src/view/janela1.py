from datetime import date
import time
from controler.pedidoControler import PedidoControler
from controler.itemControler import ItemControler
from model.pedido import Pedido

class Janela1:
    @staticmethod
    def mostrar_janela1(database_name: str) -> None:
        while True:
            menu = ItemControler.mostrar_itens_menu(database_name)

            if not menu:
                print("⚠️ O cardápio está vazio. Cadastre itens antes de realizar pedidos.")
                break

            print("\n🍽️ ---------- Cardápio Disponível ----------")
            print("ID | Nome         | Tipo        | Preço   | Descrição")
            print("---|--------------|-------------|---------|-------------------------------")
            for item in menu:
                print(f"{item[0]:<3}| {item[1]:<12} | {item[3]:<11} | R${item[2]:<7.2f} | {item[4]}")

            a = input('\nDeseja cadastrar um novo pedido? (s/n): ').strip().lower()
            if a != 's':
                print('↩️ Retornando ao menu principal...')
                time.sleep(1)
                break

            lista_itens = []
            valor_total = 0.0
            pedidos = PedidoControler.search_in_pedidos_all(database_name)
            numero_pedido = len(pedidos) + 1

            while True:
                try:
                    item = int(input('Informe o ID do item: '))
                    quantidade = int(input('Quantidade: '))
                    preco_info = ItemControler.valor_item(database_name, item)
                    if not preco_info or isinstance(preco_info, str):
                        print("❌ Item inválido. Tente novamente.")
                        continue

                    valor_unitario = preco_info[0][0]
                    valor_total += valor_unitario * quantidade
                    lista_itens += [(numero_pedido, item)] * quantidade
                except ValueError:
                    print("❌ Entrada inválida. Digite apenas números.")
                    continue

                adicionar = input('Deseja adicionar mais itens? (s/n): ').strip().lower()
                if adicionar != 's':
                    break

            delivery_input = input("O pedido é para delivery? (s/n): ").strip().lower()
            if delivery_input not in ['s', 'n']:
                print("❌ Entrada inválida. Digite 's' para sim ou 'n' para não.")
                continue
            delivery_flag = delivery_input == 's'

            endereco = input("Informe o endereço de entrega: ").strip()

            try:
                status_aux = int(input('Informe o status do pedido:\n1 - Em preparo\n2 - Pronto\n3 - Entregue\nEscolha: '))
                status_map = {1: "preparo", 2: "pronto", 3: "entregue"}
                status = status_map.get(status_aux)
                if not status:
                    print("❌ Opção de status inválida. Tente novamente.")
                    continue
            except ValueError:
                print("❌ Entrada inválida. Digite um número de 1 a 3.")
                continue

            data_formatada = date.today().strftime('%d/%m/%Y')
            pedido = Pedido(status, delivery_flag, endereco, data_formatada, float(valor_total))
            PedidoControler.insert_into_pedidos(database_name, pedido)

            for item_pedido in lista_itens:
                ItemControler.insert_into_itens_pedidos(database_name, item_pedido)

            print(f"\n✅ Pedido #{numero_pedido} cadastrado com sucesso!")
            print(f"🧾 Valor total: R$ {valor_total:.2f}")
            print("----------------------------------------------------")
