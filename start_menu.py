import pygame
import sys
import bg_menu
import threading
import time

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
menu_sound = mixer.music.load("Assets/Songs/littleidea.mp3")
button_sound = mixer.Sound("Assets/Songs/button_sound.wav")

sound = 0.2
mixer.music.set_volume(sound)
button_sound.set_volume(sound)
mixer.music.play(-1)
taille = pygame.font.SysFont(None, 60)
coeff_fps = 1
player_scale_x = 240
player_scale_y = 110
Player = [pygame.transform.scale(pygame.image.load(f"Assets/Character/Boat1_withFishingRod1.png").convert_alpha(),(player_scale_x,player_scale_y)),pygame.transform.scale(pygame.image.load("Assets/Character/Boat1_withFishingRod2.png").convert_alpha(),(player_scale_x,player_scale_y)),pygame.transform.scale(pygame.image.load("Assets/Character/Boat1_withFishingRod3.png").convert_alpha(),(player_scale_x,player_scale_y)),pygame.transform.scale(pygame.image.load("Assets/Character/Boat1_withFishingRod4.png").convert_alpha(),(player_scale_x,player_scale_y))]

logo = pygame.transform.scale(pygame.image.load("Assets/Start_Menu/logo.png").convert_alpha(), (175, 65))
logo_pressed = pygame.transform.scale(pygame.image.load("Assets/Start_Menu/logo_pressed.png").convert_alpha(), (175, 65))
reduce_logo_plus = pygame.transform.scale(pygame.image.load("Assets/Start_Menu/reduce_logo_plus.png").convert_alpha(), (65, 65))
reduce_logo_plus_pressed = pygame.transform.scale(pygame.image.load("Assets/Start_Menu/reduce_logo_plus_pressed.png").convert_alpha(),
                                                  (65, 65))
reduce_logo_minus = pygame.transform.scale(pygame.image.load("Assets/Start_Menu/reduce_logo_minus.png").convert_alpha(), (65, 65))
reduce_logo_minus_pressed = pygame.transform.scale(pygame.image.load("Assets/Start_Menu/reduce_logo_minus_pressed.png").convert_alpha(),
                                                   (65, 65))
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
                print("test")
            else:
                self.clicked=False
        return self.clicked





click = False


def loading():
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
        if important > 20:
            running=False
            game()


clock = pygame.time.Clock()





def main_menu():
    global ran
    clac = 0
    width = 800
    i = 0
    j = 0
    k = 0
    count = 0
    nat_count = 0
    ran = True

    while ran==True:
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
        ecran.blit(font.render("IPS :" + str(int(clock.get_fps())*coeff_fps), 1, (1, 1, 1)), (infoObject.current_w * 1 - 200, infoObject.current_h * (1 / 54)))

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

            loading()

        if options_button.draw(" Options"):
            options_button_pressed.draw(" Options")
            options(sound)

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
    while running:

        ecran.fill((255, 125, 0))
        text = font.render("Options", 1, (255, 255, 255))
        textRect = text.get_rect()
        textRect.center = (infoObject.current_w // 2, infoObject.current_h * (1 / 10))

        ecran.blit(text, textRect)
        ecran.blit(font.render(str(int(volume)), 1, (255, 255, 255)), (infoObject.current_w * (86 / 240), infoObject.current_h * (16 / 54)))
        ecran.blit(font.render("musique", 1, (255, 255, 255)), (infoObject.current_w * (2 / 24), infoObject.current_h * (16 / 54)))
        ecran.blit(font.render("IPS :" + str(int(clock.get_fps())*coeff_fps), 1, (1, 1, 1)),(infoObject.current_w * 1 - 200, infoObject.current_h * (1 / 54)))

        play_button1 = Button(infoObject.current_w * (1 / 2) - 87.5, infoObject.current_h * (49 / 54), logo)
        play_button1_pressed = Button(infoObject.current_w * (1 / 2) - 87.5, infoObject.current_h * (49 / 54),
                                      logo_pressed)

        sound_plus_button = Button(infoObject.current_w * (100 / 240), infoObject.current_h * (15 / 54),
                                   reduce_logo_plus)
        sound_plus_button_pressed = Button(infoObject.current_w * (100 / 240), infoObject.current_h * (15 / 54),
                                           reduce_logo_plus_pressed)
        sound_minus_button = Button(infoObject.current_w * (70 / 240), infoObject.current_h * (15 / 54),
                                    reduce_logo_minus)
        sound_minus_button_pressed = Button(infoObject.current_w * (70 / 240), infoObject.current_h * (15 / 54),
                                            reduce_logo_minus_pressed)

        FPS = Button(infoObject.current_w * (1 / 2.5) - 87.5, infoObject.current_h * (22 / 54), logo)
        FPS_pressed = Button(infoObject.current_w * (1 / 2.5) - 87.5, infoObject.current_h * (22 / 54), logo_pressed)
        FPS2 = Button(infoObject.current_w * (1 / 1.8) - 87.5, infoObject.current_h * (22 / 54), logo)
        FPS_pressed2 = Button(infoObject.current_w * (1 / 1.8) - 87.5, infoObject.current_h * (22 / 54), logo_pressed)

        if sound_plus_button.draw(""):
            if volume < 100:
                volume += 1
                mixer.music.set_volume(volume/100)
                button_sound.set_volume(volume/100)
                sound_plus_button_pressed.draw("")
        if sound_minus_button.draw(""):
            if volume > 0:
                volume -= 1
            mixer.music.set_volume(volume/100)
            button_sound.set_volume(volume/100)
            sound_minus_button_pressed.draw("")

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

def game():
    background=pygame.image.load("Assets/Map/map ile paradisiaque.png").convert_alpha()
    background = pygame.transform.scale(background,(infoObject.current_w,infoObject.current_h))
    p_count = 0
    f_count = 0
    movex = 10
    movey = 310
    flip = 0
    moving_right = False
    moving_left = False
    def playy(flip,right,left):
        if right==False and left == False and flip == 0:
            ecran.blit(Player[p_count], (movex, movey))
        elif right == True and left == False and flip == 0:
            ecran.blit(Player[p_count], (movex, movey))
        elif right == False and left == True and flip == 1 :
            ecran.blit(pygame.transform.flip(Player[p_count], True, False), (movex, movey))
        elif right == False and left == False and flip == 1:
            ecran.blit(pygame.transform.flip(Player[p_count], True, False), (movex, movey))

    while True:


        f_count +=0.2
        if f_count > 1:
            p_count += 1
            f_count = 0
        if p_count > 3:
            p_count = 0
        ecran.blit(background,(0,0))
        playy(flip, False, False)
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

            elif event.type == KEYUP:
                moving_right = False
                moving_left = False

        if moving_right == True:
            playy(flip,True, False)
            movex += 5
        if moving_left == True:
            playy(flip, False, True)
            movex -= 5

        clock.tick(60)
        pygame.display.update()

main_menu()
