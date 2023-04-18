import pygame
pygame.init()

WIDTH, HEIGHT = 800, 600

windows = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60
clock = pygame.time.Clock()

#Сам настроишь шрифт ток селект должен быть тем же ток на 10 больше
fontItelm = pygame.font.SysFont("arial", 45)
fontItelmSelect = pygame.font.SysFont("arial", 55)

#Можешь добавить
items = ["Играть","Выход","Настройки"]
select = 0
selectAdd = 0

running =True
while running:
    for event  in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP: selectAdd = -1
            elif event.key == pygame.K_DOWN: selectAdd = 1
            elif event.key in [pygame.K_RETURN]:
                #Сюда кнопки добалять
                if items[select] == "Выход": running = False

            select = (select + selectAdd) % len(items)

            while items[select] == "":
                select = (select + selectAdd) % len(items)

            selectAdd = 0



    windows.fill("black")
    for i in range(len(items)):
        if i == select:
            text = fontItelmSelect.render(items[i], 1, "white")
        else:
            text = fontItelm.render(items[i], 1, "gray")
        rect = text.get_rect(center = (WIDTH // 2, 200 + 60 * i))
        windows.blit(text, rect)

    pygame.display.update()
    clock.tick((FPS))


pygame.quit()

