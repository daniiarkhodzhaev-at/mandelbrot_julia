import pygame
import pygame_gui
import pygame.draw as dr
import calc_impr as calc
pygame.init()
calc.init()
WIDTH = 1230
HEIGHT = 700
pygame.display.set_caption('Множество Жюлиа')
window_surface = pygame.display.set_mode((WIDTH, HEIGHT))

background = pygame.Surface((WIDTH, HEIGHT))
background.fill(pygame.Color('#000000'))


def increase(dmx, dmy):
    print("эта функция что-то делает")
    return (dmx/1.2, dmy/1.2)
def move():
    print("эта функция что-то")
    pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_ARROW)
def julia():
    print("эта функция что-то")
    pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_CROSSHAIR)
def enlarge_area():
    print("эта функция что-то")
def red(dmx, dmy):
    return(dmx*1.2, dmy*1.2)
x = 95
y = 80
dx = 80
manager = pygame_gui.UIManager((1200, 700), 'theme.json')
button1 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((x, y), (50, 50)),
                                             text='+',
                                             manager=manager)
button2 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((x + dx, y), (50, 50)),
                                             text='-',
                                             manager=manager)
button4 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((x + 2*dx, y), (55, 50)),
                                             text='julia',
                                             manager=manager)
button5 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((x + 3*dx, y), (50, 50)),
                                             text='move',
                                             manager=manager)
button6 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((x + 4*dx, y), (50, 50)),
                                             text='home',
                                             manager=manager)
x1 = 840
y1 = 80
dx1 = 80
button7 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((x1, y1), (50, 50)),
                                             text='+',
                                             manager=manager)
button8 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((x1 + dx1, y1), (50, 50)),
                                             text='-',
                                             manager=manager)
button12 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((x1 + 2*dx1, y1), (50, 50)),
                                             text='home',
                                             manager=manager)
text_coor1 = (80, 20)
text_coor2 = (790, 20)
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
dr.rect(background, (255, 0, 0), (s1_coor[0], s1_coor[1], width, width), 8)
dr.rect(background, (255, 0, 0), (s2_coor[0], s2_coor[1], width, width), 8)
def create_man(mx1, my1, dmx1, dmx2):
    mx = mx1
    my = my1
    dmx = dmx1
    dmy = dmx2
    points1 = calc.calc_man(width, height, mx, my, dmx, dmy)
    newSurf_m = pygame.surfarray.make_surface(points1)
    surf1.blit(newSurf_m, (0, 0))
    calc.free()
    background.blit(surf1, s1_coor)
def create_jul(cx1, cy1, jx1, jy1, djx1, djy1 ):
    cx = cx1
    cy = cy1
    jx = jx1
    jy = jy1
    djx = djx1
    djy = djy1
    points2 = calc.calc_jul(width, height, cx, cy, jx, jy, djx, djy)
    newSurf_j = pygame.surfarray.make_surface(points2)
    surf2.blit(newSurf_j, (0, 0))
    calc.free()
    background.blit(surf2, s2_coor)


clock = pygame.time.Clock()
is_running = True
mx = 0
my = 0
dmx = 3
dmy = 3
cx = -0.1225611669
cy =  -0.7448617670 
jx = 0
jy = 0
djx = 3
djy = 3
flag = 0
flag1 = 0
flag2 = 0
create_man(mx, my, dmx, dmy)
create_jul(cx, cy, jx, jy, djx, djy)
x0, y0, x1, y1 = 0, 0, 0, 0
while is_running:
    flag = 0
    flag1 = 0
    flag2 = 0
    time_delta = clock.tick(60)/1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x0, y0 = event.pos
            print("мышку нажали", x0, y0)
        if event.type == pygame.MOUSEBUTTONUP:
            x1, y1 = event.pos
            print("мышку отпустили")
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == button1:
                    dmx, dmy = increase(dmx, dmy)
                    flag = 1
                if event.ui_element == button2:
                    dmx, dmy = red(dmx, dmy)
                    flag = 1
                if event.ui_element == button4:
                    julia()
                if event.ui_element == button5:
                    move()
                if event.ui_element == button6:
                    dmx, dmy, mx, my = 3, 3, 0, 0
                    flag = 1
                if event.ui_element == button7:
                    djx, djy = increase(djx, djy)
                    flag = 1
                if event.ui_element == button8:
                    djx, djy = red(djx, djy)
                    flag = 1 
                if event.ui_element == button12:
                    jx, jy, djx, djy = 0, 0, 3, 3
        manager.process_events(event)

    manager.update(time_delta)
    #mx = 0
    #my = 0
    if((x0 != x1 or y0 != y1) and x1 >= s1_coor[0] and x1 <= s1_coor[0] + width and y1 >= s1_coor[1] and y1 <= s1_coor[1] + height and x0 >= s1_coor[0] and x0 <= s1_coor[0]+width and y0 >= s1_coor[1]  and y0 <= s1_coor[1] + height):
        print("COOR", x0, y0)
        flag1 = 1
    if((x0 != x1 or y0 != y1) and x1 >= s2_coor[0] and x1 <= s2_coor[0] + width and y1 >= s2_coor[1] and y1 <= s2_coor[1] + height and x0 >= s2_coor[0] and x0 <= s2_coor[0]+width and y0 >= s2_coor[1]  and y0 <= s2_coor[1] + height):
        #print("COOR222", x0, y0)
        flag2 = 1
    if(flag == 1 or flag1 == 1 or flag2 == 1):
        if(flag1 == 1):
            mx -= (x1 - x0)/width*dmx
            my -= (y1 - y0)/height*dmy
        if(flag2 == 1):
            #print('второй if сработал')
            jx -= (x1 - x0)/width*djx
            jy -= (y1 - y0)/height*djy
        create_man(mx, my, dmx, dmy)
        create_jul(cx, cy, jx, jy, djx, djy)
        x0, y0, x1, y1 = 0, 0, 0, 0
        flag = 0
        flag1 = 0
        flag2 = 0
    window_surface.blit(background, (0, 0))
    manager.draw_ui(window_surface)

    pygame.display.update()
