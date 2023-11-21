import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600)) #練習1：背景画像のSurface
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex01/fig/3.png") #練習2：こうかとん画像のSurface
    kk_img = pg.transform.flip(kk_img, True, False) #練習2：こうかとん左右反転
    kk_imgs = [kk_img, pg.transform.rotozoom(kk_img, 10, 1.0)] #練習3：こうかとんSurfaceリスト
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        screen.blit(bg_img, [0, 0]) #練習4：背景画像表示
        screen.blit(kk_imgs[tmr%2], [300, 200])
        pg.display.update()
        tmr += 1        
        clock.tick(10)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()