import pygame
import sys
import bg_menu
import threading
import time
import random
import math
ticker = pygame.time.Clock()
from pygame.locals import *
from pygame import mixer
import tilemap

# pygame.display.set_mode((infoObject.current_w, infoObject.current_h))

pygame.init()
mixer.init()
pygame.display.set_caption('CrazyExtremeFishing')
size = (900, 600)
font = pygame.font.Font("Minecraft.ttf", 50)
infoObject = pygame.display.Info()

ecran = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
mixer.music.load("Assets/Songs/littleidea.mp3")
button_sound = mixer.Sound("Assets/Songs/button_sound.wav")

volume = 0.2
mixer.music.set_volume(volume)
button_sound.set_volume(volume)
mixer.music.play(-1)
taille = pygame.font.SysFont(None, 60)
coeff_fps = 1
player_scale_x = 240
player_scale_y = 110
Player = [pygame.transform.scale(pygame.image.load(f"Assets/Character/Boat1_withFishingRod1.png").convert_alpha(),
                                 (player_scale_x, player_scale_y)),
          pygame.transform.scale(pygame.image.load("Assets/Character/Boat1_withFishingRod2.png").convert_alpha(),
                                 (player_scale_x, player_scale_y)),
          pygame.transform.scale(pygame.image.load("Assets/Character/Boat1_withFishingRod3.png").convert_alpha(),
                                 (player_scale_x, player_scale_y)),
          pygame.transform.scale(pygame.image.load("Assets/Character/Boat1_withFishingRod4.png").convert_alpha(),
                                 (player_scale_x, player_scale_y))]
Hook = pygame.image.load("Assets/Hook.png")
shop_cane = pygame.transform.scale(pygame.image.load("Assets/Start_Menu/cane1.png").convert_alpha(), (250, 250))
shop_cane_2 = pygame.transform.scale(pygame.image.load("Assets/Start_Menu/cane2.png").convert_alpha(), (250, 250))
shop_cane_3 = pygame.transform.scale(pygame.image.load("Assets/Start_Menu/cane3.png").convert_alpha(), (250, 250))
shop_cane_4 = pygame.transform.scale(pygame.image.load("Assets/Start_Menu/cane4.png").convert_alpha(), (250, 250))

black_square = pygame.transform.scale(pygame.image.load("Assets/Start_Menu/black square.png").convert_alpha(),
                                      (254, 254))
logo = pygame.transform.scale(pygame.image.load("Assets/Start_Menu/logo.png").convert_alpha(), (175, 65))
logo_pressed = pygame.transform.scale(pygame.image.load("Assets/Start_Menu/logo_pressed.png").convert_alpha(),
                                      (175, 65))
reduce_logo_plus = pygame.transform.scale(pygame.image.load("Assets/Start_Menu/reduce_logo_plus.png").convert_alpha(),
                                          (65, 65))
reduce_logo_plus_pressed = pygame.transform.scale(
    pygame.image.load("Assets/Start_Menu/reduce_logo_plus_pressed.png").convert_alpha(),
    (65, 65))
reduce_logo_minus = pygame.transform.scale(pygame.image.load("Assets/Start_Menu/reduce_logo_minus.png").convert_alpha(),
                                           (65, 65))
reduce_logo_minus_pressed = pygame.transform.scale(
    pygame.image.load("Assets/Start_Menu/reduce_logo_minus_pressed.png").convert_alpha(),
    (65, 65))
logo_pause = pygame.transform.scale(
    pygame.image.load("Assets/Start_Menu/logo_pause.png").convert_alpha(),
    (65, 65))
logo_pause_pressed = pygame.transform.scale(
    pygame.image.load("Assets/Start_Menu/logo_pause_pressed.png").convert_alpha(),
    (65, 65))
logo_interrogation_pressed = pygame.transform.scale(
    pygame.image.load("Assets/Start_Menu/logo_interrogation_pressed.png").convert_alpha(), (65, 65))
logo_interrogation = pygame.transform.scale(
    pygame.image.load("Assets/Start_Menu/logo_interrogation.png").convert_alpha(), (65, 65))

logo_dollar_pressed = pygame.transform.scale(
    pygame.image.load("Assets/Start_Menu/logo_dollar_pressed.png").convert_alpha(), (65, 65))
logo_dollar = pygame.transform.scale(pygame.image.load("Assets/Start_Menu/logo_dollar.png").convert_alpha(), (65, 65))

renard_loading = pygame.transform.scale(pygame.image.load("Assets/Start_Menu/Renard.png").convert_alpha(), (50, 41))
logo_game = pygame.image.load("Assets/Main/Logo_the fox fishing.png").convert_alpha()
cursor = pygame.transform.scale(pygame.image.load("Assets/Main/cursor.png").convert_alpha(), (50, 50))
BG_mainmenu = bg_menu.Background()


class Button:
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self, text):
        ecran.blit(self.image, (self.rect.x, self.rect.y))
        font = pygame.font.Font("Minecraft.ttf", 40)
        text_render = font.render(text, 1, (255, 255, 255))
        ecran.blit(text_render, (self.rect.x, self.rect.y + 15))

        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0]:
                self.clicked = True
                button_sound.play()
            else:
                if self.clicked:
                    self.clicked = False
            return self.clicked



class Fishs(pygame.sprite.Sprite):

    def __init__(self,x,y):
        super().__init__()
        self.images = [[pygame.transform.scale(pygame.image.load("Assets/Character/Fish1.1.png"),(36,20)),pygame.transform.scale(pygame.image.load("Assets/Character/Fish1.2.png"),(36,20))],[pygame.transform.scale(pygame.image.load("Assets/Character/Fish2.1.png"),(36,20)),pygame.transform.scale(pygame.image.load("Assets/Character/Fish2.2.png"),(36,20))],[pygame.transform.scale(pygame.image.load("Assets/Character/Fish3.1.png"),(40,24)),pygame.transform.scale(pygame.image.load("Assets/Character/Fish3.2.png"),(40,24))],[pygame.transform.scale(pygame.image.load("Assets/Character/Fish4.1.png"),(112,48)),pygame.transform.scale(pygame.image.load("Assets/Character/Fish4.2.png"),(112,48))]]
        self.choose = 0
        self.cc = 0
        self.x = x
        self.y = y
        self.velocity = random.randint(2,5)
        self.direction = random.randrange(-1,2,2)
        self.image = random.randint(0,3)
        self.bool = True
        self.hook = pygame.image.load("Assets/Hook.png")
        self.hookx = 0
        self.hooky = 0
        self.catched = []
        self.tosale =[]

    def spawn(self):
        if self.bool == True and self.direction == 1:
            ecran.blit(self.images[self.image][self.anim()],(self.x,self.y))
        elif self.bool == True and self.direction == -1:
            ecran.blit(pygame.transform.flip(self.images[self.image][self.anim()],True, False),(self.x, self.y))
        elif self.bool == False and self.direction == 1:
            ecran.blit(self.images[self.image][self.anim()], (self.x, self.y))
        elif self.bool == False and self.direction == -1:
            ecran.blit(pygame.transform.flip(self.images[self.image][self.anim()],True, False),(self.x, self.y))

    def move(self):
        if self not in self.catched and self not in self.tosale:
            self.x += self.velocity * self.direction

    def anim(self):
        self.cc += 0.2
        if self.cc > 1:
            self.choose += 1
            self.cc = 0

        if self.choose > 1:
            self.choose = 0
        return self.choose

    def catch(self,hookx,hooky,poisson):

        if self.x < hookx + 20 and self.x > hookx - 20 and self.y < hooky + 20 and self.y > hooky - 20  and poisson == False:

            self.catched.append(self)
            poisson = True
            print("Catch")
        self.stuckhook(hookx,hooky)
        return poisson

    def stuckhook(self,hookx,hooky):

        if self.catched !=[]:
            for e in self.catched:
                e.x = hookx
                e.y = hooky + 20
            print("Stuck in hook")

    def hookreturn(self,hookx,hooky,shoot,time,poisson,movex,movey):
        if poisson == True and self.catched !=[] and movex + 200 > hookx > movex - 20 and movey + 100 > hooky > movey -20:
            shoot = False
            time = False
            poisson = False
            hookx = movex + 151
            hooky = movey + 37
            print(self.catched)
            self.tosale.append(self.catched[0])
            self.catched.clear()
            print(self.catched)
            print(self.tosale)

            print("Hook return to boat")
        self.inboat(movex, movey)
        return hookx, hooky, poisson, shoot, time

    def inboat(self, movex,movey):
        if self.tosale:
            self.x = movex + 5
            self.y = movey + 37
            print("Fish in boat")



click = False


class Button_option:
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self, text):
        ecran.blit(self.image, (self.rect.x, self.rect.y))
        font = pygame.font.Font("Minecraft.ttf", 40)
        text_render = font.render(text, 1, (255, 255, 255))
        ecran.blit(text_render, (self.rect.x, self.rect.y + 15))

        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0]:
                self.clicked = True
                button_sound.play()
            else:
                if self.clicked:
                    self.clicked = False
                    return True


click = False

clock = pygame.time.Clock()


def main_menu(volume):
    global ran
    clac = 0
    width = 800
    i = 0
    j = 0
    k = 0
    count = 0
    nat_count = 0
    ran = True

    while ran:
        # update position

        ecran.fill((99, 155, 255))

        ecran.blit(BG_mainmenu.sky_bg, (i, 0))
        ecran.blit(BG_mainmenu.sky_bg, (width + i, 0))
        ecran.blit(BG_mainmenu.sky_bg, (width * 2 + i, 0))
        ecran.blit(BG_mainmenu.sky_bg, (width * 3 + i, 0))

        ecran.blit(BG_mainmenu.mountain_bg, (i, -100))
        ecran.blit(BG_mainmenu.mountain_bg, (width + i, -100))
        ecran.blit(BG_mainmenu.mountain_bg, (width * 2 + i, -100))
        ecran.blit(BG_mainmenu.mountain_bg, (width * 3 + i, -100))

        if i < -width:
            i = 0
        if j < -width:
            j = 0
        if k < -width:
            k = 0
        i -= 1
        j -= 10
        k -= 3
        ecran.blit(BG_mainmenu.forest_bg, (j, -90))
        ecran.blit(BG_mainmenu.forest_bg, (width + j, -90))
        ecran.blit(BG_mainmenu.forest_bg, (width * 2 + j, -90))
        ecran.blit(BG_mainmenu.forest_bg, (width * 3 + j, -90))
        ecran.blit(BG_mainmenu.forest_fg2, (k, 200))
        ecran.blit(BG_mainmenu.forest_fg2, (width + k, 200))
        ecran.blit(BG_mainmenu.forest_fg2, (width * 2 + k, 200))
        ecran.blit(BG_mainmenu.forest_fg2, (width * 3 + k, 200))
        ecran.blit(BG_mainmenu.forest_fg, (j, 280))
        ecran.blit(BG_mainmenu.forest_fg, (width + j, 280))
        ecran.blit(BG_mainmenu.forest_fg, (width * 2 + j, 280))
        ecran.blit(BG_mainmenu.forest_fg, (width * 3 + j, 280))
        ecran.blit(BG_mainmenu.nature_fg[nat_count], (j, 437))
        ecran.blit(BG_mainmenu.nature_fg[nat_count], (width / 10 + j, 437))
        ecran.blit(BG_mainmenu.nature_fg[nat_count], (width / 10 * 2 + j, 437))
        ecran.blit(BG_mainmenu.nature_fg[nat_count], (width / 10 * 3 + j, 437))
        ecran.blit(BG_mainmenu.nature_fg[nat_count], (width / 10 * 4 + j, 437))
        ecran.blit(BG_mainmenu.nature_fg[nat_count], (width / 10 * 5 + j, 437))
        ecran.blit(BG_mainmenu.nature_fg[nat_count], (width / 10 * 6 + j, 437))
        ecran.blit(BG_mainmenu.nature_fg[nat_count], (width / 10 * 7 + j, 437))
        ecran.blit(BG_mainmenu.nature_fg[nat_count], (width / 10 * 8 + j, 437))
        ecran.blit(BG_mainmenu.nature_fg[nat_count], (width / 10 * 9 + j, 437))
        ecran.blit(BG_mainmenu.nature_fg[nat_count], (width / 10 * 10 + j, 437))
        ecran.blit(BG_mainmenu.nature_fg[nat_count], (width / 10 * 11 + j, 437))
        ecran.blit(BG_mainmenu.nature_fg[nat_count], (width / 10 * 12 + j, 437))
        ecran.blit(BG_mainmenu.nature_fg[nat_count], (width / 10 * 13 + j, 437))
        ecran.blit(BG_mainmenu.nature_fg[nat_count], (width / 10 * 14 + j, 437))
        ecran.blit(BG_mainmenu.nature_fg[nat_count], (width / 10 * 15 + j, 437))
        ecran.blit(BG_mainmenu.nature_fg[nat_count], (width / 10 * 16 + j, 437))
        ecran.blit(BG_mainmenu.nature_fg[nat_count], (width / 10 * 17 + j, 437))
        ecran.blit(BG_mainmenu.nature_fg[nat_count], (width / 10 * 18 + j, 437))
        ecran.blit(BG_mainmenu.nature_fg[nat_count], (width / 10 * 19 + j, 437))
        ecran.blit(BG_mainmenu.nature_fg[nat_count], (width / 10 * 20 + j, 437))
        ecran.blit(BG_mainmenu.nature_fg[nat_count], (width / 10 * 21 + j, 437))
        ecran.blit(BG_mainmenu.nature_fg[nat_count], (width / 10 * 22 + j, 437))
        ecran.blit(BG_mainmenu.nature_fg[nat_count], (width / 10 * 23 + j, 437))
        ecran.blit(BG_mainmenu.nature_fg[nat_count], (width / 10 * 24 + j, 437))
        ecran.blit(BG_mainmenu.nature_fg[nat_count], (width / 10 * 25 + j, 437))
        ecran.blit(BG_mainmenu.nature_fg[nat_count], (width / 10 * 26 + j, 437))
        ecran.blit(BG_mainmenu.nature_fg[nat_count], (width / 10 * 27 + j, 437))
        ecran.blit(BG_mainmenu.nature_fg[nat_count], (width / 10 * 28 + j, 437))
        ecran.blit(BG_mainmenu.nature_fg[nat_count], (width / 10 * 29 + j, 437))
        ecran.blit(BG_mainmenu.nature_fg[nat_count], (width / 10 * 30 + j, 437))
        ecran.blit(BG_mainmenu.nature_fg[nat_count], (width / 10 * 31 + j, 437))
        ecran.blit(BG_mainmenu.nature_fg[nat_count], (width / 10 * 32 + j, 437))
        ecran.blit(BG_mainmenu.nature_fg[nat_count], (width / 10 * 33 + j, 437))
        ecran.blit(BG_mainmenu.nature_fg[nat_count], (width / 10 * 34 + j, 437))
        ecran.blit(font.render("IPS :" + str(int(clock.get_fps()) * coeff_fps), 1, (1, 1, 1)),
                   (infoObject.current_w * 1 - 200, infoObject.current_h * (1 / 54)))

        if count > 11:
            count = 0
        if nat_count > 7:
            nat_count = 0
        nat_count += 1
        ecran.blit(BG_mainmenu.boat[count], (150, 600))
        count += 1

        play_button = Button(infoObject.current_w * (2 / 6), infoObject.current_h * (43 / 54), logo)
        options_button = Button(infoObject.current_w * (3 / 6), infoObject.current_h * (43 / 54), logo)
        quit_button = Button(infoObject.current_w * (4 / 6), infoObject.current_h * (43 / 54), logo)
        play_button_pressed = Button(infoObject.current_w * (2 / 6), infoObject.current_h * (43 / 54), logo_pressed)
        options_button_pressed = Button(infoObject.current_w * (3 / 6), infoObject.current_h * (43 / 54), logo_pressed)
        quit_button_pressed = Button(infoObject.current_w * (4 / 6), infoObject.current_h * (43 / 54), logo_pressed)

        if play_button.draw("   Play"):
            play_button_pressed.draw("   Play")
            ran = False

            loading(volume)

        if options_button.draw(" Options"):
            options_button_pressed.draw(" Options")
            volume2 = options(volume)
            volume = volume2

        if quit_button.draw("   Quit"):
            quit_button_pressed.draw("   Quit")
            sys.exit()

        ecran.blit(logo_game, (infoObject.current_w * (2 / 5), infoObject.current_h * (2.5 / 4)))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        pygame.display.update()
        ticker.tick(20)
        clock.tick()
        print(clock.get_fps())


def options(volume):
    global coeff_fps
    running = True
    volume *= 100
    ecran.fill((255, 125, 0))
    text = font.render("Options", 1, (255, 255, 255))
    textRect = text.get_rect()
    textRect.center = (infoObject.current_w // 2, infoObject.current_h * (1 / 10))

    ecran.blit(text, textRect)
    ecran.blit(font.render(str(int(volume)), 1, (255, 255, 255)),
               (infoObject.current_w * (86 / 240), infoObject.current_h * (16 / 54)))
    ecran.blit(font.render("Musique", 1, (255, 255, 255)),
               (infoObject.current_w * (2 / 24), infoObject.current_h * (16 / 54)))
    ecran.blit(font.render("Rafraichissement", 1, (255, 255, 255)),
               (infoObject.current_w * (2 / 24), infoObject.current_h * (22.5 / 54)))


    play_button1 = Button(infoObject.current_w * (1 / 2) - 87.5, infoObject.current_h * (49 / 54), logo)
    play_button1_pressed = Button(infoObject.current_w * (1 / 2) - 87.5, infoObject.current_h * (49 / 54), logo_pressed)

    sound_plus_button = Button_option(infoObject.current_w * (100 / 240), infoObject.current_h * (15 / 54),
                                      reduce_logo_plus)
    sound_plus_button_pressed = Button_option(infoObject.current_w * (100 / 240), infoObject.current_h * (15 / 54),
                                              reduce_logo_plus_pressed)
    sound_minus_button = Button_option(infoObject.current_w * (70 / 240), infoObject.current_h * (15 / 54),
                                       reduce_logo_minus)
    sound_minus_button_pressed = Button_option(infoObject.current_w * (70 / 240), infoObject.current_h * (15 / 54),
                                               reduce_logo_minus_pressed)

    FPS = Button(infoObject.current_w * (1 / 2.8) - 73, infoObject.current_h * (22 / 54), logo)
    FPS_pressed = Button(infoObject.current_w * (1 / 2.8) - 73, infoObject.current_h * (22 / 54), logo_pressed)
    FPS2 = Button(infoObject.current_w * (1 / 2.1) - 73, infoObject.current_h * (22 / 54), logo)
    FPS_pressed2 = Button(infoObject.current_w * (1 / 2.1) - 73, infoObject.current_h * (22 / 54), logo_pressed)

    while running:

        if sound_plus_button.draw(""):
            sound_plus_button_pressed.draw("")
            if volume < 100:
                volume += 1
                mixer.music.set_volume(volume / 100)
                button_sound.set_volume(volume / 100)
                pygame.draw.rect(ecran, (255, 125, 0),
                                 pygame.Rect(infoObject.current_w * (86 / 240), infoObject.current_h * (16 / 54), 75,
                                             70))
                ecran.blit(font.render(str(int(volume)), 1, (255, 255, 255)),
                           (infoObject.current_w * (86 / 240), infoObject.current_h * (16 / 54)))

        if sound_minus_button.draw(""):
            sound_minus_button_pressed.draw("")
            if volume > 0:
                volume -= 1
                mixer.music.set_volume(volume / 100)
                button_sound.set_volume(volume / 100)
                pygame.draw.rect(ecran, (255, 125, 0),
                                 pygame.Rect(infoObject.current_w * (86 / 240), infoObject.current_h * (16 / 54), 75,
                                             70))
                ecran.blit(font.render(str(int(volume)), 1, (255, 255, 255)),
                           (infoObject.current_w * (86 / 240), infoObject.current_h * (16 / 54)))

        if play_button1.draw("  Quitter"):
            play_button1_pressed.draw("  Quitter")
            running = False

        if FPS.draw("     60"):
            coeff_fps = 3
            FPS_pressed.draw("     60")
        if FPS2.draw("    120"):
            coeff_fps = 6
            FPS_pressed2.draw("    120")

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()
        ticker.tick(20)
    volume /= 100
    return volume


def game(volume):
    background = pygame.image.load("Assets/Map/map ile paradisiaque.png").convert_alpha()
    background = pygame.transform.scale(background, (infoObject.current_w, infoObject.current_h))
    anim = 0
    p_count = 0
    f_count = 0
    movex = 10
    movey = 310
    flip = 0
    moving_right = False
    moving_left = False
    echap = False
    magasin = False
    aides = False
    run = True
    score = 10000
    argent = 1000
    prix_canne_1, prix_canne_2, prix_canne_3, prix_canne_4 = 100, 250, 500, 1000
    cane_buy_1, cane_buy_2, cane_buy_3, cane_buy_4 = False, False, False, False
    Hook = pygame.image.load("Assets/Hook.png")
    Hookx = movex + 151
    Hooky = movey + 37
    time = 0
    shoot = False
    power = 0
    angle = 0
    poissonattrape = False
    fishattrape1 = True
    fishok = False

    def playy(flip, right, left):
        if right == False and left == False and flip == 0:
            ecran.blit(Player[p_count], (movex, movey))
        elif right == True and left == False and flip == 0:
            ecran.blit(Player[p_count], (movex, movey))
        elif right == False and left == True and flip == 1:
            ecran.blit(pygame.transform.flip(Player[p_count], True, False), (movex, movey))
        elif right == False and left == False and flip == 1:
            ecran.blit(pygame.transform.flip(Player[p_count], True, False), (movex, movey))
    def findAngle(pos):
        sX = Hookx
        sY = Hooky
        try:
            angle = math.atan((sY - pos[1]) / (sX - pos[0]))
        except:
            angle = math.pi / 2

        if pos[1] < sY and pos[0] > sX:
            angle = abs(angle)
        elif pos[1] < sY and pos[0] < sX:
            angle = math.pi - angle
        elif pos[1] > sY and pos[0] < sX:
            angle = math.pi + abs(angle)
        elif pos[1] > sY and pos[0] > sX:
            angle = (math.pi * 2) - angle

        return angle

    def ballPath(startx, starty, power, ang, time):
        angle = ang
        velx = math.cos(angle) * power
        vely = math.sin(angle) * power

        distX = velx * time
        distY = (vely * time) + ((-4.9 * (time ** 2)) / 2)

        newx = round(distX + startx)
        newy = round(starty - distY)

        return (newx, newy)

    def catchfish(poissonattrape):

        if poissonattrape:
            e.x = Hookx - 25
            e.y = Hooky + 25

            return e.x, e.y

    def hookreturn():
        Hookx = movex + 151
        Hooky = movey + 37
        shoot = False
        time = False

        return Hookx, Hooky, shoot, time


    enemies =[]

    for i in range(20):
        enemies.append(Fishs(random.randint(100,infoObject.current_w-25),random.randint(500,infoObject.current_h-100)))
    while run:
        ecran.blit(background, (0, 0))
        """if (movex - 40 < e.x < movex + 40) and (movey - 40 < e.y < movey + 40):
            print(poissonattrape)
            e.x = movex + 25
            e.y = movey + 40
            fishattrape1 = False
            Hookx, Hooky, shoot, time = hookreturn()"""

        line = [(Hookx, Hooky), (movex + 160, movey + 40)]
        pygame.draw.line(ecran, (255, 255, 255), line[0], line[1], 3)
        playy(flip, False, False)
        for e in enemies:
            e.move()
            e.spawn()
            if e.x > infoObject.current_w - 15 or e.x < -100:
                e.direction *= -1
                e.y += random.randrange(-60, 60, 10)
                e.bool = not e.bool


            if e.y > infoObject.current_h:

                e.y -= 100
            elif e.y < 410:
                e.y += 100

            poissonattrape = e.catch(Hookx,Hooky,poissonattrape)
            Hookx,Hooky,poissonattrape,shoot,time = e.hookreturn(Hookx,Hooky,shoot,time,poissonattrape,movex,movey)



            """print("POISSON")
                poissonattrape = True  # le poisson est attrapé
                e.x, e.y = catchfish(poissonattrape)"""

        f_count += 0.2
        if f_count > 1:
            p_count += 1
            f_count = 0
            anim += 1
        if p_count > 3:
            p_count = 0
        if anim > 1:
            anim = 0
        ecran.blit(Hook, (Hookx, Hooky))

        if shoot:
            if Hooky < infoObject.current_h - 50:

                time += 0.1
                po = ballPath(x, y, power, angle, time)
                Hookx = po[0]
                Hooky = po[1]
            else:
                shoot = False
                time = False
                Hooky = Hooky - 5


        scoreText = font.render(str(score) + " pts ", True, (255, 255, 255))
        scrRect = scoreText.get_rect()
        scrRect.center = (infoObject.current_w * 1 - 105, infoObject.current_h * (1.6 / 54))
        ecran.blit(scoreText, scrRect)

        argentText = font.render(str(argent) + " $ ", True, (255, 255, 255))
        argentRect = argentText.get_rect()
        argentRect.center = (infoObject.current_w * 1 - 80, infoObject.current_h * (4.5 / 54))
        ecran.blit(argentText, argentRect)

        pause = Button(infoObject.current_w * (0.1 / 15), infoObject.current_h * (0.1 / 10), logo_pause)
        pause_pressed = Button(infoObject.current_w * (0.1 / 15), infoObject.current_h * (0.1 / 10), logo_pause_pressed)

        shop = Button(infoObject.current_w * (0.7 / 15), infoObject.current_h * (0.1 / 10), logo_dollar)
        shop_pressed = Button(infoObject.current_w * (0.7 / 15), infoObject.current_h * (0.1 / 10), logo_dollar_pressed)

        helps = Button(infoObject.current_w * (1.3 / 15), infoObject.current_h * (0.1 / 10), logo_interrogation)
        helps_pressed = Button(infoObject.current_w * (1.3 / 15), infoObject.current_h * (0.1 / 10),
                               logo_interrogation_pressed)

        if pause.draw(""):
            pause_pressed.draw("")
            echap = True
        if shop.draw(""):
            shop_pressed.draw("")
            magasin = True
        if helps.draw(""):
            helps_pressed.draw("")
            aides = True


        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    flip = 0
                    moving_right = True
                elif event.key == pygame.K_LEFT:
                    flip = 1
                    moving_left = True
                elif event.key == K_ESCAPE:
                    if echap:
                        echap = False
                    else:
                        if magasin:
                            magasin = False
                        else:
                            echap = True
                elif event.key == K_m:
                    if magasin:
                        magasin = False
                    else:
                        if echap:
                            magasin = False
                        else:
                            magasin = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if not shoot :
                    shoot = True
                    x = Hookx
                    y = Hooky
                    pos = pygame.mouse.get_pos()
                    power = math.sqrt((line[1][1] - line[0][1]) ** 2 + (line[1][0] - line[0][1]) ** 2) / 8
                    angle = findAngle(pos)


            elif event.type == KEYUP:
                moving_right = False
                moving_left = False

        if moving_right:
            playy(flip, True, False)
            movex += 5
            Hookx += 5
        if moving_left:
            playy(flip, False, True)
            movex -= 5
            Hookx -= 5

        if movex < 10:
            movex = 10
        elif movex > infoObject.current_w - 220:
            movex = infoObject.current_w - 220

        if Hookx < 10:
            Hookx = 10
        elif Hookx > infoObject.current_w - 10:
            Hookx = infoObject.current_w - 10

        if echap:
            draw_rect_alpha(ecran, (50, 50, 50, 180), (0, 0, infoObject.current_w, infoObject.current_h))
            draw_rect_alpha(ecran, (180, 100, 0, 255), (0, 0, infoObject.current_w // 3, infoObject.current_h))
            draw_rect_alpha(ecran, (230, 125, 0, 200),
                            (5, 5, infoObject.current_w // 3 - 10, infoObject.current_h - 10))

            text = font.render("Menu", 1, (255, 255, 255))
            textRect = text.get_rect()
            textRect.center = (infoObject.current_w // 6, infoObject.current_h * (1 / 10))
            ecran.blit(text, textRect)

            resume_button = Button(infoObject.current_w // 8, infoObject.current_h * (3 / 10), logo)
            options_button = Button(infoObject.current_w // 8, infoObject.current_h * (5 / 10), logo)
            quit_button = Button(infoObject.current_w // 8, infoObject.current_h * (7.5 / 10), logo)

            resume_button_pressed = Button(infoObject.current_w // 8, infoObject.current_h * (3 / 10), logo_pressed)
            options_button_pressed = Button(infoObject.current_w // 8, infoObject.current_h * (5 / 10), logo_pressed)
            quit_button_pressed = Button(infoObject.current_w // 8, infoObject.current_h * (7.5 / 10), logo_pressed)

            if resume_button.draw("Continuer"):
                resume_button_pressed.draw("Continuer")
                echap = False

            if options_button.draw(" Options"):
                options_button_pressed.draw(" Options")
                volume2 = options(volume)
                volume = volume2

            if quit_button.draw(" Quitter"):
                quit_button_pressed.draw(" Quitter")
                sys.exit()
        if magasin:
            draw_rect_alpha(ecran, (50, 50, 50, 180), (0, 0, infoObject.current_w, infoObject.current_h))
            draw_rect_alpha(ecran, (180, 100, 0, 255),
                            (infoObject.current_w * (3 / 53) - 10, infoObject.current_h * (3 / 53) - 10,
                             infoObject.current_w - infoObject.current_w * (6 / 53) + 20,
                             infoObject.current_h - infoObject.current_h * (6 / 53) + 20))
            draw_rect_alpha(ecran, (230, 125, 0, 200),
                            (infoObject.current_w * (3 / 53), infoObject.current_h * (3 / 53),
                             infoObject.current_w - infoObject.current_w * (6 / 53),
                             infoObject.current_h - infoObject.current_h * (6 / 53)))

            quit_button = Button(infoObject.current_w * (42 / 53), infoObject.current_h * (43 / 53), logo)
            quit_button_pressed = Button(infoObject.current_w * (42 / 53), infoObject.current_h * (43 / 53),
                                         logo_pressed)

            if quit_button.draw("  Sortir"):
                quit_button_pressed.draw("  Sortir")
                magasin = False

            caneText = font.render("Canne a Peche", 1, (255, 255, 255))
            caneRect = caneText.get_rect()
            caneRect.center = (infoObject.current_w // 5, infoObject.current_h * (7 / 53))
            ecran.blit(caneText, caneRect)

            cane1 = Button(infoObject.current_w * (8 / 50), infoObject.current_h * (10 / 50), shop_cane)
            cane2 = Button(infoObject.current_w * (16 / 50), infoObject.current_h * (10 / 50), shop_cane_2)
            cane3 = Button(infoObject.current_w * (24 / 50), infoObject.current_h * (10 / 50), shop_cane_3)
            cane4 = Button(infoObject.current_w * (32 / 50), infoObject.current_h * (10 / 50), shop_cane_4)

            bs1 = Button(infoObject.current_w * (8 / 50) - 2, infoObject.current_h * (10 / 50) - 2, black_square)
            bs1.draw("")
            prix1Text = font.render(str(prix_canne_1) + "$", True, (255, 255, 255))
            prix1Rect = prix1Text.get_rect()
            prix1Rect.center = (infoObject.current_w * (8 / 50) + 125, infoObject.current_h * (10 / 50) + 280)
            ecran.blit(prix1Text, prix1Rect)

            bs2 = Button(infoObject.current_w * (16 / 50) - 2, infoObject.current_h * (10 / 50) - 2, black_square)
            bs2.draw("")
            prix2Text = font.render(str(prix_canne_2) + "$", True, (255, 255, 255))
            prix2Rect = prix2Text.get_rect()
            prix2Rect.center = (infoObject.current_w * (16 / 50) + 125, infoObject.current_h * (10 / 50) + 280)
            ecran.blit(prix2Text, prix2Rect)

            bs3 = Button(infoObject.current_w * (24 / 50) - 2, infoObject.current_h * (10 / 50) - 2, black_square)
            bs3.draw("")
            prix3Text = font.render(str(prix_canne_3) + "$", True, (255, 255, 255))
            prix3Rect = prix3Text.get_rect()
            prix3Rect.center = (infoObject.current_w * (24 / 50) + 125, infoObject.current_h * (10 / 50) + 280)
            ecran.blit(prix3Text, prix3Rect)

            bs4 = Button(infoObject.current_w * (32 / 50) - 2, infoObject.current_h * (10 / 50) - 2, black_square)
            bs4.draw("")
            prix4Text = font.render(str(prix_canne_4) + "$", True, (255, 255, 255))
            prix4Rect = prix4Text.get_rect()
            prix4Rect.center = (infoObject.current_w * (32 / 50) + 125, infoObject.current_h * (10 / 50) + 280)
            ecran.blit(prix4Text, prix4Rect)

            if cane1.draw(""):
                if argent >= 100 and not cane_buy_1:
                    argent -= 100
                    cane_buy_1 = True
                    print("1 canne")
            if cane2.draw("") and not cane_buy_2:
                if argent >= 250:
                    argent -= 250
                    cane_buy_2 = True
                    print("2 canne")
            if cane3.draw("") and not cane_buy_3:
                if argent >= 500:
                    argent -= 500
                    cane_buy_3 = True
                    print("3 canne")
            if cane4.draw("") and not cane_buy_4:
                if argent >= 1000:
                    argent -= 1000
                    cane_buy_4 = True
                    print("4 canne")

            text = font.render("Magasin", 1, (255, 255, 255))
            textRect = text.get_rect()
            textRect.center = (infoObject.current_w // 2, infoObject.current_h * (3 / 53))
            ecran.blit(text, textRect)

            argentText = font.render(str(argent) + " $", True, (255, 255, 255))
            argentRect = argentText.get_rect()
            argentRect.center = (
                infoObject.current_w - infoObject.current_w * (6 / 53) - 25, infoObject.current_h * (5 / 53))
            ecran.blit(argentText, argentRect)

        if aides:
            draw_rect_alpha(ecran, (50, 50, 50, 180), (0, 0, infoObject.current_w, infoObject.current_h))
            draw_rect_alpha(ecran, (180, 100, 0, 255),
                            (infoObject.current_w * (3 / 53) - 10, infoObject.current_h * (3 / 53) - 10,
                             infoObject.current_w - infoObject.current_w * (6 / 53) + 20,
                             infoObject.current_h - infoObject.current_h * (6 / 53) + 20))
            draw_rect_alpha(ecran, (230, 125, 0, 200),
                            (infoObject.current_w * (3 / 53), infoObject.current_h * (3 / 53),
                             infoObject.current_w - infoObject.current_w * (6 / 53),
                             infoObject.current_h - infoObject.current_h * (6 / 53)))

            quit_button = Button(infoObject.current_w * (42 / 53), infoObject.current_h * (43 / 53), logo)
            quit_button_pressed = Button(infoObject.current_w * (42 / 53), infoObject.current_h * (43 / 53),
                                         logo_pressed)

            if quit_button.draw("  Sortir"):
                quit_button_pressed.draw("  Sortir")
                aides = False

            text = font.render("AIDE", 1, (255, 255, 255))
            textRect = text.get_rect()
            textRect.center = (infoObject.current_w // 2, infoObject.current_h * (3 / 53))
            ecran.blit(text, textRect)

            text = font.render("Pechez des poissons pour obtenir de l'argent !!!", 1, (255, 255, 255))
            textRect = text.get_rect()
            textRect.center = (infoObject.current_w // 2, infoObject.current_h * (6 / 53))
            ecran.blit(text, textRect)

        clock.tick(60)
        pygame.display.update()


def draw_rect_alpha(surface, color, rect):
    shape_surf = pygame.Surface(pygame.Rect(rect).size, pygame.SRCALPHA)
    pygame.draw.rect(shape_surf, color, shape_surf.get_rect())
    surface.blit(shape_surf, rect)


def loading(volume):
    running = True
    angle = 0
    count = 0
    clock = 0
    important = 0
    mixer.music.set_volume(0)
    while running:
        ecran.fill((0, 0, 0))
        angle += 1
        clock += 0.05
        important += 0.05
        if clock > 1:
            count += 1
            clock = 0
        msg_loading = ["Loading", "Loading.", "Loading..", "Loading..."]
        rota_rena = pygame.transform.rotate(renard_loading, angle)
        new_rect = rota_rena.get_rect(center=renard_loading.get_rect(
            topleft=(infoObject.current_w * (8 / 9) + 50, infoObject.current_h * (8 / 9))).center)
        ecran.blit(rota_rena, new_rect)
        font = pygame.font.Font("Minecraft.ttf", 25)
        if count > len(msg_loading) - 1:
            count = 0
        text = font.render(msg_loading[count], 1, (255, 255, 255))

        ecran.blit(text, (infoObject.current_w * (8 / 9) + 25, infoObject.current_h * (8 / 9) + 50))

        pygame.display.update()
        ticker.tick(60)
        if important > 5:
            running = False
            mixer.music.set_volume(volume)
            mixer.music.play(-1)
            game(volume)


game(volume)
