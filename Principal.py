"""Ideias Para Criação
1. Configuração do tabuleiro
2. Renderização do tabuleiro
3. Entrada do jogador
4. Verificação de vitória
5. Lógica principal do jogo
6. Fim do jogo
7. Interface gráfica (opcional)
"""

def verificar_vitoria(tabuleiro, jogador):
    # Verificação nas linhas
    for linha in tabuleiro:
        if linha.count(jogador) == 3:
            return jogador

    # Verificação nas colunas
    for coluna in range(3):
        if tabuleiro[0][coluna] == tabuleiro[1][coluna] == tabuleiro[2][coluna] == jogador:
            return jogador

    # Verificação nas diagonais
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == jogador:
        return jogador
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == jogador:
        return jogador

    return None

def jogo_da_velha():
    tabuleiro = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]
    jogador_atual = 'X'
    vencedor = None
    empate = False

    while vencedor is None and not empate:
        exibir_tabuleiro(tabuleiro)
        print("Vez do jogador", jogador_atual)
        linha, coluna = obter_jogada()

        if tabuleiro[linha][coluna] == ' ':
            fazer_jogada(tabuleiro, linha, coluna, jogador_atual)

            # Verificar vitória
            vencedor = verificar_vitoria(tabuleiro, jogador_atual)

            # Alternar jogador
            jogador_atual = 'O' if jogador_atual == 'X' else 'X'

            # Verificar empate
            if not any(' ' in linha for linha in tabuleiro):
                empate = True
        else:
            print("Posição inválida. Tente novamente.")

    exibir_tabuleiro(tabuleiro)

    if vencedor:
        print("O jogador", vencedor, "venceu!")
    else:
        print("Empate!")

def exibir_tabuleiro(tabuleiro):
    print("  1   2   3")  # Números das colunas
    print(" -------------")
    for i in range(3):
        print(f"{i+1}| {tabuleiro[i][0]} | {tabuleiro[i][1]} | {tabuleiro[i][2]} |")
        print(" -------------")

def fazer_jogada(tabuleiro, linha, coluna, jogador):
    tabuleiro[linha][coluna] = jogador

def obter_jogada():
    linha = int(input("Digite o número da linha (1 a 3): ")) - 1
    coluna = int(input("Digite o número da coluna (1 a 3): ")) - 1
    return linha, coluna

jogo_da_velha()
