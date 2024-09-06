import random
import json
import time

def verificar_cartelas_batidas(cartelas, numeros_sorteados):
    """Verifica se alguma cartela foi batida com os números sorteados."""
    cartelas_batidas = []
    
    for numero_cartela, cartela in cartelas.items():
        for linha in cartela:
            # Verifica se todos os números da linha estão presentes nos números sorteados
            linha_batida = True
            for num in linha:
                if num not in numeros_sorteados:
                    linha_batida = False
                    break
            if linha_batida:
                cartelas_batidas.append((numero_cartela, cartela))
                break  # Uma vez que uma cartela é batida, não precisa checar as outras linhas
    
    return cartelas_batidas


def sorteio_bingo(cartelas):
    """Função para realizar o sorteio do bingo conforme os requisitos."""
    numeros_disponiveis = list(range(1, 76))
    numeros_sorteados = random.sample(numeros_disponiveis, 25)  # Sorteia 25 números únicos
    
    print("Números sorteados inicialmente:")
    print(sorted(numeros_sorteados))
    
    while True:
        # Verifica se houve cartelas batidas
        cartelas_batidas = verificar_cartelas_batidas(cartelas, numeros_sorteados)
        
        if cartelas_batidas:
            print("\nCartelas batidas:")
            for numero, cartela in cartelas_batidas:
                print(f"Cartela {numero}: {cartela}")
            print(f"Números sorteados: {sorted(numeros_sorteados)}")
            break
        
        # Se não houver cartelas batidas, sorteia uma nova dezena
        if len(numeros_sorteados) < 75:
            # Cria uma lista de números que ainda não foram sorteados
            numeros_faltantes = []
            for num in numeros_disponiveis:
                if num not in numeros_sorteados:
                    numeros_faltantes.append(num)
            
            # Sorteia um número dos números faltantes, se houver
            if numeros_faltantes:
                numero_sorteado = random.choice(numeros_faltantes)
                numeros_sorteados.append(numero_sorteado)
                print(f"Número sorteado: {numero_sorteado}")
                time.sleep(2)  # Espera 2 segundos antes de sortear o próximo número
            else:
                print("Não há mais números disponíveis para sortear.")
                break
        else:
            print("Número máximo de sorteios atingido.")
            break


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
    if numero_cartela not in cartelas:
        print(f"A cartela {numero_cartela} não existe!")
        return

    # Pega a cartela a partir do número fornecido
    cartela = cartelas[numero_cartela]

    # Cabeçalhos das colunas (B, I, N, G, O)
    headers = "  B    I    N    G    O "

    # Imprimindo a cartela no formato solicitado
    print("-" * 26)
    print(f"Cartela: {numero_cartela}")
    print("-" * 26)
    print(headers)
    print("-" * 26)

    # Imprime cada linha das colunas da cartela
    for i in range(5):  # Existem 5 linhas
        linha = f"| {cartela[0][i]:2} | {cartela[1][i]:2} | {cartela[2][i]:2} | {cartela[3][i]:2} | {cartela[4][i]:2} |"
        print(linha)
    
    print("-" * 25)

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
            cartelas_geradas = ler_cartelas()
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
            if cartelas_geradas:
                sorteio_bingo(cartelas_geradas)
            else:
                print("Nenhuma cartela carregada. Gere ou leia as cartelas primeiro.")
        elif pergunta == "6":
            print("Saindo do programa. Até mais!")
            break
        else:
            print("Opção inválida. Por favor, escolha um número de 1 a 6.")

# Executar o menu principal
menu_bingo()
