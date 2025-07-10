import sys
import time
from pathlib import Path
from datetime import datetime
import os  # Para abrir o relatório automaticamente no Windows

# Ajuste para permitir importações de subpastas
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

# Inicializa banco e tabelas
database = Database('TESTE.db')
cursor = DatabaseControler.conect_database(database.name)

DatabaseControler.create_table_itens(cursor)
DatabaseControler.create_table_pedidos(cursor)
DatabaseControler.create_table_itens_pedidos(cursor)

# Cadastro automático de itens se o menu estiver vazio
menu_existente = ItemControler.mostrar_itens_menu(database.name)
if not menu_existente:
    print("📦 Carregando itens iniciais no menu...")
    item1 = Item('Calabresa', 35.5, 'Pizza', 'Fatias de calabresa, molho de tomate, queijo')
    item2 = Item('Mussarela', 30.0, 'Pizza', 'Muito queijo e molho')
    item3 = Item('Frango', 32.0, 'Pizza', 'Frango desfiado, catupiry e milho')
    item4 = Item('Refrigerante', 8.0, 'Bebida', 'Lata 350ml')
    item5 = Item('Brownie', 12.5, 'Sobremesa', 'Brownie de chocolate com calda quente')

    ItemControler.insert_into_item(database.name, item1)
    ItemControler.insert_into_item(database.name, item2)
    ItemControler.insert_into_item(database.name, item3)
    ItemControler.insert_into_item(database.name, item4)
    ItemControler.insert_into_item(database.name, item5)
    print("✅ Cardápio carregado com sucesso!\n")

# Interface do sistema
print('''
                Bem-vindo ao software Pizza Mais
                        -Criando Sonhos-
                Estabelecimento: Pizza Ciclano
                "Seus sonhos têm formato e borda"
                ---------------------------------
            ''')

# Menu principal
while True:
    print('''
    1 - Cadastrar Pedido
    2 - Consultar/Atualizar Pedido
    3 - Gerar Relatório em PDF
    4 - Cadastrar Itens no Menu
    5 - Encerrar
    ''')
    opcao = input('Digite sua opção: ').strip()

    if opcao == '1':
        Janela1.mostrar_janela1(database.name)

    elif opcao == '2':
        Janela2.mostrar_janela2(database.name)

    elif opcao == '3':
        data_formatada = datetime.today().strftime('%d-%m-%Y')
        nome_arquivo = f"Relatorio_{data_formatada}.pdf"
        dados = RelatorioControler.preparar_dados_relatorio(database.name)
        sucesso = PDF.gerar_pdf(nome_arquivo, dados["pedidos"], dados["faturamento_total"])
        if sucesso:
            print(f"✅ Relatório gerado com sucesso: {nome_arquivo}")
            try:
                os.startfile(nome_arquivo)  # Abre o PDF automaticamente no Windows
            except Exception:
                print("📂 Abra o relatório manualmente na pasta do projeto.")
        else:
            print("❌ Erro ao gerar o relatório.")

    elif opcao == '4':
        Janela3.mostrar_janela3(database.name)

    elif opcao == '5':
        print("👋 Encerrando o sistema. Até a próxima!")
        break

    else:
        print("⚠️ Opção inválida. Tente novamente.")

exit()
