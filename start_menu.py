import pygame, sys
import bg_menu
import threading
import time
ticker = pygame.time.Clock()
from pygame.locals import *
from pygame import mixer


#pygame.display.set_mode((infoObject.current_w, infoObject.current_h))

pygame.init()
mixer.init()
pygame.display.set_caption('CrazyExtremeFishing')
size = (900,600)
infoObject = pygame.display.Info()

ecran = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
menu_sound = mixer.music.load("littleidea.mp3")
button_sound = mixer.Sound("button_sound.wav")
mixer.music.set_volume(0.7)
mixer.music.play(-1)
taille = pygame.font.SysFont(None, 60)
BG = pygame.image.load("Assets/Background.jpg")
BG = pygame.transform.scale(BG, (1920,1080))
play_logo = pygame.transform.scale(pygame.image.load("Assets/logo.png"),((175*infoObject.current_w)/infoObject.current_w,65))
options_logo = pygame.transform.scale(pygame.image.load("Assets/logo.png"),(175,65))
quit_logo = pygame.transform.scale(pygame.image.load("Assets/logo.png"),(175,65))
play_logo_pressed = pygame.transform.scale(pygame.image.load("Assets/logo_pressed.png"),(175,65))
options_logo_pressed = pygame.transform.scale(pygame.image.load("Assets/logo_pressed.png"),(175,65))
quit_logo_pressed = pygame.transform.scale(pygame.image.load("Assets/logo_pressed.png"),(175,65))
renard_loading = pygame.transform.scale(pygame.image.load("Assets/Renard.png"),(50,41))
logo_game = pygame.image.load("Logo_the fox fishing.png")

background = bg_menu.Background()

'''def draw_text(texte, taille, couleur, surface, x, y):
    textobj = taille.render(texte, 1, couleur)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


def button(screen, position, text, image):
    font = pygame.font.SysFont("Arial", 50)
    text_render = font.render(text, 1, (255, 255, 255))
    x, y, w, h = text_render.get_rect()

    x, y = position
    pygame.draw.line(screen, (150, 150, 150), (x, y), (x + w, y), 5)
    pygame.draw.line(screen, (150, 150, 150), (x, y - 2), (x, y + h), 5)
    pygame.draw.line(screen, (50, 50, 50), (x, y + h), (x + w, y + h), 5)
    pygame.draw.line(screen, (50, 50, 50), (x + w, y + h), [x + w, y], 5)
    pygame.draw.rect(screen, (100, 100, 100), (x, y, w, h)
    return screen.blit(text_render, (x, y))
    return screen.blit(image,(x,y))


def button_press(screen, position, text,image):
    font = pygame.font.SysFont("Arial", 50)
    text_render = font.render(text, 1, (200, 200, 200))
    x, y, w, h = text_render.get_rect()
    x, y = position
    pygame.draw.line(screen, (150, 150, 150), (x, y), (x + w, y), 5)
    pygame.draw.line(screen, (150, 150, 150), (x, y - 2), (x, y + h), 5)
    pygame.draw.line(screen, (50, 50, 50), (x, y + h), (x + w, y + h), 5)
    pygame.draw.line(screen, (50, 50, 50), (x + w, y + h), [x + w, y], 5)
    pygame.draw.rect(screen, (100, 100, 100), (x, y, w, h))
    return screen.blit(image, (x, y))


def button_maker(x, y, longueur, largeur, couleur):
    bouton = pygame.Rect(x, y, longueur, largeur)
    pygame.draw.rect(ecran, couleur, bouton)
    return bouton'''

class Button():
    def __init__(self,x,y,image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False

    def draw(self,text):
        ecran.blit(self.image, (self.rect.x,self.rect.y))
        font = pygame.font.Font("Minecraft.ttf", 40)
        text_render = font.render(text, 1, (255, 255, 255))
        ecran.blit(text_render,(self.rect.x,self.rect.y+15))


        action = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0]==1 and self.clicked == False:
                self.clicked = True
                action = True
                button_sound.play()
            if pygame.mouse.get_pressed()[0]==0:
                self.clicked = False
                action = False
        return action

click = False


def loading():
    running = True
    angle = 0
    count = 0
    clock = 0
    important = 0
    mixer.music.set_volume(0.2)
    while running:
        ecran.fill((0, 0, 0))
        angle +=1
        clock += 0.05
        important += 0.05
        if clock>1:
            count +=1
            clock = 0
        msg_loading=["Loading","Loading.","Loading..","Loading..."]
        rota_rena = pygame.transform.rotate(renard_loading, angle)
        new_rect = rota_rena.get_rect(center=renard_loading.get_rect(topleft=(infoObject.current_w*(8/9)+50,infoObject.current_h*(8/9))).center)
        ecran.blit(rota_rena,new_rect)
        font = pygame.font.Font("Minecraft.ttf", 25)
        if count > len(msg_loading)-1:
            count=0
        text = font.render(msg_loading[count], 1, (255, 255, 255))


        ecran.blit(text, (infoObject.current_w*(8/9)+25,infoObject.current_h*(8/9)+50))

        pygame.display.update()
        ticker.tick(60)
        if important > 20:
            print("C'est bon !")
            pygame.quit()
            sys.exit()


def main_menu():
    width = 800
    i = 0
    j = 0
    k = 0
    count = 0
    nat_count = 0
    while True:
        ecran.fill((99, 155, 255))

        ecran.blit(background.sky_bg, (i, 0))
        ecran.blit(background.sky_bg, (width + i, 0))
        ecran.blit(background.sky_bg, (width * 2 + i, 0))
        ecran.blit(background.sky_bg, (width * 3 + i, 0))

        ecran.blit(background.mountain_bg, (i, -100))
        ecran.blit(background.mountain_bg, (width + i, -100))
        ecran.blit(background.mountain_bg, (width * 2 + i, -100))
        ecran.blit(background.mountain_bg, (width * 3 + i, -100))

        if i < -width:
            i = 0
        if j < -width:
            j = 0
        if k < -width:
            k = 0
        i -= 1
        j -= 10
        k -= 3
        ecran.blit(background.forest_bg, (j, -90))
        ecran.blit(background.forest_bg, (width + j, -90))
        ecran.blit(background.forest_bg, (width * 2 + j, -90))
        ecran.blit(background.forest_bg, (width * 3 + j, -90))
        ecran.blit(background.forest_fg2, (k, 200))
        ecran.blit(background.forest_fg2, (width + k, 200))
        ecran.blit(background.forest_fg2, (width * 2 + k, 200))
        ecran.blit(background.forest_fg2, (width * 3 + k, 200))
        ecran.blit(background.forest_fg, (j, 280))
        ecran.blit(background.forest_fg, (width + j, 280))
        ecran.blit(background.forest_fg, (width * 2 + j, 280))
        ecran.blit(background.forest_fg, (width * 3 + j, 280))
        ecran.blit(background.nature_fg[nat_count], (j, 437))
        ecran.blit(background.nature_fg[nat_count], (width / 10 + j, 437))
        ecran.blit(background.nature_fg[nat_count], (width / 10 * 2 + j, 437))
        ecran.blit(background.nature_fg[nat_count], (width / 10 * 3 + j, 437))
        ecran.blit(background.nature_fg[nat_count], (width / 10 * 4 + j, 437))
        ecran.blit(background.nature_fg[nat_count], (width / 10 * 5 + j, 437))
        ecran.blit(background.nature_fg[nat_count], (width / 10 * 6 + j, 437))
        ecran.blit(background.nature_fg[nat_count], (width / 10 * 7 + j, 437))
        ecran.blit(background.nature_fg[nat_count], (width / 10 * 8 + j, 437))
        ecran.blit(background.nature_fg[nat_count], (width / 10 * 9 + j, 437))
        ecran.blit(background.nature_fg[nat_count], (width / 10 * 10 + j, 437))
        ecran.blit(background.nature_fg[nat_count], (width / 10 * 11 + j, 437))
        ecran.blit(background.nature_fg[nat_count], (width / 10 * 12 + j, 437))
        ecran.blit(background.nature_fg[nat_count], (width / 10 * 13 + j, 437))
        ecran.blit(background.nature_fg[nat_count], (width / 10 * 14 + j, 437))
        ecran.blit(background.nature_fg[nat_count], (width / 10 * 15 + j, 437))
        ecran.blit(background.nature_fg[nat_count], (width / 10 * 16 + j, 437))
        ecran.blit(background.nature_fg[nat_count], (width / 10 * 17 + j, 437))
        ecran.blit(background.nature_fg[nat_count], (width / 10 * 18 + j, 437))
        ecran.blit(background.nature_fg[nat_count], (width / 10 * 19 + j, 437))
        ecran.blit(background.nature_fg[nat_count], (width / 10 * 20 + j, 437))
        ecran.blit(background.nature_fg[nat_count], (width / 10 * 21 + j, 437))
        ecran.blit(background.nature_fg[nat_count], (width / 10 * 22 + j, 437))
        ecran.blit(background.nature_fg[nat_count], (width / 10 * 23 + j, 437))
        ecran.blit(background.nature_fg[nat_count], (width / 10 * 24 + j, 437))
        ecran.blit(background.nature_fg[nat_count], (width / 10 * 25 + j, 437))
        ecran.blit(background.nature_fg[nat_count], (width / 10 * 26 + j, 437))
        ecran.blit(background.nature_fg[nat_count], (width / 10 * 27 + j, 437))
        ecran.blit(background.nature_fg[nat_count], (width / 10 * 28 + j, 437))
        ecran.blit(background.nature_fg[nat_count], (width / 10 * 29 + j, 437))
        ecran.blit(background.nature_fg[nat_count], (width / 10 * 30 + j, 437))
        ecran.blit(background.nature_fg[nat_count], (width / 10 * 31 + j, 437))
        ecran.blit(background.nature_fg[nat_count], (width / 10 * 32 + j, 437))
        ecran.blit(background.nature_fg[nat_count], (width / 10 * 33 + j, 437))
        ecran.blit(background.nature_fg[nat_count], (width / 10 * 34 + j, 437))

        if count > 11:
            count = 0
        if nat_count > 7:
            nat_count = 0
        nat_count += 1
        ecran.blit(background.boat[count], (150, 600))
        count += 1

        play_button = Button(infoObject.current_w*(2/6),infoObject.current_h*(43/54),play_logo)
        options_button = Button(infoObject.current_w*(3/6), infoObject.current_h*(43/54), options_logo)
        quit_button = Button(infoObject.current_w*(4/6), infoObject.current_h*(43/54), quit_logo)
        play_button_pressed = Button(infoObject.current_w*(2/6), infoObject.current_h*(43/54), play_logo_pressed)
        options_button_pressed = Button(infoObject.current_w*(3/6), infoObject.current_h*(43/54), options_logo_pressed)
        quit_button_pressed = Button(infoObject.current_w*(4/6), infoObject.current_h*(43/54), quit_logo_pressed)


        if play_button.draw("   play"):
            play_button_pressed.draw("   play")
            loading()
        if options_button.draw("  options"):
            options_button_pressed.draw("  options")
            options()
        if quit_button.draw("   quit"):
            quit_button_pressed.draw("   quit")
            pygame.quit()
            sys.exit()

        ecran.blit(logo_game, (infoObject.current_w * (2 / 5), infoObject.current_h * (1 / 2)))
        '''draw_text('Crazy Extreme Fishing', taille, (70, 0, 150), ecran, (size[0]/2)-230, size[1]/8)

        sourisx, sourisy = pygame.mouse.get_pos()

        b1 = button(ecran, ((size[0]/2)-70, size[1]/3), " Jouer ",play_logo)

        b2 = button(ecran, ((size[0]/2)-70, size[1]/2), " Options ",options_logo)

        b3 = button(ecran, ((size[0]/2)-70, size[1]/1.5), " Quitter ",quit_logo)

        if b1.collidepoint((sourisx, sourisy)):
            b1 = button_press(ecran, ((size[0]/2)-70, size[1]/3), " Jouer ",play_logo_pressed)
            if clk:
                pygame.quit()
                sys.exit()

        if b2.collidepoint((sourisx, sourisy)):
            b1 = button_press(ecran, ((size[0]/2)-70, size[1]/2), " Options ",options_logo_pressed)
            if clk:
                options()

        if b3.collidepoint((sourisx, sourisy)):
            b3 = button_press(ecran, ((size[0]/2)-70, size[1]/1.5), " Quitter ",quit_logo_pressed)
            if clk:
                pygame.quit()
'''


        clk = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    clk = True

        pygame.display.update()
        ticker.tick(60)


def game():
    print("JOUER")

def options():

    running = True
    while running:
        pygame.draw.rect(ecran, (0, 0, 0), (infoObject.current_w*(1/8)-14, infoObject.current_h*(1/8)-14, infoObject.current_w*(3/4)+28, infoObject.current_h*(3/4)+28))
        pygame.draw.rect(ecran, (255, 100, 0), (infoObject.current_w*(1/8)-10, infoObject.current_h*(1/8)-10, infoObject.current_w*(3/4)+20,infoObject.current_h*(3/4) +20))
        pygame.draw.rect(ecran, (255, 125, 0), (infoObject.current_w*(1/8), infoObject.current_h*(1/8), infoObject.current_w*(3/4), infoObject.current_h*(3/4)))
        font = pygame.font.Font("Minecraft.ttf", 50)
        text = font.render("Options", 1, (255, 255, 255))
        textRect = text.get_rect()
        textRect.center = (infoObject.current_w // 2, infoObject.current_h *(1/5))

        ecran.blit(text,textRect)
        play_button1 = Button(infoObject.current_w * (2 / 6), infoObject.current_h * (43 / 54), play_logo)
        play_button1_pressed = Button(infoObject.current_w * (2 / 6), infoObject.current_h * (43 / 54), play_logo_pressed)
        if play_button1.draw("  Quitter"):
            play_button1_pressed.draw("  Quitter")
            running=False
            time.sleep(0.1)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()
        ticker.tick(60)


main_menu()
