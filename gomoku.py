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
        """ Jogada aleatória do computador """
        
        simbolo = "O" if jogador == 0 else "X"
        
        livres = []

        for i in range(10):
            for j in range(10):
                if self.tabuleiro[i][j] == ' ':
                    livres.append((i, j))

        linha, coluna = random.choice(livres)

        self.tabuleiro[linha][coluna] = simbolo

    def ha_jogadas_possiveis(self) -> bool:
        """ Verifica se ainda há espaços vazios no tabuleiro."""
        
        for linha in self.tabuleiro:
            if ' ' in linha:
                return True
        return False

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
