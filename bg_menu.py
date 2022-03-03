import pygame

class Background(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.mountain_bg = pygame.transform.scale(pygame.image.load("Assets/Mountains.png"), (800, 440))
        self.forest_bg = pygame.transform.scale(pygame.image.load("Assets/Forest.png"), (800, 440))
        self.sky_bg = pygame.transform.scale(pygame.image.load("Assets/SkyBG.png"), (800, 340))
        self.forest_fg = pygame.transform.scale(pygame.image.load("Assets/pine1.png"), (800, 200))
        self.forest_fg2 = pygame.transform.scale(pygame.image.load("Assets/pine2.png"), (800, 200))
        self.boat = [pygame.transform.scale(pygame.image.load("Assets/Boat1.png"), (440, 180)),
            pygame.transform.scale(pygame.image.load("Assets/Boat1.png"), (440, 180)),
            pygame.transform.scale(pygame.image.load("Assets/Boat1.png"), (440, 180)),
            pygame.transform.scale(pygame.image.load("Assets/Boat2.png"), (440, 180)),
            pygame.transform.scale(pygame.image.load("Assets/Boat2.png"), (440, 180)),
            pygame.transform.scale(pygame.image.load("Assets/Boat2.png"), (440, 180)),
            pygame.transform.scale(pygame.image.load("Assets/Boat3.png"), (440, 180)),
            pygame.transform.scale(pygame.image.load("Assets/Boat3.png"), (440, 180)),
            pygame.transform.scale(pygame.image.load("Assets/Boat3.png"), (440, 180)),
            pygame.transform.scale(pygame.image.load("Assets/Boat4.png"), (440, 180)),
            pygame.transform.scale(pygame.image.load("Assets/Boat4.png"), (440, 180)),
            pygame.transform.scale(pygame.image.load("Assets/Boat4.png"), (440, 180))]
        self.nature_fg = [pygame.transform.scale(pygame.image.load("Assets/secondground1.png"), (80, 80)),
                 pygame.transform.scale(pygame.image.load("Assets/secondground1.png"), (80, 80)),
                 pygame.transform.scale(pygame.image.load("Assets/secondground1.png"), (80, 80)),
                 pygame.transform.scale(pygame.image.load("Assets/secondground2.png"), (80, 80)),
                 pygame.transform.scale(pygame.image.load("Assets/secondground2.png"), (80, 80)),
                 pygame.transform.scale(pygame.image.load("Assets/secondground2.png"), (80, 80)),
                 pygame.transform.scale(pygame.image.load("Assets/secondground3.png"), (80, 80)),
                 pygame.transform.scale(pygame.image.load("Assets/secondground3.png"), (80, 80)),
                 pygame.transform.scale(pygame.image.load("Assets/secondground3.png"), (80, 80))]
