#####################################################################
#                            CONTROLS                               #
#####################################################################
# Pygame joystick controls for Xbox One controller.
import sys
import pygame
from pygame.locals import *

# Initializes Pygame.
pygame.init()


#####################################################################
#                              CLASS                                #
#####################################################################
class Controls:
    def __init__(self):
        
        # Create the joystick object.
        self.controller = pygame.joystick.Joystick(0)

        # Controller state attributes.
        self.joy_released = True

        # Left joystick input raw (0.0-1.0) or rounded (0-1).
        self.left_joy_lr_raw = self.controller.get_axis(0) # L=-1.0/R=1.0
        self.left_joy_ud_raw = self.controller.get_axis(1) # U=-1.0/D=1.0
        self.left_joy_lr_rnd = round(self.controller.get_axis(0)) # L=-1/R=1
        self.left_joy_ud_rnd = round(self.controller.get_axis(1)) # U=-1/D=1

        # Right joystick input raw (0.0-1.0) or rounded (0-1).
        self.right_joy_lr_raw = self.controller.get_axis(2) # L=-1.0/R=1.0
        self.right_joy_ud_raw = self.controller.get_axis(3) # U=-1.0/D=1.0
        self.right_joy_lr_rnd = round(self.controller.get_axis(2)) # L=-1/R=1
        self.right_joy_ud_rnd = round(self.controller.get_axis(3)) # U=-1/D=1

        # Basic button inputs. On=1/Off=0.
        self.a_button = self.controller.get_button(0)
        self.b_button = self.controller.get_button(1)
        self.x_button = self.controller.get_button(2)
        self.y_button = self.controller.get_button(3)
        self.lb_button = self.controller.get_button(4)
        self.rb_button = self.controller.get_button(5)
        self.select = self.controller.get_button(6)
        self.start = self.controller.get_button(7)
        self.ls_button = self.controller.get_button(8)
        self.rs_button = self.controller.get_button(9)
        self.left_trigger = self.controller.get_axis(4) # On=1/Off=-1
        self.right_trigger = self.controller.get_axis(5) # On=1/Off=-1
    

    # Moderates joystick input between 0.1 and 1.0.
    def joystick_input(self, input):
        if input >= 0.1 or input <= -0.1:
            return input
        else:
            return 0
    

    # Returns Dpad input as TRUE or FALSE.
    def check_dpad(self, direction): # Direction must = 1 of the 4 directions.
        if direction == 'left' and self.controller.get_hat(0) == (-1, 0):
            return True
        elif direction == 'right' and self.controller.get_hat(0) == (1, 0):
            return True
        elif direction == 'up' and self.controller.get_hat(0) == (0, 1):
            return True
        elif direction == 'down' and self.controller.get_hat(0) == (0, -1):
            return True
        else:
            return False
    

    # Determines joystick state.
    def joystick_state_check(self, joystick):
        if joystick < 0.1 and joystick > -0.1:
            return True
        else:
            return False
        
    
    # Returns a single click from joystick input.
    def single_joystick_click(self, input, output, max_output):
        if self.joy_released:
            if input == 1:
                output -= 1
                if output > max_output:
                    output = 0
                    return output
                elif output < 0:
                    output = max_output
                    return output
                else:
                    return output
            elif input == -1:
                output += 1
                if output > max_output:
                    output = 0
                    return output
                elif output < 0:
                    output = max_output
                    return output
                else:
                    return output
            else:
                return output
        else:
            return output
    

    # Basic QUIT controlls. 
    def quit_controls(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        pressed = pygame.key.get_pressed()
        if pressed[K_ESCAPE]:
            pygame.quit()
            sys.exit()


#####################################################################
#                            CONCLUSION                             #
#####################################################################
