# Bookboxd - Diário Digital de Livros

Este projeto é um sistema de gerenciamento e avaliação de leituras desenvolvido como desafio prático para o processo seletivo da **LES (Liga de Engenharia de Software)**.

## Descrição do Projeto
O sistema funciona como um "Letterboxd para livros", permitindo organizar suas leituras de forma simples diretamente pelo terminal. O projeto atende integralmente a todos os critérios do edital.

## Funcionalidades (CRUD)
- **Cadastrar Livro:** Permite a inserção de novas leituras no diário.
- **Listar Livros:** Exibe de forma estruturada todos os registros salvos.
- **Editar Registro:** Permite alterar as informações de um livro através do ID.
- **Remover Livro:** Exclui um registro permanentemente do arquivo, contando com uma etapa de confirmação de segurança.
- **Validação de Dados:** Mecanismo rígido que impede campos vazios, filtra entradas inválidas no ID e garante que os nomes contenham letras e as notas fiquem estritamente entre 1 e 5.

## Dados Cadastrados
Cada livro armazenado no sistema possui:
- ID (Gerado de forma automática através da lógica de maior ID, evitando duplicidade)
- Nome do Livro
- Autor
- Nota de avaliação (Filtro numérico de 1 a 5)

## Tecnologias Utilizadas
- **Python 3** (Utilizando a biblioteca padrão `pickle` para a persistência em arquivo binário `bookboxd.dat`).

## Como Executar o Programa

1. Certifique-se de ter o Python instalado no seu computador.
2. Baixe o arquivo `les.py` deste repositório.
3. Abra o terminal na pasta onde o arquivo foi salvo e execute o comando:
```bash
python les.py
```

## Exemplos de Uso
- **Tratamento de Erros:** Ao selecionar a opção `1`, se tentar deixar o nome ou autor em branco, ou inserir uma nota fora do limite, o sistema apontará o erro e exigirá a digitação correta em loop antes de salvar.
- **Exibição Prévia de IDs:** Ao escolher as opções `3` (Editar) ou `4` (Remover), o programa exibe automaticamente a lista de livros cadastrados com seus respectivos IDs antes de solicitar a ação, facilitando a escolha e validando o ID inserido.
- **Confirmação de Exclusão:** Na opção `4`, após inserir o ID, o sistema exibe o nome do livro e exige que o usuário digite explicitamente a palavra "sim" para confirmar a remoção, evitando exclusões acidentais.
- **Persistência Binária:** Você pode fechar o terminal e abrir o programa novamente; ao selecionar a opção `2`, todas as suas leituras continuarão salvas perfeitamente através do arquivo de dados.
