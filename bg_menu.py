import pygame

class Background(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.mountain_bg = pygame.transform.scale(pygame.image.load("Assets/Start_Menu/Mountains.png").convert_alpha(), (800, 440))
        self.forest_bg = pygame.transform.scale(pygame.image.load("Assets/Start_Menu/Forest.png").convert_alpha(), (800, 440))
        self.sky_bg = pygame.transform.scale(pygame.image.load("Assets/Start_Menu/SkyBG.png").convert_alpha(), (800, 340))
        self.forest_fg = pygame.transform.scale(pygame.image.load("Assets/Start_Menu/pine1.png").convert_alpha(), (800, 200))
        self.forest_fg2 = pygame.transform.scale(pygame.image.load("Assets/Start_Menu/pine2.png").convert_alpha(), (800, 200))
        self.boat = [pygame.transform.scale(pygame.image.load("Assets/Start_Menu/Boat1.png").convert_alpha(), (440, 180)),
            pygame.transform.scale(pygame.image.load("Assets/Start_Menu/Boat1.png").convert_alpha(), (440, 180)),
            pygame.transform.scale(pygame.image.load("Assets/Start_Menu/Boat1.png").convert_alpha(), (440, 180)),
            pygame.transform.scale(pygame.image.load("Assets/Start_Menu/Boat2.png").convert_alpha(), (440, 180)),
            pygame.transform.scale(pygame.image.load("Assets/Start_Menu/Boat2.png").convert_alpha(), (440, 180)),
            pygame.transform.scale(pygame.image.load("Assets/Start_Menu/Boat2.png").convert_alpha(), (440, 180)),
            pygame.transform.scale(pygame.image.load("Assets/Start_Menu/Boat3.png").convert_alpha(), (440, 180)),
            pygame.transform.scale(pygame.image.load("Assets/Start_Menu/Boat3.png").convert_alpha(), (440, 180)),
            pygame.transform.scale(pygame.image.load("Assets/Start_Menu/Boat3.png").convert_alpha(), (440, 180)),
            pygame.transform.scale(pygame.image.load("Assets/Start_Menu/Boat4.png").convert_alpha(), (440, 180)),
            pygame.transform.scale(pygame.image.load("Assets/Start_Menu/Boat4.png").convert_alpha(), (440, 180)),
            pygame.transform.scale(pygame.image.load("Assets/Start_Menu/Boat4.png").convert_alpha(), (440, 180))]
        self.nature_fg = [pygame.transform.scale(pygame.image.load("Assets/Start_Menu/secondground1.png").convert_alpha(), (80, 80)),
                 pygame.transform.scale(pygame.image.load("Assets/Start_Menu/secondground1.png").convert_alpha(), (80, 80)),
                 pygame.transform.scale(pygame.image.load("Assets/Start_Menu/secondground1.png").convert_alpha(), (80, 80)),
                 pygame.transform.scale(pygame.image.load("Assets/Start_Menu/secondground2.png").convert_alpha(), (80, 80)),
                 pygame.transform.scale(pygame.image.load("Assets/Start_Menu/secondground2.png").convert_alpha(), (80, 80)),
                 pygame.transform.scale(pygame.image.load("Assets/Start_Menu/secondground2.png").convert_alpha(), (80, 80)),
                 pygame.transform.scale(pygame.image.load("Assets/Start_Menu/secondground3.png").convert_alpha(), (80, 80)),
                 pygame.transform.scale(pygame.image.load("Assets/Start_Menu/secondground3.png").convert_alpha(), (80, 80)),
                 pygame.transform.scale(pygame.image.load("Assets/Start_Menu/secondground3.png").convert_alpha(), (80, 80))]
