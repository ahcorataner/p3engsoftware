# 📄 RELATÓRIO – Projeto Pizza Mais

**Disciplina:** Engenharia de Software (P3)  
**Curso:** Engenharia da Computação  
**Instituição:** Universidade Federal do Maranhão (UFMA)  
**Desenvolvido por:** Renata  
**Repositório:** [github.com/ahcorataner/p3engsoftware](https://github.com/ahcorataner/p3engsoftware)

---

## 🧭 Introdução

Este relatório apresenta a análise, planejamento e execução das manutenções realizadas no sistema **Pizza Mais**, como parte da avaliação da terceira prova (P3) da disciplina de **Engenharia de Software**.

O sistema foi implantado em um ambiente real de testes com um cliente beta, que relatou uma série de dificuldades e sugestões de melhoria. A proposta do trabalho é simular o papel de um analista e desenvolvedor de software, responsável por diagnosticar, classificar e corrigir os problemas identificados.

---

## 📝 Objetivos

- Analisar os relatos do cliente
- Classificar os problemas conforme o tipo de manutenção: corretiva, adaptativa ou perfectiva
- Propor e implementar soluções técnicas
- Testar e validar as correções
- Documentar o processo com clareza e boas práticas

---

## 💬 Relatos do Cliente

Os relatos foram organizados em três momentos distintos:

### 📌 Cadastro de Pedidos (02/12/2024)
1. Menu confuso na hora de cadastrar um novo pedido
2. Confirmação de cadastro falhando
3. Problema ao adicionar novo item ao pedido
4. Erros ao salvar o status do pedido
5. Falta de resposta com entradas erradas

### 📌 Pesquisa e Atualização de Pedidos (09/04/2025)
6. Atualização de status não funciona e não exibe mensagem

### 📌 Cadastro de Itens no Menu (01/05/2025)
7. Solicitação de uma nova tela para cadastrar itens no cardápio

---

## 🛠️ Classificação das Manutenções

| Nº | Problema Relatado                                       | Tipo de Manutenção |
|----|----------------------------------------------------------|---------------------|
| 1  | Menu confuso no cadastro de pedidos                     | Perfectiva          |
| 2  | Confirmação de cadastro falhando                        | Corretiva           |
| 3  | Adição de item ao pedido falha                          | Corretiva           |
| 4  | Status do pedido salva errado                           | Corretiva           |
| 5  | Sistema não responde a entradas inválidas               | Corretiva           |
| 6  | Atualização de status não funciona                      | Corretiva           |
| 7  | Criar tela para cadastrar novos itens no menu           | Adaptativa          |

---

## 🗂️ Apêndice Técnico – Histórico de Manutenções

| Nº | Descrição do Problema ou Solicitação                                                     | Tipo de Manutenção | Ação Esperada                                                                 |
|----|-------------------------------------------------------------------------------------------|---------------------|-------------------------------------------------------------------------------|
| 1  | Melhorar o layout do menu principal para torná-lo mais claro, organizado e acessível     | Perfectiva          | Reformular a interface do menu com espaçamento, ícones e texto mais amigável |
| 2  | Entrada para confirmar o cadastro de novo pedido não funciona em alguns casos            | Corretiva           | Corrigir o fluxo de validação para confirmar pedidos com entrada segura       |
| 3  | Ao adicionar novo item ao pedido, a confirmação falha ocasionalmente                     | Corretiva           | Revisar a lógica de confirmação de itens e garantir correta associação        |
| 4  | Faturamento não aparece corretamente no relatório PDF, mesmo com pedidos válidos         | Corretiva           | Ajustar cálculo e formatação de valores na geração do PDF                     |
| 5  | O sistema não apresenta nenhuma resposta ao cadastrar pedido (y-Sim, n-Nao)              | Corretiva           | Implementar validações e mensagens de erro interativas ao usuário            |
| 6  | Ao tentar atualizar o status de um pedido, nenhuma ação ocorre                           | Corretiva           | Corrigir o método de atualização e assegurar feedback visível ao usuário     |
| 7  | Cliente solicita a criação de uma nova tela para cadastrar novos itens no menu           | Adaptativa          | Implementar uma nova view conectada aos models e controllers de itens        |

---

## 🔍 Estratégia de Correção

Cada problema foi analisado individualmente, com foco em:

- Identificar a causa provável
- Corrigir a lógica ou a interface
- Validar a entrada do usuário
- Exibir mensagens claras de erro ou sucesso
- Testar o sistema após cada alteração

---

## 💡 Destaques Técnicos

- Refatoração da interface de cadastro para exibir os itens disponíveis
- Normalização de entradas com `.strip().lower()` para evitar falhas em confirmações
- Criação planejada da `Janela3` para cadastro de novos itens no menu
- Correção da lógica de atualização de status na `Janela2`
- Implementação de mensagens de erro para entradas inválidas

---

## ✅ Resultados

- O sistema passou a oferecer uma experiência mais clara e confiável para os atendentes
- Os principais bugs foram identificados e estão sendo corrigidos com commits organizados
- A documentação foi mantida atualizada no repositório GitHub

---

## 📎 Conclusão

O projeto permitiu aplicar na prática os conceitos de manutenção de software, engenharia de requisitos, usabilidade e versionamento. A simulação de um cenário real com cliente trouxe uma dimensão importante de empatia e comunicação técnica.

---

## 🔗 Repositório

Todo o código, documentação e histórico de commits estão disponíveis em:  
[https://github.com/ahcorataner/p3engsoftware](https://github.com/ahcorataner/p3engsoftware)
