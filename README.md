# 🍕 Pizza Mais – Sistema de Gerenciamento para Pizzarias

**Repositório:** `p3engsoftware`  
**Disciplina:** Engenharia de Software (P3)  
**Curso:** Engenharia da Computação  
**Instituição:** Universidade Federal do Maranhão (UFMA)  
**Desenvolvido por:** Renata Rocha
**Versão do Python:** 3.10.9

> “Seus sonhos têm formato e borda.”

---

## 🎓 Proposta Acadêmica

Este projeto foi desenvolvido como parte da avaliação da **P3 (terceira prova)** da disciplina de **Engenharia de Software**, no curso de **Engenharia da Computação** da **Universidade Federal do Maranhão (UFMA)**.

A proposta consiste em simular um cenário real de manutenção de software (originalmente disponível em https://github.com/miqueiaspcoelho/CriandoSonhosLTDA.git), no qual um cliente beta (Sr. Natanael) relatou uma série de falhas e sugestões de melhoria após utilizar o sistema “Pizza Mais” em seu restaurante.

---

## 📘 Descrição do Projeto

O sistema **Pizza Mais** é um software de gerenciamento para pizzarias, desenvolvido pela empresa fictícia **Criando Sonhos LTDA**. Após a implantação, o cliente relatou dificuldades que afetam a experiência dos atendentes e a eficiência do serviço.

O desafio proposto é:

- Analisar os relatos do cliente
- Identificar o tipo de manutenção necessária
- Implementar as correções e melhorias
- Validar as soluções com testes
- Documentar todo o processo com clareza

---

## 🧩 Objetivos do Desenvolvedor

- ✅ Diagnosticar os problemas relatados
- 🔧 Classificar e aplicar manutenções:
  - **Corretiva** – corrigir falhas
  - **Adaptativa** – adaptar a novos requisitos
  - **Perfectiva** – melhorar usabilidade
- 🧪 Testar e validar as soluções
- 📝 Documentar com boas práticas de engenharia de software

---

## 🛠️ Tecnologias Utilizadas

| Camada        | Ferramenta         |
|---------------|--------------------|
| Linguagem     | Python 3.10.9      |
| Banco de Dados| SQLite             |
| Relatórios    | ReportLab (PDF)    |
| Interface     | Terminal (CLI)     |

---

## 📁 Estrutura do Projeto

```plaintext
src/
├── app.py               # Arquivo principal
├── model/               # Modelos de dados (Pedido, Item, etc.)
│   ├── __init__.py
│   ├── pedido.py
│   ├── item.py
│   └── database.py
├── controller/          # Lógica de controle e persistência
│   ├── __init__.py
│   ├── pedidoControler.py
│   ├── itemControler.py
│   ├── databaseControler.py
│   └── relatorioController.py
├── view/                # Interface via terminal
│   ├── __init__.py
│   ├── janela1.py
│   └── janela2.py
├── report/              # Geração de relatórios PDF
│   ├── __init__.py
│   └── relatorio1.py
└── TESTE.db             # Banco de dados local

## 🚀 Como Executar o Projeto

1. Clone o repositório (originalmente em https://github.com/miqueiaspcoelho/CriandoSonhosLTDA.git)
bash
git clone https://github.com/seu-usuario/p3engsoftware.git
cd p3engsoftware/src

2. Instale a dependência
bash
pip install reportlab

3. Execute o sistema
bash
python app.py

## 🧪 Funcionalidades

- 📦 **Cadastro de pedidos**
- 🔍 **Pesquisa e atualização de pedidos**
- 📄 **Geração de relatórios em PDF**
- ➕ **Inserção de novos itens no menu** *(em desenvolvimento)*
- 🛠️ **Validações e mensagens de erro aprimoradas**

---

## 📌 Status das Manutenções

| Nº | Problema Relatado                                       | Tipo de Manutenção | Status               |
|----|----------------------------------------------------------|---------------------|----------------------|
| 1  | Menu confuso no cadastro de pedidos                     | Perfectiva          | ✅ Resolvido          |
| 2  | Confirmação de pedido falha às vezes                    | Corretiva           | 🔧 Em andamento       |
| 3  | Adição de item ao pedido falha                          | Corretiva           | 🔧 Em andamento       |
| 4  | Status do pedido salva errado                           | Corretiva           | 🔧 Em andamento       |
| 5  | Sistema não responde a entradas inválidas               | Corretiva           | 🔧 Em andamento       |
| 6  | Atualização de status não funciona                      | Corretiva           | 🔧 Em andamento       |
| 7  | Criar tela para cadastrar novos itens no menu           | Adaptativa          | 🛠️ Em desenvolvimento |


🧠 Aprendizados
Este projeto reforça conceitos fundamentais de manutenção de software, como:
Diagnóstico de bugs reais
Classificação de manutenções
Validação de entradas
Boas práticas de versionamento e documentação

📎 Licença
Este projeto é parte de um desafio acadêmico e não possui fins comerciais.

🤝 Contato
Desenvolvido por Renata Rocha 🔗 github.com/ahcorataner

