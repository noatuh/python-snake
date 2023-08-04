import pygame
import random
import sys

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# This class represents the snake
class Snake(object):
    def __init__(self):
        self.position = [100,50]
        self.body = [[100,50], [90,50], [80,50]]
        self.direction = "RIGHT"

    def changeDirection(self, direction):
        self.direction = direction

    def move(self, foodPos):
        if self.direction == "RIGHT":
            self.position[0] += 10
        elif self.direction == "LEFT":
            self.position[0] -= 10
        elif self.direction == "UP":
            self.position[1] -= 10
        elif self.direction == "DOWN":
            self.position[1] += 10
        self.body.insert(0, list(self.position))
        if self.position == foodPos:
            return 1
        else:
            self.body.pop()
            return 0

    def checkCollision(self):
        if self.position[0] > 490 or self.position[0] < 0:
            return 1
        elif self.position[1] > 490 or self.position[1] < 0:
            return 1
        for bodyPart in self.body[1:]:
            if self.position == bodyPart:
                return 1
        return 0

    def getHeadPos(self):
        return self.position

# This class represents the food that the snake needs to eat
class Food(object):
    def __init__(self):
        self.position = [random.randrange(1, 50) * 10, random.randrange(1, 50) * 10]
        self.isFoodOnScreen = True

    def spawnFood(self, snake):
        if self.isFoodOnScreen == False:
            while True:
                self.position = [random.randrange(1, 50) * 10, random.randrange(1, 50) * 10]
                if self.position not in snake.body:
                    break
            self.isFoodOnScreen = True
        return self.position

    def setFoodOnScreen(self, b):
        self.isFoodOnScreen = b

window = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Snake Game')

fps = pygame.time.Clock()

score = 0

snake = Snake()
food = Food()

def gameOver():
    pygame.quit()
    sys.exit()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.changeDirection("UP")
            if event.key == pygame.K_DOWN:
                snake.changeDirection("DOWN")
            if event.key == pygame.K_LEFT:
                snake.changeDirection("LEFT")
            if event.key == pygame.K_RIGHT:
                snake.changeDirection("RIGHT")

    foodPos = food.spawnFood(snake)
    if snake.move(foodPos) == 1:
        score += 1
        food.setFoodOnScreen(False)

    window.fill(BLACK)

    for pos in snake.body:
        pygame.draw.rect(window, WHITE, pygame.Rect(pos[0], pos[1], 10, 10))

    pygame.draw.rect(window, WHITE, pygame.Rect(foodPos[0], foodPos[1], 10, 10))

    if snake.checkCollision() == 1:
        gameOver()

    pygame.display.set_caption("Score: " + str(score))
    pygame.display.flip()

    fps.tick(24)
