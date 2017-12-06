#en esta parte se importan los complementos que va utilizar como Pygame,Time,Random
import pygame
import time
from random import randint,randrange
#aqui se aclaran los colores que se van a utilizarpara las barras de obtaculos
black = (0,0,0)
white = (255,255,255)

sunset = (253,72,47)

greenyellow = (184,255,0)
brightblue = (47,228,253)
orange = (255,113,0)
yellow = (255,236,0)
purple = (252,67,255)
#aqui se aclaran los cambios de colores alos cuales va a ir cambiando segun se valla jujando
colorChoices = [greenyellow,brightblue,orange,yellow,purple]

pygame.init()
#En esta parte se aclara las dimenciones en las cuales van allevar las barras de obstaculos
surfaceWidth = 800
surfaceHeight = 500
#en esta parte van las dimenciiones de la imagen del helicoptero
imageHeight = 43
imageWidth = 100
#En esta parte se aclara el nombre previo de la visualizacion del nombre en este caso 'helicoptero'.
surface = pygame.display.set_mode((surfaceWidth,surfaceHeight))
pygame.display.set_caption('Helicoptero')
clock = pygame.time.Clock()
#Aqui se especifica el nombre  de la imagen del helicoptero y la ruta.
img = pygame.image.load('Helicopter.png')
#ahora se van a declarar los prametros acerca de la puntuacion y los tamaños de blocks y aciones con respecto ala tecla clave 
def score(count):
    font = pygame.font.Font('freesansbold.ttf', 20)
    text = font.render("Score: "+str(count), True, white)
    surface.blit(text, [0,0])


def blocks(x_block, y_block, block_width, block_height, gap, colorChoice):
    
    pygame.draw.rect(surface, colorChoice, [x_block,y_block,block_width,block_height])
    pygame.draw.rect(surface, colorChoice, [x_block,y_block+block_height+gap,block_width, surfaceHeight])
    

def replay_or_quit():
    for event in pygame.event.get([pygame.KEYDOWN, pygame.KEYUP, pygame.QUIT]):
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        elif event.type == pygame.KEYDOWN:
            continue

        return event.key
    
    return None

def makeTextObjs(text, font):
    textSurface = font.render(text, True, sunset)
    return textSurface, textSurface.get_rect()

def msgSurface(text):
    smallText = pygame.font.Font('freesansbold.ttf', 20)
    largeText = pygame.font.Font('freesansbold.ttf', 150)

    titleTextSurf, titleTextRect = makeTextObjs(text, largeText)
    titleTextRect.center = surfaceWidth / 2, surfaceHeight / 2
    surface.blit(titleTextSurf, titleTextRect)

    typTextSurf, typTextRect = makeTextObjs('Presiona Cualquier tecla para volver a jugar', smallText)
    typTextRect.center =  surfaceWidth / 2, ((surfaceHeight / 2) + 100)
    surface.blit(typTextSurf, typTextRect)

    typTextSurf, typTextRect = makeTextObjs('Jorge Miguel Garcia Martinez', smallText)
    typTextRect.center =  surfaceWidth / 2, ((surfaceHeight / 2) + 150)
    surface.blit(typTextSurf, typTextRect)

    typTextSurf, typTextRect = makeTextObjs('Maria Isabel Gallegos Gonzalez', smallText)
    typTextRect.center =  surfaceWidth / 2, ((surfaceHeight / 2) + 200)
    surface.blit(typTextSurf, typTextRect)

    pygame.display.update()
    time.sleep(1)

    while replay_or_quit() == None:
        clock.tick()

    main()

    
#se aclaran los textos que van a mostrar al final de perder el juego 
def gameOver():
    msgSurface('Chocaste!')
    
def helicopter(x, y, image):
    surface.blit(img, (x,y))

#se definen las dimeciones de las barras de obtaculos hacia el helicoptero
def main():
    x = 150
    y = 200
    y_move = 0

    x_block = surfaceWidth
    y_block = 0

    block_width = 75
    block_height = randint(0,(surfaceHeight/2))
    gap = imageHeight * 3
    block_move = 4
    current_score = 0
    

    blockColor = colorChoices[randrange(0,len(colorChoices))]
    
    game_over = False
#aqui se definen las cituacion de chocaste que lo que ocurre si el elicoptero toca las barras de obstaculo
    while not game_over:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y_move = -5
                    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    y_move = 5

        y += y_move

        surface.fill(black)
        helicopter(x ,y, img)
        

        blocks(x_block, y_block, block_width, block_height, gap, blockColor)
        score(current_score)
        x_block -= block_move

        if y > surfaceHeight-40 or y < 0:
            gameOver()

        if x_block < (-1*block_width):
            x_block = surfaceWidth
            block_height = randint(0, (surfaceHeight / 2))
            blockColor = colorChoices[randrange(0,len(colorChoices))]
            current_score+=1

        if x + imageWidth > x_block:
            if x < x_block + block_width:
                if y < block_height:
                    if x - imageWidth < block_width + x_block:
                        gameOver()

        if x + imageWidth > x_block:
            if y + imageHeight > block_height+gap:
                if x < block_width + x_block:
                    gameOver()

        #if x_block < (x - block_width) < x_block + block_move:
        #    current_score += 1
            
        if 3 <= current_score < 5:
            block_move = 5
            gap = imageHeight * 2.9
        if 5 <= current_score < 8:
            block_move = 6
            gap = imageHeight *2.8
        if 8 <= current_score < 14:
            block_move = 7
            gap = imageHeight *2.7
        
                
                

        
            

        pygame.display.update()
        clock.tick(60)

main()
pygame.quit()
quit()

#Jorge Miguel Garcia Martinez
#Maria Isabel Gallegos Gonzalez













    
