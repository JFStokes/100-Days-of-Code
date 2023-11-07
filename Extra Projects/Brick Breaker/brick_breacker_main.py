#####################################################################
#                          BRICK BREAKER                            #
# Version: 1.0                                                      #
# Date:                                                             #
#####################################################################
import sys
import pygame
from pygame.locals import *
from controls import Controls
from mechanics import Mechanics


# Initializes custom modules.
input = Controls()
mech = Mechanics()

# Initializes Pygame.
pygame.init()

# Creates the 'screen' surface.
screen = pygame.display.set_mode((mech.screen_w, mech.screen_h))

# Sets the window caption.
pygame.display.set_caption('Josh\'s Brick Breaker')


#####################################################################
#                            MAIN LOOP                              #
#####################################################################
title_text = mech.title_font.render(
    'Josh\'s Brick Breaker', True, mech.WHITE
)
controller = pygame.joystick.Joystick(0)
button_index = 0
main_loop_clock = pygame.time.Clock()
main_loop_running = True
while main_loop_running:

    # Delta Time (dt) for Main Loop.
    dt = main_loop_clock.tick(10)

    #---------------------- CONTROLS -----------------------#
    # Variable for left joystick up/down axis.
    left_joy_ud = controller.get_axis(1) # U-1/D=1.
    left_joy_ud = round(left_joy_ud)

    # Checks for quit/exit commands.
    input.quit_controls()
    if button_index == 1 and controller.get_button(0) == 1:
        pygame.quit()
        sys.exit()

    # Returns button index.
    button_index = input.single_joystick_click(left_joy_ud, button_index, 1)

    # Sets joystick status to True or False.
    input.joy_released = input.joystick_state_check(left_joy_ud)

    #--------------------- RENDERING -----------------------#
    # Resets screen fill to BLACK.
    screen.fill((mech.BLACK))

    # Renders title text to screen.
    title = screen.blit(title_text, (
        mech.center_to_screen(title_text.get_rect(), 50)
            )
        )

    # Render START button.
    if button_index == 0:
        play_button_image = mech.button_large_selected_image
    else:
        play_button_image = mech.button_large_image

    play_button = screen.blit(play_button_image, (
        mech.center_below_rect(play_button_image.get_rect(), 
                               title.bottom, 200)
    ))

    start_button_text = mech.header_font.render(
        'START', True, mech.WHITE
    )

    screen.blit(start_button_text, (
        mech.center_inside(start_button_text.get_rect(), 
                           play_button.centerx, play_button.centery)
    ))

    # Render QUIT button.
    if button_index == 1:
        quit_button_image = mech.button_large_selected_image
    else:
        quit_button_image = mech.button_large_image

    quit_button = screen.blit(quit_button_image, (
        mech.center_below_rect(quit_button_image.get_rect(),
                               play_button.bottom, 50)
    ))

    quit_button_text = mech.header_font.render(
        'QUIT', True, mech.WHITE
    )

    screen.blit(quit_button_text, (
        mech.center_inside(quit_button_text.get_rect(),
                           quit_button.centerx, quit_button.centery)
    ))

    # Makes the display update each frame.
    pygame.display.update()


#####################################################################
#                            CONCLUSION                             #
#####################################################################
# Exits the Game.
pygame.quit()

