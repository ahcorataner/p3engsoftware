

# 🍕 P3 Engenharia de Software — *Pizza Mais*  
**Sistema de Gerenciamento para Pizzarias**  

**Disciplina:** Engenharia de Software (P3)  
**Curso:** Engenharia da Computação  
**Instituição:** Universidade Federal do Maranhão (UFMA)  
**Desenvolvido por:** Renata Rocha  
**Versão do Python:** `3.10.9`  

> _"Seus sonhos têm formato e borda."_

---

## 🎓 Proposta Acadêmica

Este projeto foi desenvolvido como parte da avaliação da terceira prova da disciplina **Engenharia de Software**, no curso de **Engenharia da Computação** da **UFMA**.

O sistema simula um cenário real de **manutenção de software**, onde o cliente beta *Sr. Natanael* relata falhas e sugere melhorias após utilizar o sistema **Pizza Mais**, criado pela empresa fictícia **Criando Sonhos LTDA**.

---

## 📘 Descrição

**Pizza Mais** é um sistema de gerenciamento para pizzarias que permite:
- Cadastro de pedidos 🍕
- Consulta e atualização de pedidos 🔍
- Geração de relatórios em PDF 📄
- Inserção dinâmica de itens no menu 🧾

Este repositório corresponde à versão estável `v1.0`, publicada [aqui](https://github.com/ahcorataner/p3engsoftware/releases/tag/v1.0).

---

## 🧩 Objetivos do Projeto

- Diagnosticar falhas reais relatadas pelo cliente
- Aplicar manutenções corretivas, adaptativas e perfectivas
- Validar as correções com testes práticos
- Criar documentação clara para desenvolvedores e usuários

---

## 🛠️ Tecnologias Utilizadas

| Camada            | Ferramenta         |
|-------------------|--------------------|
| Linguagem         | Python 3.10.9      |
| Banco de Dados    | SQLite             |
| Relatórios        | ReportLab (PDF)    |
| Interface         | Terminal (CLI)     |
| Versionamento     | Git + GitHub       |

---

## 📁 Estrutura Atualizada

```plaintext
src/
├── app.py                         # Arquivo principal do sistema
├── model/                         # Modelos de dados
│   ├── __init__.py
│   ├── pedido.py
│   ├── item.py
│   └── database.py
├── controler/                     # Lógica de negócio
│   ├── __init__.py
│   ├── pedidoControler.py
│   ├── itemControler.py
│   ├── databaseControler.py
│   └── relatorioController.py
├── view/                          # Interface via terminal
│   ├── __init__.py
│   ├── janela1.py                 # Cadastro de pedido
│   ├── janela2.py                 # Consulta e atualização
│   └── janela3.py                 # Cadastro de itens
├── report/                        # Geração de relatórios
│   ├── __init__.py
│   └── pdf.py
└── TESTE.db                       # Banco SQLite gerado automaticamente
```

---

## 🚀 Como Executar o Projeto

### 1. Clonar o repositório
```bash
git clone https://github.com/ahcorataner/p3engsoftware.git
cd p3engsoftware/src
```

### 2. Instalar dependências
```bash
pip install reportlab
```

### 3. Executar o sistema
```bash
python app.py
```

---

## 🧪 Funcionalidades

- 📦 **Cadastro de pedidos com múltiplos itens**
- 🔍 **Consulta por ID ou listagem total**
- ✏️ **Atualização de status e validação de dados**
- 📄 **Relatórios em PDF com total de faturamento**
- ➕ **Cadastro interativo de novos itens no menu**

---

## 🔧 Manutenções Aplicadas

| Nº | Relato do Cliente                                 | Tipo         | Status              |
|----|---------------------------------------------------|--------------|---------------------|
| 1  | Menu confuso para o atendente                     | Perfectiva   | ✅ Corrigido         |
| 2  | Confirmação de pedido falha às vezes              | Corretiva    | ✅ Corrigido         |
| 3  | Itens não são adicionados corretamente             | Corretiva    | ✅ Corrigido         |
| 4  | Status do pedido não atualiza                     | Corretiva    | ✅ Corrigido         |
| 5  | Entradas inválidas travam sistema                 | Corretiva    | ✅ Corrigido         |
| 6  | Relatório não gera corretamente                   | Corretiva    | ✅ Corrigido         |
| 7  | Adição de novos itens ao menu via interface       | Adaptativa   | ✅ Implementado      |

---

## 📚 Aprendizados

Este projeto reforça os seguintes conceitos:
- Diagnóstico e resolução de bugs reais
- Aplicação de diferentes tipos de manutenção
- Boas práticas de estrutura de projeto
- Uso profissional de Git e versionamento
- Documentação técnica clara e funcional

---

## 📎 Licença

Este projeto é parte de um desafio acadêmico e **não possui fins comerciais**.

---

## 🤝 Contato

Desenvolvido por: **Renata Rocha**  
GitHub: [@ahcorataner](https://github.com/ahcorataner)

---


