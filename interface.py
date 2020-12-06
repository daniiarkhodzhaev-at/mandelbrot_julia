import pygame
import pygame_gui


pygame.init()

pygame.display.set_caption('Множество Жулиа')
window_surface = pygame.display.set_mode((1400, 700))

background = pygame.Surface((1400, 700))
background.fill(pygame.Color('#000000'))


def increase():
    print("эта функция что-то делает")
def move():
    print("эта функция что-то")
def home():
    print("эта функция что-то")
def julia():
    print("эта функция что-то")
def enlarge_area():
    print("эта функция что-то")
def red():
    print("эта функция что-то")
x = 20
y = 20
manager = pygame_gui.UIManager((1200, 700), 'theme.json')
button1 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((x, y), (50, 50)),
                                             text='+',
                                             manager=manager)
button2 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((x + 100, 20), (50, 50)),
                                             text='-',
                                             manager=manager)
button3 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((x + 200, 20), (50, 50)),
                                             text='[+]',
                                             manager=manager)
button4 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((x + 300, 20), (150, 50)),
                                             text='множество жулиа',
                                             manager=manager)
button5 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((x + 500, 20), (100, 50)),
                                             text='Переместить',
                                             manager=manager)
button6 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((x + 650, 20), (100, 50)),
                                             text='Домой',
                                             manager=manager)
text_coor1 = (50, 100)
text_coor2 = (720, 100)
f = pygame.font.SysFont('arial', 30)
text1 = f.render('множество Мандельброта', True, (255, 255, 255))
text2 = f.render('множество Жюлиа', True, (255, 255, 255))
background.blit(text1, text_coor1)
background.blit(text2, text_coor2)
surf1 = pygame.Surface((550, 500))
surf2 = pygame.Surface((550, 500))
surf1.fill((255, 255, 255))
surf2.fill((255, 255, 255))
s1_coor = (30, 150)
s2_coor = (700, 150)
image1 = pygame.image.load('maxresdefault.bmp')
image2 = pygame.image.load('julia.bmp')
surf1.blit(image1, (0, 0))
surf2.blit(image2, (0, 0))
background.blit(surf1, s1_coor)
background.blit(surf2, s2_coor)



clock = pygame.time.Clock()
is_running = True

while is_running:
    time_delta = clock.tick(60)/1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == button1:
                    increase()
                if event.ui_element == button2:
                    red()
                if event.ui_element == button3:
                    enlarge_area()
                if event.ui_element == button4:
                    move()
                if event.ui_element == button5:
                    julia()
                if event.ui_element == button6:
                    home()
        manager.process_events(event)

    manager.update(time_delta)

    window_surface.blit(background, (0, 0))
    manager.draw_ui(window_surface)

    pygame.display.update()
