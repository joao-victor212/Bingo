import random
import json

def gerar_cartelas():
    num = int(input("Digite quantas cartelas você deseja criar: "))
    while num <= 0 or num > 10000:
        print("O número de cartelas deve ser entre 1 e 10.000. Tente novamente!")
        num = int(input("Digite novamente quantas cartelas você deseja criar:"))

    cartelas = {}
    while len(cartelas) < num:
        coluna_b = []
        coluna_i = []
        coluna_n = []
        coluna_g = []
        coluna_o = []

        for _ in range(5):
            coluna_b.append(random.randint(1, 15))
            coluna_i.append(random.randint(16, 30))
            coluna_n.append(random.randint(31, 45))
            coluna_g.append(random.randint(46, 60))
            coluna_o.append(random.randint(61, 75))

        cartela = [sorted(coluna_b), sorted(coluna_i), sorted(coluna_n), sorted(coluna_g), sorted(coluna_o)]

        numero_correspondente = random.randint(1, 100000)
        if numero_correspondente not in cartelas:
            cartelas[numero_correspondente] = cartela

    return cartelas

def salvar_cartelas(cartelas):
    with open("cartelas.txt", "w") as arquivo:
        for numero, cartela in cartelas.items():
            # Escreve o número da cartela e os números no formato solicitado
            arquivo.write(f"{numero}: {cartela}\n")
    print("Cartelas salvas em 'cartelas.txt'.")

def imprimir_cartela(cartelas, numero_cartela):
    # Verifica se a cartela existe no dicionário
    if numero_cartela in cartelas:
        # Imprime a cartela no formato simples
        print(f"{numero_cartela}: {cartelas[numero_cartela]}")
    else:
        print(f"Cartela número {numero_cartela} não encontrada.")


def ler_cartelas():
    try:
        with open("cartelas.txt", "r") as arquivo:
            linhas = arquivo.readlines()
            cartelas = {}

            for linha in linhas:
                # Separando o número da cartela dos números
                numero_cartela, cartela_str = linha.split(": ")
                
                # Usando json.loads() para converter a string de volta para lista
                cartela = json.loads(cartela_str.strip())

                # Armazenando no dicionário com o número da cartela como chave
                cartelas[int(numero_cartela)] = cartela

        print("Cartelas lidas e organizadas com sucesso.")
        return cartelas

    except FileNotFoundError:
        print("Arquivo 'cartelas.txt' não encontrado.")
        return None


def menu_bingo():
    cartelas_geradas = None
    print("--- Seja Bem-Vindo ao Bingo ---")
    print("-="*16)
    print()
    print("Esse é o seu menu de opções:")
    print("1) Gerar Cartelas")
    print("2) Salvar Cartelas")
    print("3) Ler Cartelas")
    print("4) Imprimir Cartela")
    print("5) Sorteio do Bingo")
    print("6) Sair.")
    print()

    while True:
        pergunta = input("Digite um número correspondente à uma ação: ").strip()
        if pergunta == "1":
            cartelas_geradas = gerar_cartelas()
            print("Cartelas geradas com sucesso.")
        elif pergunta == "2":
            if cartelas_geradas:
                salvar_cartelas(cartelas_geradas)
            else:
                print("Nenhuma cartela gerada para salvar.")
        elif pergunta == "3":
            ler_cartelas()
            print("Cartelas organizadas")
        elif pergunta == "4":
            if cartelas_geradas:  # Verifica se as cartelas já foram carregadas
                try:
                    numero = int(input("Digite o número da cartela que deseja imprimir: "))
                    imprimir_cartela(cartelas_geradas, numero)  # Passa o dicionário e o número da cartela
                except ValueError:
                    print("Por favor, insira um valor válido.")
            else:
                print("Nenhuma cartela carregada. Gere ou leia as cartelas primeiro.")

        elif pergunta == "5":
            print("Função de sorteio do bingo ainda não implementada.")
        elif pergunta == "6":
            print("Saindo do programa. Até mais!")
            break
        else:
            print("Opção inválida. Por favor, escolha um número de 1 a 6.")

# Executar o menu principal
menu_bingo()


