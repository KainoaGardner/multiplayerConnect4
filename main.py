
from network import Network
from settings import *
import pygame


screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()
pygame.font.init()

font = pygame.font.Font("font/LEMONMILK-Regular.otf",50)
font1 = pygame.font.Font("font/LEMONMILK-Regular.otf",50)
textRed = font.render("Red Wins",True,red)
textYellow = font.render("Yellow Wins", True, yellow)
textRestart = font1.render("Press R to Restart",True,"white")
textWaitingForPlayer = font.render("Waiting for Player",True,"white")

def main():
    n = Network()
    player = int(n.getN())
    game = n.send("GetGame")

    run = True
    while run:
        try:
            game = n.send("get")
        except:
            run = False
            print("Couldn't get game")
            break

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player == game.turn and len(game.winningTiles) <= 0 and game.ready:
                    mos = pygame.mouse.get_pos()
                    column = mos[0] // TILESIZE
                    game.makeMove(column,player)
                    if game.checkWin():
                        game.winningTurn = player
                    game = n.send("M" + str(column))
            if event.type == pygame.KEYDOWN:
                if game.ready:
                    if event.key == pygame.K_r:
                        game.reset()
                        game = n.send("R")



        if player == game.turn and len(game.winningTiles) <= 0 and game.ready:
            mos = pygame.mouse.get_pos()
            if 0 + TILESIZE // 2 <= mos[0] <= WIDTH - TILESIZE // 2:
                game.mousePos = mos[0]
                game = n.send("P" + str(mos[0]))


        screen.fill("#2980b9")
        if game.ready:
            game.display(screen)
            if game.winningTurn == 0:
                screen.blit(textRed,(WIDTH//2 - textRed.get_width() // 2, HEIGHT // 2))
                screen.blit(textRestart, (WIDTH // 2 - textRestart.get_width() // 2, HEIGHT // 2 + 100))
            elif game.winningTurn == 1:
                screen.blit(textYellow,(WIDTH//2 - textRed.get_width() // 2, HEIGHT // 2))
                screen.blit(textRestart,(WIDTH//2 - textRestart.get_width() // 2, HEIGHT // 2 + 100))
        else:
            screen.blit(textWaitingForPlayer,(WIDTH//2 - textWaitingForPlayer.get_width() // 2, HEIGHT // 2))

        pygame.display.update()
        clock.tick(FPS)




main()