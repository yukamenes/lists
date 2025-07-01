import pygame

pygame.init()

WIDTH = 500
HEIGHT = 500
BACGROUND_COLOR = (123, 10, 20)

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame")

clock = pygame.time.Clock()

player_rect = pygame.Rect(0, 0, 100, 100)

background_image = pygame.image.load("forest.png")#!!!!!!!!!!!!!
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))#!!!!!!!!!!!!!


while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
        if e.type == pygame.MOUSEBUTTONDOWN:
            x, y = e.pos
            print(x, y)
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_w:
                print("Ми рухаємось вгору")
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        print("Ми рухаємось вгору")
    window.blit(background_image, (0,0))#!!!!!!!!!!!!!
    
    pygame.draw.rect(window, (0,0,0), player_rect)
    pygame.display.update()
    clock.tick(60)