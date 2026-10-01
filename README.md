Bookboxd - Diário Digital de Livros
Este projeto é um sistema de gerenciamento e avaliação de leituras desenvolvido como desafio prático para o processo seletivo da LES (Liga de Engenharia de Software).
Descrição do Projeto
O sistema funciona como um "Letterboxd para livros", permitindo organizar suas leituras de forma simples diretamente pelo terminal. O projeto atende a todos os critérios do edital:
• Tema Livre: Catálogo e review de livros.
• Múltiplas Informações: Nome do livro, Autor e Nota.
• Validação Rígida: Não permite campos em branco. O sistema obriga o preenchimento de todas as informações e valida se os nomes contêm letras e se as notas estão estritamente entre 1 e 5.
• Operações CRUD: Criação, leitura (listagem), atualização e remoção de registros de livros.
• Persistência Binária: Todos os dados são salvos de forma segura em formato binário utilizando a biblioteca nativa pickle do Python, gerando o arquivo dados.dat.
Linguagem Utilizada
• Python 3
Como Executar o Programa
1. Certifique-se de ter o Python instalado no seu computador.
2. Baixe o arquivo les.py deste repositório.
3. Abra o terminal na pasta onde o arquivo foi salvo e execute o comando:
bash
python les.py
Use o código com cuidado.
Exemplos de Uso
• Cadastrar livro: Selecione a opção 1, insira o nome do livro, o autor e uma nota de 1 a 5. Se tentar deixar em branco ou digitar dados inválidos (como apenas símbolos ou números no nome), o sistema apontará o erro e exigirá a digitação correta.
• Editar ou Remover: Ao escolher as opções 3 ou 4, o programa exibe automaticamente a lista de livros disponíveis com seus respectivos IDs antes de solicitar a ação. Caso digite um ID inexistente ou inválido, o sistema avisa e pede para inserir o ID correto em loop, sem interromper o fluxo.
• Persistência: Você pode fechar o terminal e abrir o programa novamente; ao selecionar a opção 2, todas as suas leituras continuarão salvas perfeitamente através do arquivo binário.

