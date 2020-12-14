import pygame
import pygame_gui
#import sample_drow.py as dr
import calc_impr as calc
pygame.init()
calc.init()
WIDTH = 700
HEIGHT = 700
pygame.display.set_caption('Множество Жулиа')
window_surface = pygame.display.set_mode((2*WIDTH, HEIGHT))

background = pygame.Surface((2*WIDTH, HEIGHT))
background.fill(pygame.Color('#000000'))



def increase(dmx, dmy):
    print("эта функция что-то делает")
    return (dmx/1.2, dmy/1.2)
def move():
    print("эта функция что-то")
def julia():
    print("эта функция что-то")
def enlarge_area():
    print("эта функция что-то")
def red(dmx, dmy):
    return(dmx*1.2, dmy*1.2)
x = 45
y = 80
dx = 80
manager = pygame_gui.UIManager((1200, 700), 'theme.json')
button1 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((x, y), (50, 50)),
                                             text='+',
                                             manager=manager)
button2 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((x + dx, y), (50, 50)),
                                             text='-',
                                             manager=manager)
button3 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((x + 2*dx, y), (50, 50)),
                                             text='[+]',
                                             manager=manager)
button4 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((x + 3*dx, y), (55, 50)),
                                             text='julia',
                                             manager=manager)
button5 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((x + 4*dx, y), (50, 50)),
                                             text='move',
                                             manager=manager)
button6 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((x + 5*dx, y), (50, 50)),
                                             text='home',
                                             manager=manager)
x = 750
y = 80
dx = 80
button7 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((x, y), (50, 50)),
                                             text='+',
                                             manager=manager)
button8 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((x + dx, y), (50, 50)),
                                             text='-',
                                             manager=manager)
button9 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((x + 2*dx, y), (50, 50)),
                                             text='[+]',
                                             manager=manager)
button10 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((x + 3*dx, y), (55, 50)),
                                             text='julia',
                                             manager=manager)
button11 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((x + 4*dx, y), (50, 50)),
                                             text='move',
                                             manager=manager)
button12 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((x + 5*dx, y), (50, 50)),
                                             text='home',
                                             manager=manager)
text_coor1 = (50, 20)
text_coor2 = (770, 20)
f = pygame.font.SysFont('arial', 30)
text1 = f.render('множество Мандельброта', True, (255, 255, 255))
text2 = f.render('множество Жюлиа', True, (255, 255, 255))
background.blit(text1, text_coor1)
background.blit(text2, text_coor2)
width = 500
height = 500
surf1 = pygame.Surface((width, height))
surf2 = pygame.Surface((width, height))
surf1.fill((255, 255, 255))
surf2.fill((255, 255, 255))
s1_coor = (30, 150)
s2_coor = (700, 150)
def create_fractal(mx1, my1, dmx1, dmx2, jx1, jy1, djx1, djy1 ):
    mx = mx1
    my = my1
    dmx = dmx1
    dmy = dmx2
    jx = jx1
    jy = jy1
    djx = djx1
    djy = djy1
    cx = -0.1225611669
    cy =  -0.7448617670 
    points1 = calc.calc_man(width, height, mx, my, dmx, dmy)
    points2 = calc.calc_jul(width, height, cx, cy, jx, jy, djx, djy)
    newSurf_m = pygame.surfarray.make_surface(points1)
    newSurf_j = pygame.surfarray.make_surface(points2)
    surf1.blit(newSurf_m, (0, 0))
    surf2.blit(newSurf_j, (0, 0))
    calc.free()
    background.blit(surf1, s1_coor)
    background.blit(surf2, s2_coor)



clock = pygame.time.Clock()
is_running = True
mx = 0
my = 0
dmx = 3
dmy = 3
jx = 0
jy = 0
djx = 3
djy = 3
while is_running:
    time_delta = clock.tick(60)/1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        if event.type == pygame.MOUSEBUTTONUP and (mx != event.pos[0] or my != event.pos[1]):
            x, y = event.pos
            if x >= 30 and y >= 150 and x <= 650 and y <= 650:
                mx, my = event.pos
                mx -= 30
                my -= 150
                mx = 500 - mx
                my = 500 - my
                mx = mx / 500
                my = my / 500
       # print(mx, my)
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == button1:
                    dmx, dmy = increase(dmx, dmy)
                if event.ui_element == button2:
                    dmx, dmy = red(dmx, dmy)
                if event.ui_element == button3:
                    enlarge_area()
                if event.ui_element == button4:
                    move()
                if event.ui_element == button5:
                    julia()
                if event.ui_element == button6:
                    dmx, dmy, mx, my = 3, 3, 0, 0

                if event.ui_element == button7:
                    djx, djy = increase(djx, djy)
                if event.ui_element == button8:
                    djx, djy = red(djx, djy)
                if event.ui_element == button9:
                    enlarge_area()
                if event.ui_element == button12:
                    jx = 0
                    jy = 0
                    djx = 3
                    djy = 3
        manager.process_events(event)

    manager.update(time_delta)
    #mx = 0
    #my = 0
    create_fractal(mx, my, dmx, dmy, jx, jy, djx, djy)
    window_surface.blit(background, (0, 0))
    manager.draw_ui(window_surface)

    pygame.display.update()
