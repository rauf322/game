import pygame 
import time 
import random 

pygame.font.init()

WIDTH, HEIGHT = 1000,800
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Space Dodge")

BG = pygame.transform.scale(pygame.image.load("2023-12-12 22.57.23.jpg"),(WIDTH,HEIGHT))

PLAYER_WIDTH = 40
PLAYER_HEIGHT = 60
PLAYER_VEL = 10
FONT = pygame.font.SysFont("comicsans",50)
STAR_WIDTH = 10
STAR_HEIGHT = 20
STAR_VEL = 3 

def draw(player,elaps_time,stars):
    WIN.blit(BG,(0,0))
    
    time_text = FONT.render(f"DICK : {round(elaps_time)}s", 100,"white")
    WIN.blit(time_text,(10,10))

    pygame.draw.rect(WIN,"blue",player)

    for star in stars:
        pygame.draw.rect(WIN,'red',star)

    pygame.display.update()

def main():
    run = True

    player = pygame.Rect(200,HEIGHT-PLAYER_HEIGHT,  PLAYER_WIDTH, PLAYER_HEIGHT)
    clock = pygame.time.Clock()
    start_time = time.time()
    elaps_time = 0

    star_add_increment = 2000
    star_count = 0

    stars = []
    hit = False

    while run:
        star_count += clock.tick(60)
        elaps_time = time.time() - start_time 

        if star_count > star_add_increment:
            for _ in range(3):
                star_x = random.randint(0,WIDTH - STAR_WIDTH)
                star = pygame.Rect(star_x,-STAR_HEIGHT,STAR_WIDTH,STAR_HEIGHT)
                stars.append(star)

            star_add_increment = max(200,star_add_increment - 50)
            star_count = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - PLAYER_VEL >= 0:
            player.x -= PLAYER_VEL
        if keys[pygame.K_RIGHT]and player.x + PLAYER_VEL + player.width <= WIDTH:
            player.x += PLAYER_VEL
        if keys[pygame.K_UP]and player.y - PLAYER_VEL >= 0:
            player.y -= PLAYER_VEL
        if keys[pygame.K_DOWN]and player.y + PLAYER_VEL + player.height <= HEIGHT:
            player.y += PLAYER_VEL

        for star in stars[:]:
            star.y += STAR_VEL
            if star.y > HEIGHT:
                stars.remove(star)
            elif star.y + star.height >= player.y and star.colliderect(player):
                stars.remove(star)
                hit = True
                break

        if hit:
            lost_text = FONT.render("You sucked!",1,"white")
            WIN.blit(lost_text,(WIDTH/2-lost_text.get_width()/2,HEIGHT/2 -lost_text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(4000)
            break

        draw(player,elaps_time,stars)
    
    pygame.quit()


if __name__ == "__main__":
    main()
