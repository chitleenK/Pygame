#Chitleen Kohli
#import pygame, system and operating system
import pygame, sys, os
#importing to work with the ball
import random

#initializing pygame and fonts
pygame.init()
pygame.font.init()

#creating a window and intial elements
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong!")

#health stuff
HEALTH_FONT = pygame.font.SysFont('comicsans', 20)
WINNER_FONT = pygame.font.SysFont('comicsans', 100)
BLUE_HEALTH = 0
RED_HEALTH = 0

#creating the colour white
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

#border to seperate the two player game
BORDER = pygame.Rect(WIDTH // 2 - 5, 0, 10, HEIGHT)

#Platform lengths
PLATFORM_WIDTH, PLATFORM_HEIGHT = 10, 140

#hits stuff
BLUE_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2

#frames/second and velocity
FPS = 60
VEL = 5

#ball related variables
BALL_SPEED_X = 7
BALL_SPEED_Y = 7


#this method for drawing anything on the screen
def draw_window(blue_player, red_player, ball):
  #filling the screen with white
  WIN.fill(GREEN)
  pygame.draw.rect(WIN, WHITE, BORDER)
  #font for health
  blue_health_text = HEALTH_FONT.render("Health: " + str(BLUE_HEALTH), 1,
                                        BLACK)
  red_health_text = HEALTH_FONT.render("Health: " + str(RED_HEALTH), 1, BLACK)
  WIN.blit(blue_health_text, (WIDTH - red_health_text.get_width() - 10, 10))
  WIN.blit(red_health_text, (10, 10))
  #putting the character's platform on the screen
  pygame.draw.rect(WIN, BLUE, blue_player)
  pygame.draw.rect(WIN, RED, red_player)
  pygame.draw.ellipse(WIN, BLACK, ball)
  pygame.display.update()


#method for handling the movement of blue platform
def blue_handle_movement(keys_pressed, blue_player):
  if keys_pressed[pygame.K_w] and blue_player.y - VEL > 0:  #up key
    blue_player.y -= VEL
  if keys_pressed[
      pygame.
      K_s] and blue_player.y + VEL + blue_player.height < HEIGHT - 15:  #down key
    blue_player.y += VEL


#method for handling the movement of red platform
def red_handle_movement(keys_pressed, red_player):
  if keys_pressed[pygame.K_UP] and red_player.y - VEL > 0:  #up key
    red_player.y -= VEL
  if keys_pressed[
      pygame.
      K_DOWN] and red_player.y + VEL + red_player.height < HEIGHT - 15:  #down key
    red_player.y += VEL


#method for handling ball movement
def ball_handle_movement(blue_player, red_player, ball):
  #using the global function avoid the UnboundLocalError
  global BALL_SPEED_X, BALL_SPEED_Y, BLUE_HEALTH, RED_HEALTH
  #moving the ball forward to intialize the game
  ball.x += BALL_SPEED_X
  ball.y += BALL_SPEED_Y
  #handling the movement for vertical axis and bouncing back
  if ball.top <= 0 or ball.bottom >= HEIGHT:
    BALL_SPEED_Y *= -1
  #handling the movement for horizontal axis
  if ball.left <= 0:
    RED_HEALTH += 1
    #randomize ball once it hits one of the sides of the screen
    ball.center = (WIDTH / 2, HEIGHT / 2)
    BALL_SPEED_Y *= random.choice((1, -1))
    BALL_SPEED_X *= random.choice((1, -1))
  if ball.right >= WIDTH:
    BLUE_HEALTH += 1
    #randomize ball once it hits one of the sides of the screen
    ball.center = (WIDTH / 2, HEIGHT / 2)
    BALL_SPEED_Y *= random.choice((1, -1))
    BALL_SPEED_X *= random.choice((1, -1))
  #handling collision of ball with the platforms
  if ball.colliderect(blue_player):
    BALL_SPEED_X *= -1
  if ball.colliderect(red_player):
    BALL_SPEED_X *= -1


#handling when someone won
def draw_winner(text):
  draw_text = WINNER_FONT.render(text, 1, BLACK)
  WIN.blit(draw_text, (WIDTH / 2 - draw_text.get_width() / 2,
                       HEIGHT / 2 - draw_text.get_height()))
  pygame.display.update()
  pygame.time.delay(5000)


#first pygame event loop
def main():
  #to show the characters
  blue_player = pygame.Rect(815, 350, PLATFORM_WIDTH, PLATFORM_HEIGHT)
  red_player = pygame.Rect(25, 350, PLATFORM_WIDTH, PLATFORM_HEIGHT)
  #drawing the ball on the screen
  ball = pygame.Rect(WIDTH / 2, HEIGHT / 2, 20, 20)
  clock = pygame.time.Clock()
  run = True
  while run:
    clock.tick(FPS)
    for event in pygame.event.get():
      #effectivly quiting the game
      if event.type == pygame.QUIT:
        run = False
        pygame.quit()
    #handling when someone won
    winner_text = ""
    if BLUE_HEALTH >= 2:
      winner_text = "Blue wins!!!"
    if RED_HEALTH >= 10:
      winner_text = "Red Wins!!!"
    if winner_text != "":
      draw_winner(winner_text)
      break
    #players can move their platforms using keys
    keys_pressed = pygame.key.get_pressed()
    blue_handle_movement(keys_pressed, blue_player)
    red_handle_movement(keys_pressed, red_player)
    ball_handle_movement(blue_player, red_player, ball)
    draw_window(blue_player, red_player, ball)
  main()


#making ensure that if we run this file we only run this main function when we run this file directly
if __name__ == "__main__":
  main()
