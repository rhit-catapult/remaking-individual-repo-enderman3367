import pygame
import sys


def main():
    pygame.init()
    pygame.display.set_caption("Moving Smile")
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    
    # Variables for pupil positions
    left_pupil_x = 242
    left_pupil_y = 162
    right_pupil_x = 398
    right_pupil_y = 162

    while True:
        clock.tick(60)  # TODO 4: Set the clock speed to 60 fps
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # TODO 3: Make the eye pupils move with Up, Down, Left, and Right keys
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    left_pupil_y -= 5
                    right_pupil_y -= 5
                elif event.key == pygame.K_DOWN:
                    left_pupil_y += 5
                    right_pupil_y += 5
                elif event.key == pygame.K_LEFT:
                    left_pupil_x -= 5
                    right_pupil_x -= 5
                elif event.key == pygame.K_RIGHT:
                    left_pupil_x += 5
                    right_pupil_x += 5

        screen.fill((255, 255, 255))  # white

        # API --> pygame.draw.circle(screen, color, (x, y), radius, thickness)

        pygame.draw.circle(screen, (255, 255, 0), (320, 240), 210)  # yellow circle
        pygame.draw.circle(screen, (0, 0, 0), (320, 240), 210, 4)  # black outline

        pygame.draw.circle(screen, (225, 225, 225), (240, 160), 25)  # white eye
        pygame.draw.circle(screen, (0, 0, 0), (240, 160), 25, 3)  # black outline
        pygame.draw.circle(screen, (0, 0, 0), (left_pupil_x, left_pupil_y), 7)  # black pupil

        pygame.draw.circle(screen, (225, 225, 225), (400, 160), 25)  # white eye
        pygame.draw.circle(screen, (0, 0, 0), (400, 160), 25, 3)  # black outline
        pygame.draw.circle(screen, (0, 0, 0), (right_pupil_x, right_pupil_y), 7)  # black pupil

        # TODO 1: Draw a nose
        # Suggestion: color (80,0,0) location (320,245), radius 10
        # API --> pygame.draw.circle(screen, (r,g,b), (x, y), radius, thickness)
        pygame.draw.circle(screen, (80, 0, 0), (320, 245), 10)

        # TODO 2: Draw a mouth
        # Suggestion: color (0,0,0), x 230, y 320, width 180, height 30
        # API --> pygame.draw.rect(screen, (r,g,b), (x, y, width, height), thickness)
        pygame.draw.rect(screen, (0, 0, 0), (230, 320, 180, 30))

        pygame.display.update()


main()
