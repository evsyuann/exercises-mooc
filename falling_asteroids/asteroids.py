import pygame
from random import randint


class Rock:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


def print_text(points: int):
    game_font = pygame.font.SysFont("Arial", 24)
    text = game_font.render(f"Points: {points}", True, (255, 0, 0))
    window.blit(text, (500, 40))


def adding_rocks():
    rocks = []
    for i in range(10):
        generated_x = randint(0, (640 - rock.get_width()))
        rocks.append(Rock(generated_x, -100 * i))
    return rocks


pygame.init()
pygame.display.set_caption("Asteroids")
window = pygame.display.set_mode((640, 480))

rock = pygame.image.load("rock.png")
robot = pygame.image.load("robot.png")

clock = pygame.time.Clock()

while True:
    to_right = False
    to_left = False
    x_robot = 0
    y_robot = 480 - robot.get_height()
    rocks = adding_rocks()

    points = 0
    game_is_running = True
    while game_is_running == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    to_left = True
                if event.key == pygame.K_RIGHT:
                    to_right = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    to_left = False
                if event.key == pygame.K_RIGHT:
                    to_right = False

        if to_right and x_robot < 640 - robot.get_width():
            x_robot += 3
        if to_left and x_robot > 0:
            x_robot -= 3
        robot_rect = robot.get_rect(topleft=(x_robot, y_robot))

        window.fill((0, 0, 0))
        print_text(points)
        for i in rocks:
            window.blit(rock, (i.x, i.y))
            if i.y + rock.get_height() == 480:
                game_is_running = False

            else:
                i.y += 1
                rock_rect = rock.get_rect(topleft=(i.x, i.y))
            if robot_rect.colliderect(rock_rect):
                points += 1
                i.x, i.y = randint(0, 640 - rock.get_width()), -100

        window.blit(robot, (x_robot, y_robot))

        pygame.display.flip()
        clock.tick(60)
