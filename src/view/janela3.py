from controler.itemControler import ItemControler

class Janela3:
    @staticmethod
    def mostrar_janela3(database_name: str):
        print("\n--- Cadastro de Novo Item ---")
        nome = input("Nome do item: ").strip()
        descricao = input("Descrição: ").strip()

        try:
            preco = float(input("Preço (ex: 29.99): ").strip())
        except ValueError:
            print("❌ Preço inválido.")
            return

        print("Categoria: 1 - Pizza | 2 - Bebida | 3 - Sobremesa | 4 - Outro")
        categorias = {'1': 'Pizza', '2': 'Bebida', '3': 'Sobremesa', '4': 'Outro'}
        tipo = categorias.get(input("Digite o número: ").strip())

        if not nome or not descricao or preco <= 0 or not tipo:
            print("❌ Erro: campos obrigatórios ou inválidos.")
            return

        novo_item = ItemControler.create_item([nome, preco, tipo, descricao])
        if not novo_item:
            print("❌ Erro ao criar item.")
            return

        sucesso = ItemControler.insert_into_item(database_name, novo_item)
        print("✅ Item cadastrado!" if sucesso else "❌ Falha ao salvar item.")
