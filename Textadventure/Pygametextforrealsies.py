import pygame as pg
import os



def main():
    screen = pg.display.set_mode((1850, 1000))
    font = pg.font.Font(None, 32)
    clock = pg.time.Clock()
    input_box = pg.Rect(1300, 100, 600, 50)
    color_inactive = pg.Color('lightskyblue3')
    color_active = pg.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''
    done = False
    room = 0
    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            if event.type == pg.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if input_box.collidepoint(event.pos):
                    # Toggle the active variable.
                    active = not active
                else:
                    active = False
                # Change the current color of the input box.
                color = color_active if active else color_inactive
            if event.type == pg.KEYDOWN:
                if active:
                    if event.key == pg.K_RETURN:
                        print(text)
                        text = ''
                        pg.draw.rect(screen, color, input_box)
                    elif event.key == pg.K_BACKSPACE:
                        text = text[:-1]
                        pg.draw.rect(screen, color, input_box)
                        txt_surface = font.render(text, True, color)
                        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
                    else:
                        text += event.unicode



        bg = pg.image.load(os.path.join("images", "map_25x20.png"))
        screen.blit(bg, (0,0))
        # Render the current text.
        txt_surface = font.render(text, True, pg.Color("black"))
        width = 550
        input_box.w = width

        # Blit the input_box rect.
        pg.draw.rect(screen, color, input_box)
        # Blit the text.
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))

        pg.display.flip()
        clock.tick(30)
        

if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()