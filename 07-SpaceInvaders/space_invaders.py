import pygame
import sys

# TODO: when need import the fighter_missile_module
import fighter_missile_module
# TODO: when need import the enemy_fleet_module
import enemy_fleet_module


class Scoreboard:
    def __init__(self, screen):
        self.screen = screen
        self.score = 0
        self.font = pygame.font.Font(None, 30)
    
    def draw(self):
        score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        self.screen.blit(score_text, (5, 5))


def main():
    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption("SPACE INVADERS!")
    screen = pygame.display.set_mode((640, 650))

    # TODO 9: Set    enemy_rows    to an initial value of 3.
    enemy_rows = 3
    # TODO 10: Create an EnemyFleet object (called enemy_fleet) with the screen and enemy_rows
    enemy_fleet = enemy_fleet_module.EnemyFleet(screen, enemy_rows)
    # TODO 1: Create a Fighter (called fighter)
    fighter = fighter_missile_module.Fighter(screen)
    
    # TODO 23: Create a Scoreboard class (from scratch)
    scoreboard = Scoreboard(screen)
    
    # Game over variables
    game_over = False
    gameover_image = pygame.image.load("gameover.png")

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            # TODO 5: If the event type is KEYDOWN and pressed_keys[pygame.K_SPACE] is True, then fire a missile
            if event.type == pygame.KEYDOWN:
                pressed_keys = pygame.key.get_pressed()
                if pressed_keys[pygame.K_SPACE]:
                    fighter.fire()
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill((0, 0, 0))
        
        # Check for continuous key presses
        pressed_keys = pygame.key.get_pressed()
        # TODO 3: If pygame.K_LEFT is pressed and move the fighter left 5 (i.e. -5)
        if pressed_keys[pygame.K_LEFT]:
            fighter.move(-5)
        # TODO 4: If pygame.K_RIGHT is pressed and move the fighter right 5
        if pressed_keys[pygame.K_RIGHT]:
            fighter.move(5)
        
        # TODO 2: Draw the fighter
        fighter.draw()

        # TODO 11: Move the enemy_fleet
        enemy_fleet.move()
        # TODO 12: Draw the enemy_fleet
        enemy_fleet.draw()

        # TODO 6: For each missile in the fighter missiles
        for missile in fighter.missiles:
            #   TODO 7: Move the missile
            missile.move()
            #   TODO 8: Draw the missile
            missile.draw()

        # TODO 12: For each badguy in the enemy_fleet.badguys list
        for badguy in enemy_fleet.badguys:
            #     TODO 13: For each missile in the fighter missiles
            for missile in fighter.missiles:
                #         TODO 14: If the badguy is hit by the missile
                if badguy.is_hit_by(missile):
                    #             TODO 15: Mark the badguy is_dead = True
                    badguy.is_dead = True
                    #             TODO 16: Mark the missile has_exploded = True
                    missile.has_exploded = True
                    # When a Badguy is killed add 100 points to the scoreboard.score
                    scoreboard.score += 100

        # Optional TODOs (technically this is already done within fighter.remove_exploded_missiles)
        # TODO 16.5: For each missile in the fighter missiles
        for missile in fighter.missiles:
            #     TODO 16.5: If the missle is off the screen
            if missile.is_off_screen():
                #         TODO 16.5: Mark the missile has_exploded = True (cleaning up off screen stuff)
                missile.has_exploded = True

        # TODO 17: Use the fighter to remove exploded missiles
        fighter.remove_exploded_missiles()
        # TODO 18: Use the enemy_fleet to remove dead badguys
        enemy_fleet.remove_dead_badguys()

        # TODO 19: If the enemy is_defeated
        if enemy_fleet.is_defeated:
            #     TODO 20: Increment the enemy_rows
            enemy_rows += 1
            #     TODO 21: Create a new enemy_fleet with the screen and enemy_rows
            enemy_fleet = enemy_fleet_module.EnemyFleet(screen, enemy_rows)

        # TODO 22: Check for your death.  Figure out what needs to happen.
        # Hints: Check if a Badguy gets a y value greater than 545
        #    Note: 545 is screen.get_height() -
        #    If that happens set a variable (game_over) as appropriate
        #    If the game is over, show the gameover.png image at (170, 200)
        for badguy in enemy_fleet.badguys:
            if badguy.y > 545:
                game_over = True
                break

        # TODO 23: Create a Scoreboard class (from scratch)
        # Hints: Instance variables: screen, score, and font (size 30)
        #    Methods: draw (and __init__)
        # Create a scoreboard and draw it at location 5, 5
        scoreboard.draw()

        # Show game over screen if needed
        if game_over:
            screen.blit(gameover_image, (170, 200))

        # TODO 24: Optional extra - Add sound effects!

        pygame.display.update()


main()
