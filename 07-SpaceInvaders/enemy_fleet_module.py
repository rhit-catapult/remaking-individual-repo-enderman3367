import pygame
import sys


class Badguy:
    def __init__(self, screen, x, y, speed):
        # Store the given arguments as instance variables with the same names.
        # Set   is_dead to False   and   original_x to x.
        # Load the file  "badguy.png"  as the image. and set its colorkey to black.
        # Additionally make a   move_right   instance variable set to to True (we might us it in the move method).
        self.screen = screen
        self.x = x
        self.y = y
        self.speed = speed
        self.is_dead = False
        self.original_x = x
        self.image = pygame.image.load("badguy.png")
        self.image.set_colorkey((0, 0, 0))
        self.move_right = True

    def move(self):
        # Move self.speed units horizontally in the current direction.
        # If this Badguy's horizontal position is more than 100 pixels from its original x position, then...
        #     change the direction
        #     move the y down 4 * self.speed units
        if self.move_right:
            self.x += self.speed
        else:
            self.x -= self.speed
            
        if abs(self.x - self.original_x) > 100:
            self.move_right = not self.move_right
            self.y += 4 * self.speed

    def draw(self):
        # Draw this Badguy, using its image at its current (x, y) position.
        self.screen.blit(self.image, (self.x, self.y))

    def is_hit_by(self, missile):
        # Make a Badguy hitbox rect.
        # Return True if that hitbox collides with the xy point of the given missile.
        badguy_rect = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())
        return badguy_rect.collidepoint(missile.x, missile.y)


class EnemyFleet:
    def __init__(self, screen, enemy_rows):
        # Already done.  Prepares the list of Badguys.
        self.badguys = []
        for j in range(enemy_rows):
            for k in range(8):
                self.badguys.append(Badguy(screen, 80 * k, 50 * j + 20, enemy_rows))

    @property
    def is_defeated(self):
        # Return True if the number of badguys in this Enemy Fleet is 0,
        # otherwise return False.
        return len(self.badguys) == 0

    def move(self):
        # Make each Badguy in badguys move.
        for badguy in self.badguys:
            badguy.move()

    def draw(self):
        # Make each Badguy in badguys draw itself.
        for badguy in self.badguys:
            badguy.draw()

    def remove_dead_badguys(self):
        for k in range(len(self.badguys) - 1, -1, -1):
            if self.badguys[k].is_dead:
                del self.badguys[k]


def main():
    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption("Testing the Enemy Fleet and Badguys only")
    screen = pygame.display.set_mode((640, 650))

    enemy_rows = 4
    enemy_fleet = EnemyFleet(screen, enemy_rows)

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill((0, 0, 0))
        enemy_fleet.draw()
        enemy_fleet.move()

        # enemy_fleet.remove_dead_badguys()
        pygame.display.update()


# Testing the classes
if __name__ == "__main__":
    main()
