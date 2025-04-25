def interface():
    print("   0   1   2")
    for i in range(3):
        print(f"{i} [{tabuleiro[i][0]}] [{tabuleiro[i][1]}] [{tabuleiro[i][2]}]")

tabuleiro = [[" ", " ", " "] for _ in range(3)]

def validarvitoria(rodada):
    vitorias = [
        # Linhas
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        # Colunas
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        # Diagonais
        [(0, 0), (1, 1), (2, 2)],
        [(2, 0), (1, 1), (0, 2)],
    ]
    for linha in vitorias:
        if all(tabuleiro[l][c] == rodada for l, c in linha):
            interface()
            print(f"O jogador {rodada} venceu!")
            return True
    return False

rodada = "X"
jogadas = 0

while True:
    interface()

    try:
        linha = int(input("Digite a linha escolhida (0 a 2): "))
        coluna = int(input("Digite a coluna escolhida (0 a 2): "))
    except ValueError:
        print("Digite apenas números inteiros válidos.")
        continue

    if linha not in [0, 1, 2] or coluna not in [0, 1, 2]:
        print("Linha ou coluna inválida. Tente novamente.")
        continue

    if tabuleiro[linha][coluna] != " ":
        print("Essa posição já está ocupada. Escolha outra.")
        continue

    tabuleiro[linha][coluna] = rodada
    jogadas += 1

    if validarvitoria(rodada):
        break

    if jogadas == 9:
        interface()
        print("Deu velha!")
        break

    rodada = "O" if rodada == "X" else "X"

print("Fim de jogo!")
