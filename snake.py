#LIBRERIAS IMPORTADAS
import pygame, sys, time
from pygame.locals import *
from random import randint

#COLOR Y GROSOR DE SERPIENTE 
def snakeDibujo(snake, window):
    for i in range(len(snake)):
        pygame.draw.rect(window,(255,0,0,0),(snake[i][1]*20,snake[i][0]*20,20,20),10)

#MOVIMIENTO DE LA SERPIENTE
def avanzar(snake, newpos):
    for i in reversed(range(1,len(snake))):
        snake[i] = snake[i-1]
    snake[0] = newpos
    return snake

def startWindow():
    puntuacion=0
    window = pygame.display.set_mode((600,500)) #resolucion 600(ancho)x500(alto)
    pygame.display.set_caption("SNAKE JUAN PABLO GALLEGOS") #nombre de la ventana
    snake = [[5,7],[5,6],[5,5]]
    right,left,up,down,rand1,rand2 = True, False, False, False, 10, 10
    R, G, B = 0, 0, 255

    while True:
        window.fill((0,0,0))
        snakeDibujo(snake, window)
        pygame.draw.rect(window, (R, G, B, 0), (rand1*20, rand2*20, 20, 20), 10)
        pygame.font.init()
        fuente = pygame.font.Font(None, 25)
        texto = fuente.render('Score', 1, (255, 0, 255))
        texto2 = fuente.render(str(puntuacion), 1, (255, 0, 255))
        window.blit(texto, (0,0))
        window.blit(texto2, (65,0))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_DOWN and up == False: down, up, right, left = True, False, False, False
                if event.key == K_UP and down == False: up, down, right, left = True, False, False, False
                if event.key == K_RIGHT and right == False: right, up, down, left = True, False, False, False
                if event.key == K_LEFT and left == False: left, up, right, down = True, False, False, False

#Cuando la serpiente come un cuadrado, se agranda.
        if snake[0][0] == rand2 and snake[0][1] == rand1:
                puntuacion=puntuacion+1
                snake.append([0,0])
                rand1, rand2, R, G, B = randint(1,25),randint(1,25),randint(10,255),randint(10,255),randint(10,255)

        pygame.display.flip()
        
#En caso de que se choque la serpiente con ella misma
#NO APRETES IZQUIERDA O DERECHA DOS VECES PORQUE SE CIERRA Y NO LO PUEDO ARREGLAR
        for i in range(1, len(snake)): 
                if snake[0][0] == snake[i][0] and snake[0][1] == snake[i][1]:
                        print("Puntuacion obtenida:", puntuacion)
                        print("GAME OVER")
                        sys.exit()

                if puntuacion == 10: 
                    print("YOU WIN")
                    sys.exit()

#Movimiento de serpiente
        if right == True: snake = avanzar(snake,[snake[0][0], snake[0][1]+1])
        elif left == True: snake = avanzar(snake,[snake[0][0], snake[0][1]-1])
        elif up == True: snake = avanzar(snake,[snake[0][0]-1, snake[0][1]])
        elif down == True: snake = avanzar(snake,[snake[0][0]+1, snake[0][1]])
        time.sleep(.1)
        pygame.display.update()

def main():
    startWindow()
main()
