import pygame
import time
import random
import pygame_menu
# ------------------импорты
size = [900,400]
snake_color = (106,90,205)#
head_color = (255,3,62)
game_over_color = (227,38,54)
food_color = (137,172,118)
snake_list = []
snake_length = 1
snake_block = 10#

delta = [0,0]#
pygame.init()#
clock = pygame.time.Clock()#
font_style = pygame.font.SysFont(None, 50)#
score_style = pygame.font.SysFont(None,20)
screen = pygame.display.set_mode(size)#
#
pygame.display.set_caption("Snake by Misha")

def knopka(event):#
    if event.key == pygame.K_LEFT:
        delta = [-snake_block,0]
    if event.key == pygame.K_RIGHT:
        delta = [snake_block, 0]
    if event.key == pygame.K_UP:
        delta = [0, -snake_block]
    if event.key == pygame.K_DOWN:
        delta = [0, snake_block]
    return(delta)

def print_score (point):
    render = score_style.render("очки: "+ str(point), True, (255,255,255))
    screen.blit(render, [5,5])
    #
def draw_snake(snake_list):
    for i in snake_list:
        pygame.draw.rect(screen, snake_color, [i[0], i[1], snake_block, snake_block])
    if len(snake_list) > 1:
        k = len(snake_list)
        pygame.draw.rect(screen, head_color, [snake_list[k - 1][0], snake_list[k - 1][1], snake_block, snake_block])
#
def print_message(text, color):
    render = font_style.render(text, True, color)  #
    screen.blit(render, [(size[0] / 2), (size[1] / 2)])

def start_the_game():
    x1 = 300#
    y1 = 300
    playing = True
    delta = [0,0]#
    snake_list = []

    snake_length = 1
    foodx = round(random.randrange(0,size[0] - snake_block)/ 10.0) * 10.0
    foody = round(random.randrange(0,size[1] - snake_block)/ 10.0) * 10.0
    while playing:#
        for event in pygame.event.get():#
            if event.type == pygame.KEYDOWN:#
                delta = knopka(event) #
            if event.type == pygame.QUIT:
                pygame.quit()
        if x1 >= size[0] or y1 >= size[1] or x1 < 0 or y1 < 0:
            playing = False
            print_message("Вы проиграли",game_over_color)
            pygame.display.update()
            time.sleep(5)
        x1 += delta[0]#
        y1 += delta[1]
        screen.fill((0,0,0))#
        pygame.draw.rect(screen,snake_color,[x1,y1,snake_block,snake_block])#
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]
        draw_snake(snake_list)
        pygame.draw.rect(screen, food_color, [foodx, foody, snake_block, snake_block])
        print_score(snake_length - 1)
        pygame.display.update()#
        if x1 == foodx and y1 == foody:
            snake_length += 1
            foodx = round(random.randrange(0, size[0] - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, size[1] - snake_block) / 10.0) * 10.0
        touching = snake_list.copy()
        head = touching.pop()
        for i in touching:
            if i == head:
                playing = False
        if touching in snake_list:
            playing = False
        clock.tick(5)#

menu = pygame_menu.Menu('Добро пожаловать', 400, 300, theme=pygame_menu.themes.THEME_BLUE)
menu.add.text_input('Имя :', default='Snake by Misha')
menu.add.button('Играть', start_the_game)
menu.add.button('Выйти', pygame_menu.events.EXIT)

while True:

	events = pygame.event.get()
	for event in events:
		if event.type == pygame.QUIT:
			exit()

	if menu.is_enabled():
		menu.update(events)
		menu.draw(screen)

	pygame.display.update()


pygame.quit()
quit()
