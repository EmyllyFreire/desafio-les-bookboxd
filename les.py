import os
import pickle

ARQUIVO_DADOS = "bookboxd_oficial.dat"


def carregar_dados():
    if not os.path.exists(ARQUIVO_DADOS):
        return []
    with open(ARQUIVO_DADOS, "rb") as arquivo:
        try:
            return pickle.load(arquivo)
        except EOFError:
            return []


def salvar_dados(lista_livros):
    with open(ARQUIVO_DADOS, "wb") as arquivo:
        pickle.dump(lista_livros, arquivo)


# 1. CREATE
def adicionar_livro():
    print("\n--- ADICIONAR NOVO LIVRO ---")
    livros = carregar_dados()

    id_livro = len(livros) + 1

    titulo = input("Nome do Livro (Obrigatório): ").strip()
    while not titulo:
        print("O nome do livro não pode ficar em branco!")
        titulo = input("Nome do Livro (Obrigatório): ").strip()

    autor = input("Autor (ou Enter para pular): ").strip()
    if not autor:
        autor = "---"

    print("\nEscolha o Status do Livro:")
    print("1 - Lido")
    print("2 - Não Lido")
    print("3 - Próxima Leitura")
    opcao_status = input("Sua opção (1-3 ou Enter para 'Não Lido'): ").strip()

    status = "Não Lido"
    nota = "---"
    resenha = "---"

    if opcao_status == "1":
        status = "Lido"
        entrada_nota = (
            input("Sua Nota (Digite de 1 a 5 ou Enter para pular): ").strip()
        )
        if entrada_nota:
            try:
                nota_num = int(entrada_nota)
                if 1 <= nota_num <= 5:
                    nota = "⭐" * nota_num
                else:
                    print("Nota fora do limite (1 a 5). Salvo como '---'.")
            except ValueError:
                print("Entrada inválida. Salvo como '---'.")

        entrada_resenha = input(
            "Escreva sua Resenha (ou Enter para pular): "
        ).strip()
        if entrada_resenha:
            resenha = entrada_resenha

    elif opcao_status == "3":
        status = "Próxima Leitura"

    novo_livro = {
        "id": id_livro,
        "titulo": titulo,
        "autor": autor,
        "status": status,
        "nota": nota,
        "resenha": resenha,
    }

    livros.append(novo_livro)
    salvar_dados(livros)
    print(f"'{titulo}' foi adicionado e salvo com sucesso!")


# 2. READ
def listar_livros():
    print("\n--- DIÁRIO DE LEITURAS (BOOKBOXD) ---")
    livros = carregar_dados()

    if not livros:
        print("Sua lista está vazia. Que tal adicionar um livro?")
        return

    for livro in livros:
        print(f"ID: {livro['id']} | {livro['titulo']} (por {livro['autor']})")
        print(f"   Status: [{livro['status']}] | Avaliação: {livro['nota']}")
        print(f"   Resenha: {livro['resenha']}")
        print("-" * 50)


# 3. UPDATE
def atualizar_livro():
    print("\n--- EDITAR REGISTRO DO LIVRO ---")
    livros = carregar_dados()

    try:
        id_busca = int(input("Digite o ID do livro que deseja atualizar: "))
    except ValueError:
        print(" ID inválido.")
        return

    for livro in livros:
        if livro["id"] == id_busca:
            print(f"\nLivro encontrado: '{livro['titulo']}'")
            print(f"Status atual: {livro['status']}")

            print("\nEscolha o NOVO Status:")
            print("1 - Lido")
            print("2 - Não Lido")
            print("3 - Próxima Leitura")
            print("Aperte Enter direto para MANTER o status atual.")
            opcao_status = input("Sua opção: ").strip()

            if opcao_status == "1":
                livro["status"] = "Lido"
            elif opcao_status == "2":
                livro["status"] = "Não Lido"
                livro["nota"] = "---"
                livro["resenha"] = "---"
            elif opcao_status == "3":
                livro["status"] = "Próxima Leitura"
                livro["nota"] = "---"
                livro["resenha"] = "---"

            if livro["status"] == "Lido":
                nova_nota = input(
                    "Nova nota (1 a 5) ou Enter para manter/pular: "
                ).strip()
                if nova_nota:
                    try:
                        num = int(nova_nota)
                        if 1 <= num <= 5:
                            livro["nota"] = "⭐" * num
                        else:
                            livro["nota"] = "---"
                    except ValueError:
                        print("Entrada inválida. Mantendo valor.")

                nova_resenha = input(
                    "Nova resenha ou Enter para manter/pular: "
                ).strip()
                if nova_resenha:
                    livro["resenha"] = nova_resenha

            salvar_dados(livros)
            print("Registro de livro updated com sucesso!")
            return

    print("Livro não encontrado.")


# 4. DELETE
def remover_livro():
    print("\n--- REMOVER LIVRO ---")
    livros = carregar_dados()

    try:
        id_busca = int(input("Digite o ID do livro que deseja remover: "))
    except ValueError:
        print("ID inválido.")
        return

    for livro in livros:
        if livro["id"] == id_busca:
            livros.remove(livro)
            salvar_dados(livros)
            print(f"'{livro['titulo']}' foi removido da sua lista.")
            return

    print("Livro não encontrado.")


def menu():
    while True:
        print("\n==================================")
        print("    BOOKBOXD - DIÁRIO DE LIVROS   ")
        print("==================================")
        print("1. Criar (Adicionar Livro)")
        print("2. Read (Listar Livros)")
        print("3. Update (Editar Livro)")
        print("4. Delete (Remover Livro)")
        print("5. Sair")

        opcao = input("Escolha uma opção (1-5): ").strip()

        if opcao == "1":
            adicionar_livro()
        elif opcao == "2":
            listar_livros()
        elif opcao == "3":
            atualizar_livro()
        elif opcao == "4":
            remover_livro()
        elif opcao == "5":
            print("Saindo do Bookboxd... Até a próxima!")
            break
        else:
            print("Opção inválida! Escolha um número de 1 a 5.")


if __name__ == "__main__":
    menu()
