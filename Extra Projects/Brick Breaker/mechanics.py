#####################################################################
#                            MECHANICS                              #
#                         (Brick Breacker)                          #
#####################################################################
import pygame
from pygame.locals import *


# Initializes Pygame.
pygame.init()

# Creates the 'screen' surface.
screen = pygame.display.set_mode((0, 0))


#####################################################################
#                           LOAD ASSETS                             #
#####################################################################
bar_image = pygame.image.load(
'Extra Projects/Brick Breaker/assets/bar.png'
) # (32, 4).
bar_image = bar_image.convert_alpha()
ball_image = pygame.image.load(
'Extra Projects/Brick Breaker/assets/ball.png'
) # (8, 8).
ball_image = ball_image.convert_alpha()
brick_image = pygame.image.load(
'Extra Projects/Brick Breaker/assets/brick.png'
) # (16, 9).
brick_image = brick_image.convert_alpha()
button_large_image = pygame.image.load(
    'Extra Projects/Brick Breaker/assets/button_large.png'
) # (32, 8).
button_large_image = button_large_image.convert_alpha()
button_large_selected_image = pygame.image.load(
    'Extra Projects/Brick Breaker/assets/button_large_selected.png'
) # (32, 8).
button_large_selected_image = button_large_selected_image.convert_alpha()
font = 'Extra Projects/Brick Breaker/assets/AtariClassicChunky-PxXP.ttf'

#####################################################################
#                              CLASS                                #
#####################################################################
class Mechanics:
    def __init__(self):

        # Basic attributes.
        self.screen_w = 800 # max = 1920.
        self.screen_h = 800 # max = 1080
        self.fps = 15

        # Constant attributes.
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.GREY = (128, 128, 128)

        # Asset attributes.
        self.title_font = pygame.font.Font(font, 48)
        self.header_font = pygame.font.Font(font, 24)
        self.base_font = pygame. font.Font(font, 14)
        self.ball = pygame.transform.scale(ball_image, (32, 32))
        self.ball_rect = self.ball.get_rect()
        self.bar = pygame.transform.scale(bar_image, (128, 12))
        self.bar_rect = self.bar.get_rect()
        self.brick = pygame.transform.scale(brick_image, (64, 36))
        self.brick_rect = self.brick.get_rect()
        self.button_large_image = pygame.transform.scale(
            button_large_image, (320, 80)
        )
        self.button_large_selected_image = pygame.transform.scale(
            button_large_selected_image, (320, 80)
        )
    

############################ CENTERING ##############################
    def center_inside(self, new_rect, centerx, centery):
        return (
            centerx - new_rect[2] / 2,
            centery - new_rect[3] / 2
        )
    
    def center_below_rect(self, new_rect, old_rect, offset_below):
        return (
            self.screen_w / 2 - new_rect[2] / 2,
            old_rect + offset_below
        )
    
    def center_to_screen(self, new_rect, offset):
        return (
            self.screen_w / 2 - new_rect[2] / 2,
            new_rect[1] + offset
        )


#####################################################################
#                            CONCLUSION                             #
#####################################################################

