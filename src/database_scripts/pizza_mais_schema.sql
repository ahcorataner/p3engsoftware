-- 📦 Tabela de pedidos
CREATE TABLE Pedidos (
    IdPedido INTEGER PRIMARY KEY AUTOINCREMENT,
    Status VARCHAR(30) NOT NULL,
    Delivery INTEGER,
    Endereco VARCHAR(100),
    date VARCHAR(30),
    ValorTotal REAL NOT NULL
);

-- 🍕 Tabela de itens do menu
CREATE TABLE Itens (
    IdItens INTEGER PRIMARY KEY AUTOINCREMENT,
    Nome VARCHAR(30),
    Preco REAL,
    Tipo VARCHAR(30),
    Descricao VARCHAR(255),
    CONSTRAINT Produto_Unique UNIQUE (Nome)
);

-- 🔗 Relação entre pedidos e itens
CREATE TABLE ItensPedidos (
    Id INTEGER PRIMARY KEY AUTOINCREMENT,
    IdPedido INTEGER NOT NULL,
    IdItem INTEGER NOT NULL,
    FOREIGN KEY (IdPedido) REFERENCES Pedidos(IdPedido),
    FOREIGN KEY (IdItem) REFERENCES Itens(IdItens)
);

-- Itens do cardápio padrão
INSERT INTO Itens (Nome, Preco, Tipo, Descricao) VALUES
('Calabresa', 35.90, 'Pizza', 'Calabresa fatiada, cebola roxa e queijo mussarela'),
('Frango com Catupiry', 36.50, 'Pizza', 'Frango desfiado com catupiry tradicional'),
('Mussarela', 32.00, 'Pizza', 'Queijo mussarela com orégano'),
('Brownie', 12.00, 'Sobremesa', 'Brownie de chocolate com calda quente'),
('Refrigerante 2L', 8.50, 'Bebida', 'Refrigerante cola 2 litros'),
('Suco Natural', 6.00, 'Bebida', 'Suco de frutas natural da casa');
