#!/usr/bin/python3

import pygame
import pygame_gui
import pygame.draw as dr
import calc_impr as calc

pygame.init()
calc.init()

JULIA = 0
MOVE = 1

WIDTH = 1230
HEIGHT = 700

c1, c2, c3 = (128,0,0), (0,128,0), (0,0,128)
c4, c5, c6 = (220,20,60), (0,100,0), (75,0,130)
c7, c8, c9 = (139,0,139), (30,144,255), (255,140,0)
c10, c11, c12  = (255, 255, 0), (255, 165, 0), (64, 224, 208)
p1 = (c1, c2, c3)
p2 = (c4, c5, c6)
p3 = (c7, c8, c9)
p4 = (c1, c4, c7)
p5 = (c2, c5, c8)
p6 = (c3, c6, c9)
p7 = (c1, c5, c9)
p8 = (c7, c5, c3)
p9 = (c10, c11, c12)
p10 = (c2, c9, c10)
pallete = (p1, p2, p3, p4, p5, p6, p7, p8, p9, p10)
pygame.display.set_caption('Множество Жюлиа')
window_surface = pygame.display.set_mode((WIDTH, HEIGHT))

background = pygame.Surface((WIDTH, HEIGHT))
background.fill(pygame.Color('#000000'))

CURSOR_CHANGE_FEATURE = "mouse" in pygame.__dict__ and\
        "set_system_cursor" in pygame.mouse.__dict__

def increase_sc(dmx, dmy):
    return (dmx/1.2, dmy/1.2)
def pick_move_tool():
    if (CURSOR_CHANGE_FEATURE):
        pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_ARROW)
def pick_julia_tool():
    if (CURSOR_CHANGE_FEATURE):
        pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_CROSSHAIR)
def reduce_sc(dmx, dmy):
    return(dmx*1.2, dmy*1.2)
x = 95
y = 80
dx = 80

manager = pygame_gui.UIManager((1200, 700), 'theme.json')
button_man_plus = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((x, y), (50, 50)),
        text='+',
        manager=manager)

button_man_minus = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((x + dx, y), (50, 50)),
        text='-',
        manager=manager)

button_man_julia_point = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((x + 2*dx, y), (55, 50)),
        text='julia',
        manager=manager)

button_man_move = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((x + 3*dx, y), (50, 50)),
        text='move',
        manager=manager)

button_man_home = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((x + 4*dx, y), (50, 50)),
        text='home',
        manager=manager)

x1 = 840
y1 = 80
dx1 = 80
button_jul_plus = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((x1, y1), (50, 50)),
        text='+',
        manager=manager)

button_jul_minus = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((x1 + dx1, y1), (50, 50)),
        text='-',
        manager=manager)

button_jul_home = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((x1 + 2*dx1, y1), (50, 50)),
        text='home',
        manager=manager)


button_pallete_change = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((585, y1), (70, 50)),
        text='colors',
        manager=manager)

text_coor_man = (80, 20)
text_coor_jul = (790, 20)
font_arial_30 = pygame.font.SysFont('arial', 30)

text_man = font_arial_30.render('множество Мандельброта', True, (255, 255, 255))
text_jul = font_arial_30.render('множество Жюлиа', True, (255, 255, 255))
background.blit(text_man, text_coor_man)
background.blit(text_jul, text_coor_jul)

width = 500
height = 500
surf_man = pygame.Surface((width, height))
surf_jul = pygame.Surface((width, height))
surf_man.fill((255, 255, 255))
surf_jul.fill((255, 255, 255))

offset_man = (30, 150)
offset_jul = (700, 150)

dr.rect(background, (255, 0, 0), (offset_man[0], offset_man[1], width, width), 8)
dr.rect(background, (255, 0, 0), (offset_jul[0], offset_jul[1], width, width), 8)

def create_man(mx, my, dmx, dmy):
    points_man = calc.calc_man(width, height, mx, my, dmx, dmy)
    newSurf_m = pygame.surfarray.make_surface(points_man)
    surf_man.blit(newSurf_m, (0, 0))
    calc.free()
    background.blit(surf_man, offset_man)
    print("MAN")

def create_jul(cx, cy, jx, jy, djx, djy):
    points_jul = calc.calc_jul(width, height, cx, cy, jx, jy, djx, djy)
    newSurf_j = pygame.surfarray.make_surface(points_jul)
    surf_jul.blit(newSurf_j, (0, 0))
    calc.free()
    background.blit(surf_jul, offset_jul)
    print("JUL")


clock = pygame.time.Clock()
flag_running = True

mx_init = 0
my_init = 0
dmx_init = 3
dmy_init = 3
cx_init = -0.1225611669
cy_init = -0.7448617670
jx_init = 0
jy_init = 0
djx_init = 3
djy_init = 3

mx = mx_init
my = my_init
dmx = dmx_init
dmy = dmy_init
cx = cx_init
cy = cy_init
jx = jx_init
jy = jy_init
djx = djx_init
djy = djy_init

create_man(mx, my, dmx, dmy)
create_jul(cx, cy, jx, jy, djx, djy)

x0, y0, x1, y1 = 0, 0, 0, 0

flag_man_upd = False
flag_jul_upd = False

tool = MOVE
color_pos = 0

while flag_running:
    time_delta = clock.tick(60)/1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag_running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x0, y0 = event.pos
        if event.type == pygame.MOUSEBUTTONUP:
            x1, y1 = event.pos
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == button_man_plus:
                    dmx, dmy = increase_sc(dmx, dmy)
                    flag_man_upd = True
                if event.ui_element == button_man_minus:
                    dmx, dmy = reduce_sc(dmx, dmy)
                    flag_man_upd = True
                if event.ui_element == button_man_julia_point:
                    tool = JULIA
                    pick_julia_tool()
                if event.ui_element == button_man_move:
                    tool = MOVE
                    pick_move_tool()
                if event.ui_element == button_man_home:
                    mx, my, dmx, dmy = mx_init, my_init, dmx_init, dmy_init
                    flag_man_upd = True
                if event.ui_element == button_jul_plus:
                    djx, djy = increase_sc(djx, djy)
                    flag_jul_upd = True
                if event.ui_element == button_jul_minus:
                    djx, djy = reduce_sc(djx, djy)
                    flag_jul_upd = True
                if event.ui_element == button_jul_home:
                    jx, jy, djx, djy = jx_init, jy_init, djx_init, djy_init
                    cx = cx_init
                    cy =  cy_init
                    flag_jul_upd = True
                if event.ui_element == button_pallete_change:
                    color_pos += 1
                    color_pos %= len(pallete)
                    calc.set_colors(*pallete[color_pos])
                    flag_man_upd = True
                    flag_jul_upd = True
        manager.process_events(event)

    manager.update(time_delta)

    if (tool == MOVE and (x0 != x1 or y0 != y1) and
            x1 >= offset_man[0] and x1 <= offset_man[0] + width and
            y1 >= offset_man[1] and y1 <= offset_man[1] + height and
            x0 >= offset_man[0] and x0 <= offset_man[0] + width and
            y0 >= offset_man[1]  and y0 <= offset_man[1] + height):
        flag_man_upd = True
        mx -= (x1 - x0)/width*dmx
        my -= (y1 - y0)/height*dmy
        x0, y0 = 0, 0
        x1, y1 = 0, 0

    if ((x0 != x1 or y0 != y1) and
            x1 >= offset_jul[0] and x1 <= offset_jul[0] + width and
            y1 >= offset_jul[1] and y1 <= offset_jul[1] + height and
            x0 >= offset_jul[0] and x0 <= offset_jul[0] + width and
            y0 >= offset_jul[1]  and y0 <= offset_jul[1] + height):
        flag_jul_upd = True
        jx -= (x1 - x0)/width*djx
        jy -= (y1 - y0)/height*djy
        x0, y0 = 0, 0
        x1, y1 = 0, 0

    if (tool == JULIA and
            x0 >= offset_man[0] and x0 <= offset_man[0] + width and
            y0 >= offset_man[1] and y0 <= offset_man[1] + width):
        flag_jul_upd = True
        cx = mx + ((x0 - offset_man[0])/width - 0.5)*dmx
        cy = my + ((y0 - offset_man[1])/width - 0.5)*dmy
        x0, y0 = 0, 0
        x1, y1 = 0, 0

    if (flag_man_upd):
        flag_man_upd = False
        create_man(mx, my, dmx, dmy)

    if (flag_jul_upd):
        flag_jul_upd = False
        create_jul(cx, cy, jx, jy, djx, djy)

    window_surface.blit(background, (0, 0))
    manager.draw_ui(window_surface)

    pygame.display.update()
