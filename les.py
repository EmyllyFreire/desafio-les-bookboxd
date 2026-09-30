import os
import pickle

ARQUIVO = "dados.dat"

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
        autor = input("Autor: ")
        nota = input("Nota: ")

        if titulo == "":
            titulo = "---"
        if autor == "":
            autor = "---"
        if nota == "":
            nota = "---"

        id_livro = len(livros) + 1
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

        id_busca = int(input("ID para editar: "))
        for l in livros:
            if l["id"] == id_busca:
                l["titulo"] = input("Novo Nome: ")
                l["autor"] = input("Novo Autor: ")
                l["nota"] = input("Nova Nota: ")

                arq = open(ARQUIVO, "wb")
                pickle.dump(livros, arq)
                arq.close()
                print("Atualizado!")

    elif opcao == "4":
        if os.path.exists(ARQUIVO):
            arq = open(ARQUIVO, "rb")
            livros = pickle.load(arq)
            arq.close()
        else:
            livros = []

        id_busca = int(input("ID para apagar: "))
        for l in livros:
            if l["id"] == id_busca:
                livros.remove(l)

                arq = open(ARQUIVO, "wb")
                pickle.dump(livros, arq)
                arq.close()
                print("Removido!")

    elif opcao == "5":
        print('Saindo...')
        break
