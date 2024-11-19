import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_flip_img = pg.transform.flip(bg_img, True, False)
    kk_img = pg.image.load("fig/3.png")
    kk_img = pg.transform.flip(kk_img, True, False)
    kk_img = pg.transform.rotozoom(kk_img, 10, 1.0)

    bg_x = 0
    bg_width = bg_img.get_width()
    kk_rect = kk_img.get_rect()
    kk_rect.center = (300, 200)

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
        bg_x -= 2
        if bg_x <= -bg_width:
            bg_x += bg_width
        screen.blit(bg_img, [bg_x, 0])
        screen.blit(bg_flip_img, [bg_x + bg_width, 0])
        screen.blit(bg_img, [bg_x - bg_width, 0])
        screen.blit(bg_flip_img, [bg_x, 0])

        keys = pg.key.get_pressed()
        if keys[pg.K_UP]:
            kk_rect.move_ip(0, -1)
        if keys[pg.K_DOWN]:
            kk_rect.move_ip(0, 1)
        if keys[pg.K_LEFT]:
            kk_rect.move_ip(-1, 0)
        if keys[pg.K_RIGHT]:
            kk_rect.move_ip(1, 0)

        screen.blit(kk_img, kk_rect)

        pg.display.update()
        clock.tick(200)

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
