import random

# Lista para armazenar as pontuações
pontuacoes = []

print("Bem-vindo ao Jogo de Adivinhação!")

while True:
    numero_secreto = random.randint(1, 100)
    tentativas_totais = 0  # Inicializa a variável corretamente
    tentativas = 0  # Conta as tentativas feitas pelo jogador

    print("Eu pensei em um número entre 1 e 100.")
    print("Escolha o nível de dificuldade:")
    print("1. Fácil (10 tentativas)")
    print("2. Médio (7 tentativas)")
    print("3. Difícil (5 tentativas)")

    # Escolha do nível de dificuldade
    while True:
        dificuldade = input("Digite o número da dificuldade desejada: ")
        if dificuldade == "1":
            tentativas_totais = 10
            break
        elif dificuldade == "2":
            tentativas_totais = 7
            break
        elif dificuldade == "3":
            tentativas_totais = 5
            break
        else:
            print("Opção inválida. Por favor, escolha 1, 2 ou 3.")

    tentativas_restantes = tentativas_totais  # Define tentativas restantes com base na dificuldade escolhida

    # Loop de Tentativas
    while tentativas_restantes > 0:
        try:
            palpite = int(input("Digite seu palpite: "))
        except ValueError:
            print("Por favor, insira um número válido.")
            continue  # Pede novamente o palpite caso não seja um número

        tentativas += 1
        tentativas_restantes -= 1

        if palpite == numero_secreto:
            print(f"Parabéns! Você acertou o número em {tentativas} tentativa(s).")
            pontuacao = tentativas_restantes * 10
            pontuacoes.append(pontuacao)
            print(f"Sua pontuação nesta partida: {pontuacao} pontos.")
            break
        elif palpite < numero_secreto:
            print("O número é maior que esse.")
        else:
            print("O número é menor que esse.")

        print(f"Tentativas restantes: {tentativas_restantes}")
    else:
        print(f"\nQue pena! Você não conseguiu adivinhar. O número era {numero_secreto}.")
        pontuacoes.append(0)

    # Exibindo o Placar
    print("Placar:")
    for idx, pontos in enumerate(pontuacoes, start=1):
        print(f"Partida {idx}: {pontos} pontos")

    # Perguntar se o jogador quer jogar novamente
    jogar_novamente = input("Deseja jogar novamente? (s/n): ").lower()
    if jogar_novamente != 's':
        print("Obrigado por jogar! Até a próxima.")
        break