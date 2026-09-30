import os
import pickle

ARQUIVO = "bookboxd_dados.dat"


def carregar_dados():
    if not os.path.exists(ARQUIVO):
        return []
    arquivo = open(ARQUIVO, "rb")
    dados = pickle.load(arquivo)
    arquivo.close()
    return dados


def salvar_dados(lista):
    arquivo = open(ARQUIVO, "wb")
    pickle.dump(lista, arquivo)
    arquivo.close()


def adicionar_livro():
    livros = carregar_dados()
    titulo = input("Nome do Livro: ")
    autor = input("Autor: ")
    nota = input("Nota (1 a 5): ")

    if titulo == "":
        titulo = "---"
    if autor == "":
        autor = "---"
    if nota == "":
        nota = "---"

    id_livro = len(livros) + 1
    novo = {"id": id_livro, "titulo": titulo, "autor": autor, "nota": nota}
    livros.append(novo)
    salvar_dados(livros)
    print("Salvo!")


def listar_livros():
    livros = carregar_dados()
    if len(livros) == 0:
        print("Vazio.")
        return
    for l in livros:
        print(
            f"ID: {l['id']} | Livro: {l['titulo']} | Autor: {l['autor']} | Nota: {l['nota']}"
        )


def atualizar_livro():
    livros = carregar_dados()
    id_busca = int(input("ID para editar: "))
    for l in livros:
        if l["id"] == id_busca:
            l["titulo"] = input("Novo Nome: ")
            l["autor"] = input("Novo Autor: ")
            l["nota"] = input("Nova Nota: ")
            salvar_dados(livros)
            print("Atualizado!")
            return
    print("Não encontrado.")


def remover_livro():
    livros = carregar_dados()
    id_busca = int(input("ID para apagar: "))
    for l in livros:
        if l["id"] == id_busca:
            livros.remove(l)
            salvar_dados(livros)
            print("Removido!")
            return
    print("Não encontrado.")


def menu():
    while True:
        print('=== BOOKBOXD ===')
        print("1-Adicionar livro\n2-Listar livros\n3-Editar livro\n4-Remover livro\n5-Sair")
        opcao = input("Opção: ")
        if opcao == "1":
            adicionar_livro()
        elif opcao == "2":
            listar_livros()
        elif opcao == "3":
            atualizar_livro()
        elif opcao == "4":
            remover_livro()
        elif opcao == "5":
            break


if __name__ == "__main__":
    menu()
