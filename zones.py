from hero_all.hero_class import *
from field_all.field_zones import *

all_sprites = pygame.sprite.Group()
hero_group = pygame.sprite.Group()
barriers = pygame.sprite.Group()
walls = pygame.sprite.Group()
rooms = pygame.sprite.Group()
floor = pygame.sprite.Group()
furniture = pygame.sprite.Group()
bullets = pygame.sprite.Group()

pygame.init()
size = width, height = 700, 600
pygame.display.set_caption('Игровое поле')
screen = pygame.display.set_mode(size)

if __name__ == '__main__':

    game = Field()

    hero_group = pygame.sprite.Group()
    hero = Hero(main.all_sprites, hero_group)
    hero.set_place(343, 293)
    MOVING = pygame.USEREVENT + 1
    pygame.time.set_timer(MOVING, 10)
    screen.fill(pygame.Color('white'))

    s = pygame.Surface((700, 600))
    # s.fill(pygame.Color(115, 115, 115))
    s.set_alpha(100)
    pix = pygame.PixelArray(s)
    pix[:] = (115, 115, 115)
    # pix[100:250] = (255, 255, 255)
    # pix[:100] = (115, 115, 115)
    # pix[251:] = (115, 115, 115)
    for y in range(600):
        for x in range(700):
            if (x - 300) ** 2 + (y - 350) ** 2 <= 150 ** 2:
                pix[y][x] = 16777215
    del pix

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == MOVING:
                game.move(hero, 1)
                main.bullets.update()
                screen.fill((255, 255, 255))

            if event.type == pygame.MOUSEBUTTONDOWN:
                hero.fire(event.pos)

            if event.type == pygame.QUIT:
                running = False

        game.render()

        main.all_sprites.draw(screen)
        screen.blit(s, (0, 0), special_flags=pygame.BLEND_RGB_MULT)

        # screen.fill(pygame.Color(115, 115, 115), special_flags=pygame.BLEND_RGB_MULT)
        # color = pygame.Color('white')
        # pygame.draw.circle(screen, color, (hero.rect.x, hero.rect.y), 100)
        # print(screen)

        # print(len(pix[0]))
        # s.fill((255, 255, 255))  # this fills the entire surface
        # screen.fill((255, 255, 255))
        # screen.blit(s, (0, 0), special_flags=pygame.BLEND_RGB_MULT)

        pygame.display.flip()
    pygame.quit()
