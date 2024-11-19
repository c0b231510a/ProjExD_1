import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img = pg.transform.scale(bg_img, (1600, 900))
    kk_img = pg.image.load("fig/3.png")
    kk_img = pg.transform.flip(kk_img, True, False)

    bg_x = 0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        bg_x -= 2
        if bg_x <= -1600:
            bg_x += 1600

        screen.blit(bg_img, [bg_x, 0])
        screen.blit(bg_flip_img, [bg_x + 1600, 0])
        screen.blit(bg_img, [bg_x - 1600, 0])
        screen.blit(bg_flip_img, [bg_x, 0])
        screen.blit(kk_img, [300, 200])

        pg.display.update()
        clock.tick(200)

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()