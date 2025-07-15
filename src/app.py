import sys
import time
from pathlib import Path
from datetime import datetime
import os

# Permitir importações locais
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

# MODELS
from model.pedido import Pedido
from model.item import Item
from model.database import Database

# CONTROLLERS
from controler.pedidoControler import PedidoControler
from controler.itemControler import ItemControler
from controler.databaseControler import DatabaseControler
from controler.relatorioController import RelatorioControler

# VIEWS
from view.janela1 import Janela1
from view.janela2 import Janela2
from view.janela3 import Janela3

# REPORT
from report.pdf import PDF

# Inicia banco
database = Database('TESTE.db')
cursor = DatabaseControler.conect_database(database.name)

# Cria tabelas
DatabaseControler.create_table_itens(cursor)
DatabaseControler.create_table_pedidos(cursor)
DatabaseControler.create_table_itens_pedidos(cursor)

# Verifica se há itens no menu
menu_existente = ItemControler.mostrar_itens_menu(database.name)
if not menu_existente:
    print("📦 Carregando itens padrão no cardápio...")
    itens_padrao = [
        Item('Calabresa', 35.5, 'Pizza', 'Fatias de calabresa, molho de tomate, queijo'),
        Item('Mussarela', 30.0, 'Pizza', 'Muito queijo e molho'),
        Item('Frango', 32.0, 'Pizza', 'Frango desfiado, catupiry e milho'),
        Item('Refrigerante', 8.0, 'Bebida', 'Lata 350ml'),
        Item('Brownie', 12.5, 'Sobremesa', 'Brownie de chocolate com calda quente')
    ]
    for item in itens_padrao:
        ItemControler.insert_into_item(database.name, item)
    print("✅ Cardápio carregado com sucesso!\n")

# Interface de boas-vindas
print('''
                🍕 Bem-vindo ao sistema Pizza Mais 🍕
                     - Criando Sonhos -
                Estabelecimento: Pizza Ciclano
           "Seus sonhos têm formato e borda!"
                -----------------------------
            ''')

# Menu principal com opções em português
while True:
    print('''
    🍽️  1 - Cadastrar novo pedido
    🔍 2 - Consultar ou atualizar pedido
    📄 3 - Gerar relatório em PDF
    🆕 4 - Cadastrar novos itens no cardápio
    ❌ 5 - Encerrar o sistema
    ''')
    opcao = input('👉 Digite sua opção: ').strip()

    if opcao == '1':
        Janela1.mostrar_janela1(database.name)

    elif opcao == '2':
        Janela2.mostrar_janela2(database.name)

    elif opcao == '3':
        data_formatada = datetime.today().strftime('%d-%m-%Y')
        nome_arquivo = f"Relatorio_{data_formatada}.pdf"

        dados = RelatorioControler.preparar_dados_relatorio(database.name)

        print("\n📊 Faturamento total:", dados["faturamento_total"])
        print("📋 Quantidade de pedidos:", len(dados["pedidos"]))
        for pedido in dados["pedidos"]:
            print(f"→ Pedido #{pedido['id']} | Data: {pedido['data']} | Valor: R$ {pedido['valor']}")

        sucesso = PDF.gerar_pdf(nome_arquivo, dados["pedidos"], float(dados["faturamento_total"]))
        if sucesso:
            print(f"\n✅ Relatório gerado com sucesso: {nome_arquivo}")
            try:
                os.startfile(nome_arquivo)
            except Exception:
                print("📂 Relatório salvo na pasta do projeto. Abra manualmente.")
        else:
            print("❌ Houve um erro ao gerar o relatório.")

    elif opcao == '4':
        Janela3.mostrar_janela3(database.name)

    elif opcao == '5':
        confirma = input("Deseja realmente encerrar o sistema? (s/n): ").strip().lower()
        if confirma == 's':
            print("👋 Sistema encerrado. Até a próxima!")
            break
        elif confirma == 'n':
            print("🔁 Voltando ao menu principal...")
        else:
            print("⚠️ Entrada inválida. Digite 's' para sim ou 'n' para não.")

    else:
        print("⚠️ Opção inválida. Tente novamente.")

exit()
