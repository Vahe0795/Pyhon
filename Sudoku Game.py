import pygame
from dokusan import generators
import numpy as np
import random

pygame.font.init()

screen = pygame.display.set_mode((505, 620))

pygame.display.set_caption("SUDOKU SOLVER USING BACKTRACKING")

x = 0
y = 0
dif = 500 / 9
val = 0

grid = np.array(list(str(generators.random_sudoku(avg_rank=random.randrange(300)))))
grid = grid.reshape(9, 9)
grid = grid.astype(np.int64)

font1 = pygame.font.SysFont("comicsans", 30)
font2 = pygame.font.SysFont("comicsans", 20)


def get_cord(pos):
    global x
    x = pos[0] // dif
    global y
    y = pos[1] // dif


def draw_box():
    for i in range(2):
        pygame.draw.line(screen, (255, 0, 0), (x * dif - 3, (y + i) * dif), (x * dif + dif + 3, (y + i) * dif), 7)
        pygame.draw.line(screen, (255, 0, 0), ((x + i) * dif, y * dif), ((x + i) * dif, y * dif + dif), 7)


def draw():
    for i in range(9):
        for j in range(9):
            if grid[i][j] != 0:
                pygame.draw.rect(screen, (0, 153, 153), (i * dif, j * dif, dif + 1, dif + 1))

                text1 = font1.render(str(grid[i][j]), 1, (0, 0, 0))
                screen.blit(text1, (i * dif + 15, j * dif + 15))
    for i in range(10):
        if i % 3 == 0:
            thick = 7
        else:
            thick = 1
        pygame.draw.line(screen, (0, 0, 0), (0, i * dif), (500, i * dif), thick)
        pygame.draw.line(screen, (0, 0, 0), (i * dif, 0), (i * dif, 500), thick)


def draw_val(val):
    text1 = font1.render(str(val), 1, (0, 0, 0))
    screen.blit(text1, (x * dif + 15, y * dif + 15))


def raise_error1():
    text1 = font1.render("WRONG !!!", 1, (0, 0, 0))
    screen.blit(text1, (20, 570))


def raise_error2():
    text1 = font1.render("Wrong !!! Not a valid Key", 1, (0, 0, 0))
    screen.blit(text1, (20, 570))


def valid(m, i, j, val):
    for it in range(9):
        if m[i][it] == val:
            return False
        if m[it][j] == val:
            return False
    it = i // 3
    jt = j // 3
    for i in range(it * 3, it * 3 + 3):
        for j in range(jt * 3, jt * 3 + 3):
            if m[i][j] == val:
                return False
    return True


def solve(grid, i, j):
    while grid[i][j] != 0:
        if int(i) < 8:
            i = int(i) + 1
        elif int(i) == 8 and int(j) < 8:
            i = 0
            j = int(j) + 1
        elif int(i) == 8 and int(j) == 8:
            return True
    pygame.event.pump()
    for it in range(1, 10):
        if valid(grid, i, j, it):
            grid[i][j] = it
            global x, y
            x = i
            y = j

            screen.fill((255, 255, 255))
            draw()
            draw_box()
            pygame.display.update()
            pygame.time.delay(20)
            if solve(grid, i, j) == 1:
                return True
            else:
                grid[i][j] = 0

            screen.fill((255, 255, 255))

            draw()
            draw_box()
            pygame.display.update()
            pygame.time.delay(50)
    return False


def instruction():
    text1 = font2.render("PRESS R TO RESET / U TO UPDATE THE GAME", 1, (0, 0, 0))
    text2 = font2.render("ENTER VALUES AND PRESS ENTER TO VISUALIZE", 1, (0, 0, 0))
    screen.blit(text1, (20, 520))
    screen.blit(text2, (0, 540))


def result():
    text1 = font1.render("FINISHED PRESS U", 1, (0, 0, 0))
    screen.blit(text1, (80, 570))


run = True
flag1 = 0
flag2 = 0
rs = 0
error = 0

while run:

    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            flag1 = 1
            pos = pygame.mouse.get_pos()
            get_cord(pos)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x -= 1
                flag1 = 1
            if event.key == pygame.K_RIGHT:
                x += 1
                flag1 = 1
            if event.key == pygame.K_UP:
                y -= 1
                flag1 = 1
            if event.key == pygame.K_DOWN:
                y += 1
                flag1 = 1
            if event.key == pygame.K_1 or event.key == pygame.K_KP1:
                val = 1
            if event.key == pygame.K_2 or event.key == pygame.K_KP2:
                val = 2
            if event.key == pygame.K_3 or event.key == pygame.K_KP3:
                val = 3
            if event.key == pygame.K_4 or event.key == pygame.K_KP4:
                val = 4
            if event.key == pygame.K_5 or event.key == pygame.K_KP5:
                val = 5
            if event.key == pygame.K_6 or event.key == pygame.K_KP6:
                val = 6
            if event.key == pygame.K_7 or event.key == pygame.K_KP7:
                val = 7
            if event.key == pygame.K_8 or event.key == pygame.K_KP8:
                val = 8
            if event.key == pygame.K_9 or event.key == pygame.K_KP9:
                val = 9
            if event.key == pygame.K_RETURN:
                flag2 = 1
            if event.key == pygame.K_r:
                rs = 0
                error = 0
                flag2 = 0
                grid = [
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0]
                ]
            if event.key == pygame.K_u:
                rs = 0
                error = 0
                flag2 = 0
                grid = np.array(list(str(generators.random_sudoku(avg_rank=random.randrange(300)))))
                grid = grid.reshape(9, 9)
                grid = grid.astype(np.int64)

    if flag2 == 1:
        if not solve(grid, 0, 0):
            error = 1
        else:
            rs = 1
        flag2 = 0
    if val != 0:
        draw_val(val)

        if valid(grid, int(x), int(y), val):
            grid[int(x)][int(y)] = val
            flag1 = 0
        else:
            grid[int(x)][int(y)] = 0
            raise_error2()
        val = 0

    if error == 1:
        raise_error1()
    if rs == 1:
        result()
    draw()
    if flag1 == 1:
        draw_box()
    instruction()

    pygame.display.update()

pygame.quit()

