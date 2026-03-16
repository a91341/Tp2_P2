"""Implementação do jogo Gomoku (5 em linha)"""

from jogo_abs import Jogo
import random


class Gomoku(Jogo):
    """ Classe concreta que herda da classe Jogo e implementa o jogo Gomoku."""

    def inicializa_tabuleiro(self) -> None:
        """ Inicializa o tabuleiro 10x10 com espaços vazios ' '. """
        self.tabuleiro = [[' ' for _ in range(10)] for _ in range(10)]

    def mostra_tabuleiro(self) -> None:
        """ Exibe o tabuleiro na consola. """
        print("\n " + " ".join(str(i) for i in range (10)))

        for i, linha in enumerate(self.tabuleiro):
            print(f"{i:2}" + " |".join(linha))
            if i < 9:
                print("  " + "-" * 19)

    def joga_humano(self, jogador: int) -> None:
        """ Jogada do jogador humano. """

        simbolo = "O" if jogador == 0 else "X"

        while True:
            try:
                linha = int(input("Linha (0-9): "))
                coluna = int(input("Coluna (0-9): "))
                if linha < 0 or linha > 9 or coluna < 0 or coluna > 9:
                    print("Posição fora do tabuleiro. Tente novamente.")
                    continue

                if self.tabuleiro[linha][coluna] != ' ':
                    print("Posição já ocupada. Tente novamente.")
                    continue

                self.tabuleiro[linha][coluna] = simbolo
                break
            except ValueError:
                print("Entrada inválida. Digite números entre 0 e 9. Tente novamente.") 


    def joga_computador(self, jogador: int) -> None:
        """ Jogada do computador. 
        O computador tenta jogar de forma inteligente, seguindo uma estratégia simples."""
        
        simbolo = "O" if jogador == 0 else "X"
        adversario = "X" if simbolo == "O" else "O"
        
        livres = []

        for i in range(10):
            for j in range(10):
                if self.tabuleiro[i][j] == ' ':
                    livres.append((i, j))


        # Primeiro, verifica se há uma jogada vencedora para o computador
        for i, j in livres:
            if self.jogada_win(i, j, simbolo):
                self.tabuleiro[i][j] = simbolo
                return
            
        # Segundo, verifica se o oponente tem uma jogada vencedora e bloqueia
        for i, j in livres:
            if self.jogada_win(i, j, "O" if simbolo == "X" else "X"):
                self.tabuleiro[i][j] = simbolo
                return
        
        # Terceiro, tenta jogar próximo a uma peça já colocada.
        possivel = [(i,j) for i, j in livres if self.tem_vizinho(i, j)]
                    
        if possivel:
            i, j = random.choice(possivel)
            self.tabuleiro[i][j] = simbolo
            return
        
        # Quarto, joga aleatoriamente.
        i, j = random.choice(livres)
        self.tabuleiro[i][j] = simbolo

    def ha_jogadas_possiveis(self) -> bool:
        """ Verifica se ainda há espaços vazios no tabuleiro."""
        
        for linha in self.tabuleiro:
            if ' ' in linha:
                return True
        return False
    
    def contar_linhas(self, linha, coluna, dx, dy, simnolo):

        contador = 0

        for k in range(5):
            x = linha + dx * k
            y = coluna + dy * k

            if 0 <= x < 10 and 0 <= y < 10:
                if self.tabuleiro[x][y] == simnolo:
                    contador += 1
                else:
                    break
            else:
                break

        return contador
    
    def tem_vizinho(self, linha, coluna):

        for dx in range(-1, 0, 1):
            for dy in range(-1, 0, 1):
                if dx == 0 and dy == 0:
                    continue

                x = linha + dx
                y = coluna + dy

                if 0 <= x < 10 and 0 <= y < 10:
                    if self.tabuleiro[x][y] != ' ':
                        return True

        return False
    
    def jogada_win(self, linha, coluna, simbolo):

        self.tabuleiro[linha][coluna] = simbolo

        ganhou = self.terminou()

        self.tabuleiro[linha][coluna] = ' '

        return ganhou

    def terminou(self) -> bool:
        """ Verifica se existe 5 em linha """
        
        tamanho = 10 
        direcoes = [
            (0, 1),   # horizontal
            (1, 0),   # vertical
            (1, 1),   # diagonal descendo
            (1, -1)   # diagonal subindo
        ]

        for i in range(tamanho):
            for j in range(tamanho):

                simbolo = self.tabuleiro[i][j]
                
                if simbolo == ' ':
                    continue

                for dx, dy in direcoes:

                    contador = 0

                    for k in range(5):
                        x = i + dx * k
                        y = j + dy * k

                        if 0 <= x < tamanho and 0 <= y < tamanho:
                            if self.tabuleiro[x][y] == simbolo:
                                contador += 1
                            else:
                                break
                        else:
                            break

                    if contador == 5:
                        return True 
                    
        return False
