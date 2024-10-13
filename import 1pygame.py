import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("2_2")

blue = (135, 206, 235)
green = (34, 139, 34)
brown = (139, 69, 19)
red = (255, 0, 0)
white = (255, 255, 255)
pink = (255, 192, 203)
dark_green = (0, 100, 0)

# Функция для рисования дома
def draw_house(x, y):
    pygame.draw.rect(screen, brown, (x, y, 120, 80))  # Дом
    pygame.draw.rect(screen, blue, (x + 40, y + 20, 40, 40))  # Окно
    pygame.draw.polygon(screen, red, [(x, y), (x + 60, y - 40), (x + 120, y)])  # Крыша

# Функция для рисования дерева
def draw_tree(x, y):
    pygame.draw.rect(screen, brown, (x + 10, y, 10, 60))  # Ствол
    pygame.draw.circle(screen, dark_green, (x + 5, y), 15)
    pygame.draw.circle(screen, dark_green, (x + 30, y), 15)
    pygame.draw.circle(screen, dark_green, (x + 15, y - 15), 15)
    pygame.draw.circle(screen, dark_green, (x , y - 15), 15)
    pygame.draw.circle(screen, dark_green, (x + 35, y - 15), 15)
    pygame.draw.circle(screen, dark_green, (x + 17, y - 30), 15)


# Основной цикл
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()

    # Заполнение фона
    screen.fill(green)
    pygame.draw.rect(screen, blue, (0, 0, 600, 400 // 2))  # Голубая половина

    # Рисуем дома
    draw_house(100, 250)

    draw_house(350, 230)

    # Рисуем деревья
    draw_tree(250, 230)
    draw_tree(500, 250)

    # Рисуем облака
    def draw_cloud(x, y):
        pygame.draw.circle(screen, white, (x + 10, y), 30)
        pygame.draw.circle(screen, white, (x + 30, y), 30)
        pygame.draw.circle(screen, white, (x + 50, y), 30)
        pygame.draw.circle(screen, white, (x + 70, y), 30)
        pygame.draw.circle(screen, white, (x + 20, y - 20), 30)
        pygame.draw.circle(screen, white, (x + 60, y - 20), 30)
    
    draw_cloud(170, 70)
    draw_cloud(350, 100)
    draw_cloud(500, 60)



    # Рисуем солнце
    pygame.draw.circle(screen, pink, (50, 50), 30)


    pygame.display.flip()