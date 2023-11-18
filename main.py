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
lines_quantity = WW/20
is_print_text = False

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
            elif event.key == 96:
                is_print_text = not is_print_text

    # Создание переменной с линиями
    lines = []

    # Добавление линий в переменную линий
    for i in range(random.randint(lines_quantity-4, lines_quantity)):
        lines.append(random.randint(5, 95))

    # Отрисовка линий
    for i in range(len(lines)):
        try:
            pg.draw.line(window, (255, 0, 0), 
                (
                    i*WW/len(lines), 
                    WH - lines[i]*WH/100), 
                (
                    (i+1)*WW/len(lines), 
                    WH - lines[i+1]*WH/100), 10)
        except: 
            pg.draw.line(window, (255, 0, 0), 
                (
                    i*WW/len(lines), 
                    WH - lines[i]*WH/100), 
                (
                    (i+1)*WW/len(lines), 
                    WH - lines[0]*WH/100))

    # Отображение текста
    if is_print_text:
        text = font.render(f'FPS: {float(fps)}', False, (255, 255, 255))
        window.blit(text, (WW-text.get_width()-10, 0))
        text = font.render(f'Lines: {int(lines_quantity-4)}:{int(lines_quantity)}', False, (255, 255, 255))
        window.blit(text, (WW-text.get_width()-10, WH//100))


    # Обновление экрана
    pg.display.update()
    clock.tick(fps)
