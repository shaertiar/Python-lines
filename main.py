import pygame as pg
import random

# Иниацилизация
pg.init()

# Создание часов
clock = pg.time.Clock()

# Создание окна
window = pg.display.set_mode()
pg.display.set_caption('Lines')
WW, WH = window.get_size()
fps = 12.8

# Переменные 
lines_color = (255, 0, 0)
lines_quantity = WW//20
lines_width = 1
is_print_text = False
is_random_quantity = True
is_show_grid = False

# Создание шрифта
font = pg.font.SysFont('Arial', WH//100)

# Игровой цикл
is_game = True
while is_game:
    # Окрашивание окна в черный
    window.fill((0, 0, 0))

    # Обработка событий
    for event in pg.event.get():
        # Обработка закрытия окна
        if event.type == pg.QUIT:
            is_game = False

        # Обработка нажатий на клавиши
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_UP:
                fps *= 2
            elif event.key == pg.K_DOWN:
                if fps > 0.1: 
                    fps /= 2
                else:
                    fps = 0.1

            elif event.key == pg.K_RIGHT:
                lines_quantity += 5
            elif event.key == pg.K_LEFT:
                if lines_quantity > 10: 
                    lines_quantity -= 5
                else:
                    lines_quantity = 5

            elif event.key == pg.K_EQUALS:
                lines_width += 1
            elif event.key == pg.K_MINUS:
                if lines_width >= 2:
                    lines_width -= 1

            elif event.key == 96: # key 96 = `
                is_print_text = not is_print_text

            elif event.key == pg.K_q:
                is_random_quantity = not is_random_quantity

            elif event.key == pg.K_g:
                is_show_grid = not is_show_grid

    # Создание переменной с линиями
    lines = []

    # Добавление линий в переменную линий
    if is_random_quantity:
        for i in range(random.randint(lines_quantity-4, lines_quantity)):
            lines.append(random.randint(50, 950))
    else: 
        for i in range(lines_quantity):
            lines.append(random.randint(50, 950))

    # Отрисовка линий сетки
    if is_show_grid:
        for i in range(len(lines)):
            pg.draw.line(window, (3, 3, 50), (i*WW/len(lines), 0), (i*WW/len(lines), WH))
            pg.draw.line(window, (3, 50, 3), (0, WH - lines[i]*WH/1000), (WW, WH - lines[i]*WH/1000))

            # Отрисовка позиций сетки
            if is_print_text:
                window.blit(font.render(str(round(i*WW/len(lines), 1)), False, (6, 6, 100)), (i*WW/len(lines), 0))
                window.blit(font.render(str(round(WH - lines[i]*WH/1000, 1)), False, (6, 100, 6)), (0, WH - lines[i]*WH/1000))

    # Отрисовка линий
    for i in range(len(lines)):
        try:
            pg.draw.line(window, (255, 0, 0), (i*WW/len(lines), WH - lines[i]*WH/1000), ((i+1)*WW/len(lines), WH - lines[i+1]*WH/1000), lines_width)
        except: 
            pg.draw.line(window, (255, 0, 0), (i*WW/len(lines), WH - lines[i]*WH/1000), ((i+1)*WW/len(lines), WH - lines[0]*WH/1000), lines_width)

    # Отображение текста
    if is_print_text:
        text = font.render(f'FPS: {float(fps)}/{round(clock.get_fps(), 1)} [↑][↓]', False, (255, 255, 255))
        window.blit(text, (WW-text.get_width()-10, 0))
        if is_random_quantity:
            text = font.render(f'Lines quantity: {int(lines_quantity-4)}:{int(lines_quantity)} [←][→]', False, (255, 255, 255))
            window.blit(text, (WW-text.get_width()-10, WH//100))
        else:
            text = font.render(f'Lines quantity: {int(lines_quantity)} [←][→]', False, (255, 255, 255))
            window.blit(text, (WW-text.get_width()-10, WH//100))
        text = font.render(f'Linew width: {lines_width} [-][=]', False, (255, 255, 255))
        window.blit(text, (WW-text.get_width()-10, WH//50))
        text = font.render(f'Random lines quantity: {is_random_quantity} [q]', False, (255, 255, 255))
        window.blit(text, (WW-text.get_width()-10, WH//33.333))
        text = font.render(f'Show grid: {is_show_grid} [g]', False, (255, 255, 255))
        window.blit(text, (WW-text.get_width()-10, WH//25))


    # Обновление экрана
    pg.display.update()
    clock.tick(fps)
