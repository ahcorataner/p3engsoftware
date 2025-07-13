# Manutenção: Cícero Tasso - Validação aprimorada em 13/07/2025

from controler.itemControler import ItemControler

class Janela3:
    @staticmethod
    def mostrar_janela3(database_name: str):
        print("\n🆕 --- Cadastro de Novo Item no Cardápio ---")

        nome = input("📛 Nome do item: ").strip()
        descricao = input("📝 Descrição do item: ").strip()

        try:
            preco = float(input("💰 Preço (ex: 29.99): ").strip())
        except ValueError:
            print("❌ Preço inválido. Digite apenas números usando ponto para centavos.")
            return

        print("\n🍴 Categoria do item:")
        print("1️⃣ - Pizza")
        print("2️⃣ - Bebida")
        print("3️⃣ - Sobremesa")
        print("4️⃣ - Outro")
        categorias = {'1': 'Pizza', '2': 'Bebida', '3': 'Sobremesa', '4': 'Outro'}
        tipo = categorias.get(input("👉 Escolha o número da categoria: ").strip())

        if not nome or not descricao or preco <= 0 or not tipo:
            print("❌ Erro: Todos os campos são obrigatórios e devem ser válidos.")
            return

        novo_item = ItemControler.create_item([nome, preco, tipo, descricao])
        if not novo_item:
            print("❌ Erro ao criar o item.")
            return

        sucesso = ItemControler.insert_into_item(database_name, novo_item)
        if sucesso:
            print(f"\n✅ Item '{nome}' cadastrado com sucesso na categoria {tipo}!")
        else:
            print("❌ Falha ao salvar o item no banco de dados.")
