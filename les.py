import os
import pickle

ARQUIVO = "bookboxd.dat"

while True:
    print("=== BOOKBOXD ===\n1-Adicionar livro\n2-Listar livros\n3-Editar livro\n4-Remover livro\n5-Sair")
    opcao = input("Opção: ")

    if opcao == "1":
        if os.path.exists(ARQUIVO):
            arq = open(ARQUIVO, "rb")
            livros = pickle.load(arq)
            arq.close()
        else:
            livros = []

        titulo = input("Nome: ")
        tem_letra_titulo = False
        for caractere in titulo:
            if caractere.isalpha():
                tem_letra_titulo = True

        while titulo == "" or tem_letra_titulo == False:
            print("Erro: O nome do livro precisa conter letras!")
            titulo = input("Nome: ")
            tem_letra_titulo = False
            for caractere in titulo:
                if caractere.isalpha():
                    tem_letra_titulo = True

        autor = input("Autor: ")
        tem_letra_autor = False
        for caractere in autor:
            if caractere.isalpha():
                tem_letra_autor = True
        
        while autor == "" or tem_letra_autor == False:
            print("Erro: O nome do autor precisa conter letras!")
            autor = input("Autor: ")
            tem_letra_autor = False
            for caractere in autor:
                if caractere.isalpha():
                    tem_letra_autor = True

        nota = input("Nota: ")
        while nota not in ["1", "2", "3", "4", "5"]:
            print("Erro: Digite um número de 1 a 5.")
            nota = input("Nota: ")

        # Nova lógica para evitar IDs duplicados
        if len(livros) == 0:
            id_livro = 1
        else:
            maior_id = 0
            for l in livros:
                if l["id"] > maior_id:
                    maior_id = l["id"]
            id_livro = maior_id + 1

        novo = {"id": id_livro, "titulo": titulo, "autor": autor, "nota": nota}
        livros.append(novo)

        arq = open(ARQUIVO, "wb")
        pickle.dump(livros, arq)
        arq.close()
        print("Salvo!")

    elif opcao == "2":
        if os.path.exists(ARQUIVO):
            arq = open(ARQUIVO, "rb")
            livros = pickle.load(arq)
            arq.close()
        else:
            livros = []

        if len(livros) == 0:
            print("Vazio.")
        else:
            for l in livros:
                print(
                    f"ID: {l['id']} | {l['titulo']} | {l['autor']} | Nota: {l['nota']}"
                )

    elif opcao == "3":
        if os.path.exists(ARQUIVO):
            arq = open(ARQUIVO, "rb")
            livros = pickle.load(arq)
            arq.close()
        else:
            livros = []

        if len(livros) == 0:
            print("Vazio. Nenhum livro cadastrado para editar.")
        else:
            print("\n--- Livros Disponíveis ---")
            for l in livros:
                print(f"ID: {l['id']} | {l['titulo']}")
            print("--------------------------")

            livro_encontrado = False
            while not livro_encontrado:
                entrada_id = input("ID para editar: ")
                while entrada_id == "" or not entrada_id.isdigit():
                    print("Erro: O ID precisa ser um número inteiro válido!")
                    entrada_id = input("ID para editar: ")
                
                id_busca = int(entrada_id)
                
                for l in livros:
                    if l["id"] == id_busca:
                        livro_encontrado = True
                        
                        novo_titulo = input("Novo Nome: ")
                        tem_letra_titulo = False
                        for caractere in novo_titulo:
                            if caractere.isalpha():
                                tem_letra_titulo = True

                        while novo_titulo == "" or tem_letra_titulo == False:
                            print("Erro: O nome do livro precisa conter letras!")
                            novo_titulo = input("Novo Nome: ")
                            tem_letra_titulo = False
                            for caractere in novo_titulo:
                                if caractere.isalpha():
                                    tem_letra_titulo = True
                        l["titulo"] = novo_titulo

                        novo_autor = input("Novo Autor: ")
                        tem_letra_autor = False
                        for caractere in novo_autor:
                            if caractere.isalpha():
                                tem_letra_autor = True
                        
                        while novo_autor == "" or tem_letra_autor == False:
                            print("Erro: O nome do autor precisa conter letras!")
                            novo_autor = input("Novo Autor: ")
                            tem_letra_autor = False
                            for caractere in novo_autor:
                                if caractere.isalpha():
                                    tem_letra_autor = True
                        l["autor"] = novo_autor

                        nova_nota = input("Nova Nota: ")
                        while nova_nota not in ["1", "2", "3", "4", "5"]:
                            print("Erro: Digite de 1 a 5.")
                            nova_nota = input("Nova Nota: ")
                        l["nota"] = nova_nota

                        arq = open(ARQUIVO, "wb")
                        pickle.dump(livros, arq)
                        arq.close()
                        print("Atualizado!")
                
                if not livro_encontrado:
                    print("Insira o ID correto.")

    elif opcao == "4":
        if os.path.exists(ARQUIVO):
            arq = open(ARQUIVO, "rb")
            livros = pickle.load(arq)
            arq.close()
        else:
            livros = []

        if len(livros) == 0:
            print("Vazio. Nenhum livro cadastrado para apagar.")
        else:
            print("\n--- Livros Disponíveis ---")
            for l in livros:
                print(f"ID: {l['id']} | {l['titulo']}")
            print("--------------------------")

            livro_encontrado = False
            while not livro_encontrado:
                entrada_id = input("ID para apagar: ")
                while entrada_id == "" or not entrada_id.isdigit():
                    print("Erro: O ID precisa ser um número inteiro válido!")
                    entrada_id = input("ID para apagar: ")
                    
                id_busca = int(entrada_id)
                
                for l in livros:
                    if l["id"] == id_busca:
                        livro_encontrado = True
                        
                        confirmacao = input(f"Você tem certeza que deseja apagar '{l['titulo']}'? (Digite sim para confirmar): ")
                        if confirmacao == "sim" or confirmacao == "SIM":
                            livros.remove(l)
                            arq = open(ARQUIVO, "wb")
                            pickle.dump(livros, arq)
                            arq.close()
                            print("Removido!")
                        else:
                            print("Operação cancelada.")
                        
                if not livro_encontrado:
                    print("Insira o ID correto.")

    elif opcao == "5":
        print('Saindo...')
        break

    else:
        print("Opção inválida! Escolha um número de 1 a 5.")
