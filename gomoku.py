"""Implementação do jogo Gomoku (5 em linha)"""

from jogo_abs import Jogo
import random


class Gomoku(Jogo):
    """
    Classe concreta que herda da classe Jogo e implementa o jogo Gomoku.
    """

    def inicializa_tabuleiro(self) -> None:
        """
        Inicializa o tabuleiro 10x10 com espaços vazios ' '.
        """
        self.tabuleiro = [[' ' for _ in range(10)] for _ in range(10)]

    def mostra_tabuleiro(self) -> None:
        """ Exibe o tabuleiro na consola. """
        print("\n " + " ".join(str(i) for i in range (10)))

        for i, linha in enumerate(self.tabuleiro):
            print(f"{i:2}" + " |".join(linha))
            if i < 9:
                print("  " + "-" * 19)

    def joga_humano(self, jogador: int) -> None:
        """ Jogada do jogador himano """

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
        """
        Realiza uma jogada aleatória do computador numa posição livre.
        - Jogador 0 usa 'O', Jogador 1 usa 'X'.
        :param jogador: número do jogador (computador).
        """
        raise NotImplementedError("Implementar este método")

    def ha_jogadas_possiveis(self) -> bool:
        """
        Verifica se ainda há espaços vazios no tabuleiro.
        :return: True se ainda há jogadas possíveis, False caso contrário.
        """
        raise NotImplementedError("Implementar este método")

    def terminou(self) -> bool:
        """
        Verifica se alguém ganhou (5 peças seguidas em qualquer direção:
        horizontal, vertical, diagonal ↘️, diagonal ↗️).
        :return: True se o jogo terminou (alguém ganhou), False caso contrário.
        """
        raise NotImplementedError("Implementar este método")
