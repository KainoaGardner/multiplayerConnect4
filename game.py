import numpy
import pygame
from settings import *

class Game:
    def __init__(self):
        self.turn = 0
        self.ready = False
        self.mousePos = 0
        self.winningTiles = []
        self.winningTurn = None

        self.board = numpy.zeros((6,7),dtype=numpy.int8)

    def validMove(self,column):
        if self.board[0,column] == 0:
            return True
        return False
    def makeMove(self,column,turn):
        if self.validMove(column):
            row = 0
            for i in range(1,len(self.board)):
                if self.board[i,column] == 0:
                    row = i
                else:
                    break

            self.board[row,column] = turn + 1


            if self.turn == 0:
                self.turn = 1
            elif self.turn == 1:
                self.turn = 0

    def checkWin(self):
        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                if self.board[r,c] != 0:
                    if r < 3:
                        if c <= len(self.board[r]) - 4:
                            if self.board[r][c] == self.board[r][c + 1] == self.board[r][c + 2] == self.board[r][c + 3]:
                                self.winningTiles.append((r, c))
                                self.winningTiles.append((r, c + 1))
                                self.winningTiles.append((r, c + 2))
                                self.winningTiles.append((r, c + 3))

                        if r <= len(self.board) - 4:
                            if self.board[r][c] == self.board[r + 1][c] == self.board[r + 2][c] == self.board[r + 3][c]:
                                self.winningTiles.append((r, c))
                                self.winningTiles.append((r + 1, c))
                                self.winningTiles.append((r + 2, c))
                                self.winningTiles.append((r + 3, c))

                        if c <= len(self.board[r]) - 4 and r <= len(self.board) - 4:
                            if self.board[r][c] == self.board[r + 1][c + 1] == self.board[r + 2][c + 2] == \
                                    self.board[r + 3][c + 3]:
                                self.winningTiles.append((r, c))
                                self.winningTiles.append((r + 1, c + 1))
                                self.winningTiles.append((r + 2, c + 2))
                                self.winningTiles.append((r + 3, c + 3))

                        if c >= 3 and r <= len(self.board) - 4:
                            if self.board[r][c] == self.board[r + 1][c - 1] == self.board[r + 2][c - 2] == \
                                    self.board[r + 3][c - 3]:
                                self.winningTiles.append((r, c))
                                self.winningTiles.append((r + 1, c - 1))
                                self.winningTiles.append((r + 2, c - 2))
                                self.winningTiles.append((r + 3, c - 3))

        return len(self.winningTiles) > 0

    def reset(self):
        self.board = numpy.zeros((6, 7), dtype=numpy.int8)
        self.turn = 0
        self.winningTiles = []
        self.winningTurn = None


    def highlightWin(self,screen):
        if len(self.winningTiles) > 0:
            for tile in self.winningTiles:
                pygame.draw.circle(screen,"#ecf0f1",(tile[1] * TILESIZE + TILESIZE // 2,tile[0] * TILESIZE + TILESIZE // 2 + TILESIZE),TILESIZE //2  - 5,5)

    def displayBoard(self,screen):
        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                if self.board[r,c] == 0:
                    pygame.draw.circle(screen,"#2d3436",(c * TILESIZE + TILESIZE // 2,(r + 1) * TILESIZE + TILESIZE // 2),TILESIZE // 2.1)
                elif self.board[r,c] == 1:
                    pygame.draw.circle(screen,red,(c * TILESIZE + TILESIZE // 2,(r + 1) * TILESIZE + TILESIZE // 2),TILESIZE // 2.1)
                elif self.board[r,c] == 2:
                    pygame.draw.circle(screen,yellow,(c * TILESIZE + TILESIZE // 2,(r + 1) * TILESIZE + TILESIZE // 2),TILESIZE // 2.1)

    def displayBar(self,screen):
        pygame.draw.rect(screen,"#7f8c8d",(0,0,WIDTH,TILESIZE))
        if self.turn == 0:
            pygame.draw.circle(screen,red,(self.mousePos,TILESIZE // 2),TILESIZE//2)
        else:
            pygame.draw.circle(screen, yellow, (self.mousePos, TILESIZE // 2), TILESIZE // 2)

    def display(self,screen):
        self.displayBar(screen)
        self.displayBoard(screen)
        self.highlightWin(screen)



