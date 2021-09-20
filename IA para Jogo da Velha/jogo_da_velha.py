class Jogo():
    #inicializa uma matriz
    def __init__(self):
        self.matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    #realiza uma jogada 
    def jogada(self, posicao, jogador):
        for i in range(2, 0, -1):
            if jogador == "X":
                for j in range(2):
                    if posicao == self.matriz[i][j]:
                        self.matriz[i][j] = 10
            if jogador == "O":
                for j in range(2):
                    if posicao == self.matriz[i][j]:
                        self.matriz[i][j] = -10
    #mostra como o jogo esta no momento
    def mostra_jogo(self):
        matriz2 = self.matriz
        for i in range(2):
            for j in range(2):
                if matriz2[i][j] == 10:
                    matriz2[i][j] == "X"
                elif matriz2[i][j] == -10:
                    matriz2[i][j] == "O"
        return matriz2
    #diz se em uma determinada rodada do jogo houve algum vencedor
    def venceu(self):
        #verificação na horizontal
        for i in range(2):
            soma = 0
            for j in range(2):
                soma = self.matriz[i][j]
                if soma == 30:
                    return print("Jogador X venceu!")
                if soma == -30:
                    return print("Jogador O venceu!")
        #verificação na vertical
        for i in range(2):
            soma = 0
            for j in range(2):
                soma = self.matriz[j][i]
                if soma == 30:
                    return print("Jogador X venceu!")
                if soma == -30:
                    return print("Jogador O venceu!")
        #verificação na diagonal
        primeira_diagonal = self.matriz[0][0] + self.matriz[1][1] + self.matriz[2][0]
        segunda_diagonal = self.matriz[0][2] + self.matriz[1][1] + self.matriz[2][0]
        if primeira_diagonal == 30 or segunda_diagonal == 30:
            return print("Jogador X venceu!")
        elif primeira_diagonal == -30 or segunda_diagonal == -30:
            return print("Jogador O venceu!")
        #verificação de empate
        for i in range(2):
            for j in range(2):
                if self.matriz[i][j] == 0:
        