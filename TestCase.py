import unittest
import math
import csv
import player
import pygame
from Pygame import Player, Enemy, GameLevel, display_end_screen 

class TestPlayerInitialization(unittest.TestCase):
 def setUp(self):
     pygame.init()
     self.player_instance = Player((10, 10)) 

 def tearDown(self):
     pygame.quit()
# Assertions to check the position of the player.
 def test_initial_state(self):
     self.assertEqual(self.player_instance.pos, (10, 10))
     self.assertEqual(self.player_instance.vec_pos, pygame.math.Vector2(10, 10))
     self.assertEqual(self.player_instance.base_player_rect.center, (10, 10))
     self.assertEqual(self.player_instance.rect, self.player_instance.base_player_rect.copy())
     self.assertEqual(self.player_instance.player_speed, 10)
     self.assertEqual(self.player_instance.shoot, False)
     self.assertEqual(self.player_instance.shoot_cooldown, 0)
     self.assertEqual(self.player_instance.health, 100)
     self.assertEqual(self.player_instance.gun_barrel_offset, pygame.math.Vector2(45, 20))

class TestPlayerMovement(unittest.TestCase):
  def setUp(self):
      pygame.init()
      self.player_instance = Player((10, 10)) # initial position of the player.

  def tearDown(self):
      pygame.quit()

  def test_player_turning(self):
      # Mouse position.
      pygame.mouse.set_pos((20, 20))
      self.player_instance.player_turning()
      # angle
      self.assertEqual(self.player_instance.angle, 45)

  def test_player_input(self):
      # keyboard and mouse inputs
      pygame.key.set_pressed([pygame.K_w])
      pygame.mouse.set_pressed([1, 0, 0])
      self.player_instance.player_input()
      #velocity and shooting state
      self.assertEqual(self.player_instance.velocity_y, -10)
      self.assertEqual(self.player_instance.shoot, True)

  def test_move(self):
      #velocity
      self.player_instance.velocity_x = 10
      self.player_instance.velocity_y = 10
      #player movement
      self.player_instance.move()
      # position of the player
      self.assertEqual(self.player_instance.base_player_rect.centerx, 20)
      self.assertEqual(self.player_instance.base_player_rect.centery, 20)

class TestEnemyMovement(unittest.TestCase):
  def setUp(self):
      pygame.init()
      self.enemy_instance = Enemy("necromancer", (10, 10)) # Position of the Enemy

  def tearDown(self):
      pygame.quit()

  def test_check_alive(self):
      # Health
      self.enemy_instance.health = 0
      self.enemy_instance.check_alive()
      # alive state
      self.assertEqual(self.enemy_instance.alive, False)

  def test_roam(self):
      # velocity and direction
      self.enemy_instance.velocity = pygame.math.Vector2(10, 10)
      self.enemy_instance.direction = pygame.math.Vector2(1, 1)
      # Enemy Roam
      self.enemy_instance.roam()
      # position
      self.assertEqual(self.enemy_instance.position, (20, 20))

  def test_hunt_player(self):
     # Mock the player position
     player.base_player_rect.center = (20, 20)
     self.enemy_instance.hunt_player()
     # Check the position and direction
     self.assertEqual(self.enemy_instance.position, (20, 20))
     self.assertEqual(self.enemy_instance.direction, pygame.math.Vector2(-10, -10))

  def test_get_vector_distance(self):
     # player and enemy positions
     player_vector = pygame.math.Vector2(player.base_player_rect.center)
     enemy_vector = pygame.math.Vector2(self.enemy_instance.base_zombie_rect.center)
     # distance
     self.assertEqual(self.enemy_instance.get_vector_distance(player_vector, enemy_vector), 10)

  def test_animate(self):
     # sprite and animation speed
     self.enemy_instance.animations["hunt"] = [pygame.Surface((10, 10)) for _ in range(10)]
     self.enemy_instance.animation_speed = 1
     self.enemy_instance.current_index = 0
     # Enemy Animation
     self.enemy_instance.animate(self.enemy_instance.current_index, self.enemy_instance.animation_speed, self.enemy_instance.animations["hunt"], "hunt")
     # current index
     self.assertEqual(self.enemy_instance.current_index, 1)

  def test_check_player_collision(self):
     #player and enemy positions
     player.base_player_rect.center = self.enemy_instance.base_zombie_rect.center
     # collisions
     self.enemy_instance.check_player_collision()
     # Health of the player
     self.assertEqual(player.health, player.health - self.enemy_instance.attack_damage)

  def test_draw_enemy_health(self):
     # Health and position
     self.enemy_instance.health = 50
     self.enemy_instance.base_zombie_rect.center = (20, 20)
     # Enemy health
     self.enemy_instance.draw_enemy_health(self.enemy_instance.position[0], self.enemy_instance.position[1])
     # Health bar length
     self.assertEqual(self.enemy_instance.health_bar_length, 50)

  def test_update(self):
     # Updateing the enemy
     self.enemy_instance.update()
     #Health bar length
     self.assertEqual(self.enemy_instance.health_bar_length, 50)
 
class TestEndScreenDisplay(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.screen = pygame.Surface((800, 600))  

    def test_display_end_screen_game_over(self):
        # game over conditions
        beat_game = False
        game_stats = {
            'necromancer_death_count': 2,
            'nightborne_death_count': 3,
            'coins': 10,
        }

        # function to display the end screen
        display_end_screen(self.screen, pygame.font.Font(None, 36), beat_game, game_stats)

        #"GAME OVER" text is displayed
        self.assertTrue("GAME OVER" in pygame.display.get_surface().get_data())

    def test_display_end_screen_beat_game(self):
        # Simulate beating the game conditions
        beat_game = True
        game_stats = {
            'necromancer_death_count': 5,
            'nightborne_death_count': 7,
            'coins': 20,
        }

        # function to display the end screen
        display_end_screen(self.screen, pygame.font.Font(None, 36), beat_game, game_stats)

        # Add assertions based on the expected display for beating the game
        # "You beat the game! Thanks for playing!" text is displayed
        self.assertTrue("You beat the game! Thanks for playing!" in pygame.display.get_surface().get_data())

        

if __name__ == '__main__':
 unittest.main()








