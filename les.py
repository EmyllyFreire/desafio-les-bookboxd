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
    print("\n--- ADICIONAR LIVRO ---")
    livros = carregar_dados()

    titulo = input("Nome do Livro: ")
    autor = input("Autor: ")
    status = input("Status (Lido, Não Lido ou Próxima Leitura): ")
    nota = input("Nota (1 a 5 ou Enter para pular): ")
    resenha = input("Resenha (ou Enter para pular): ")

    if titulo == "":
        titulo = "---"
    if autor == "":
        autor = "---"
    if status == "":
        status = "---"
    if nota == "":
        nota = "---"
    if resenha == "":
        resenha = "---"

    id_livro = len(livros) + 1
    novo = {
        "id": id_livro,
        "titulo": titulo,
        "autor": autor,
        "status": status,
        "nota": nota,
        "resenha": resenha,
    }

    livros.append(novo)
    salvar_dados(livros)
    print("Livro salvo com sucesso!")


def listar_livros():
    print("\n--- LISTA DE LIVROS ---")
    livros = carregar_dados()

    if len(livros) == 0:
        print("Nenhum livro cadastrado.")
        return

    for l in livros:
        print(f"ID: {l['id']} | Livro: {l['titulo']} | Autor: {l['autor']}")
        print(f"Status: {l['status']} | Nota: {l['nota']} | Resenha: {l['resenha']}")
        print("-" * 30)


def atualizar_livro():
    print("\n--- EDITAR LIVRO ---")
    livros = carregar_dados()

    id_busca = int(input("Digite o ID do livro que quer editar: "))

    for l in livros:
        if l["id"] == id_busca:
            print(f"Editando o livro: {l['titulo']}")
            l["titulo"] = input("Novo Nome: ")
            l["autor"] = input("Novo Autor: ")
            l["status"] = input("Novo Status: ")
            l["nota"] = input("Nova Nota: ")
            l["resenha"] = input("Nova Resenha: ")

            salvar_dados(livros)
            print("Livro updated!")
            return

    print("Livro não encontrado.")


def remover_livro():
    print("\n--- REMOVER LIVRO ---")
    livros = carregar_dados()

    id_busca = int(input("Digite o ID do livro que quer apagar: "))

    for l in livros:
        if l["id"] == id_busca:
            livros.remove(l)
            salvar_dados(livros)
            print("Livro removido!")
            return

    print("Livro não encontrado.")


def menu():
    while True:
        print("\n=== MENU BOOKBOXD ===")
        print("1. Adicionar")
        print("2. Listar")
        print("3. Editar")
        print("4. Remover")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_livro()
        elif opcao == "2":
            listar_livros()
        elif opcao == "3":
            atualizar_livro()
        elif opcao == "4":
            remover_livro()
        elif opcao == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")


if __name__ == "__main__":
    menu()
