# Bookboxd - Diário Digital de Livros

Este projeto é um sistema de gerenciamento e avaliação de leituras desenvolvido como desafio prático para o processo seletivo da **LES (Liga de Engenharia de Software)**.

## Descrição do Projeto
O sistema funciona como um "Letterboxd para livros", permitindo organizar suas leituras de forma simples diretamente pelo terminal. O projeto atende a todos os critérios do edital:
- **Tema Livre:** Catálogo e review de livros.
- **Múltiplas Informações:** Nome do livro, Autor, Status (Lido, Não Lido, Próxima Leitura), Nota (em estrelas) e Resenha.
- **Campos Opcionais:** Permite pular o preenchimento de Autor, Nota ou Resenha apenas apertando Enter.
- **Operações CRUD:** Criação, leitura, atualização e remoção de registros de livros.
- **Persistência Binária:** Todos os dados são salvos de forma segura em formato binário utilizando a biblioteca nativa `pickle` do Python.

## Linguagem Utilizada
- **Python 3**

## Como Executar o Programa

1. Certifique-se de ter o Python instalado no seu computador.
2. Baixe o arquivo `les.py` deste repositório.
3. Abra o terminal na pasta onde o arquivo foi salvo e execute o comando:
```bash
python les.py
```

## Exemplos de Uso
- **Cadastrar livro lido:** Escolha a opção `1`, digite o nome do livro, mude o status para `1` (Lido) e insira sua nota e resenha.
- **Pular campos opcionais:** Ao cadastrar um livro que você ainda não leu, basta apertar `Enter` nos campos de Nota e Resenha para que o sistema salve automaticamente com o preenchimento `---`.
- **Persistência:** Feche o programa e abra-o novamente; ao selecionar a opção `2`, todas as suas entradas continuarão salvas no arquivo binário.
