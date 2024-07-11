import pygame 
import time
window = pygame.display.set_mode((1024, 600))
score = 0
speed = 5
playerspeed = 5
pygame.font.init()
font = pygame.font.SysFont("Arial", 32)

fps = pygame.time.Clock()


game = True 

def renderText(text):
       return font.render(text, True, (255, 200, 100))

dontwin = renderText("Вы проиграли(")
win = renderText('Winner winner chicken dinner!')   

class platf:
    def __init__(self, y, x, width, length) -> None:
        self.hitbox = pygame.Rect(x, y, width, length)

    def move_1(self):
        kl = pygame.key.get_pressed()
        if kl[pygame.K_w] == True:
            self.hitbox.y -= 5
        if kl[pygame.K_s] == True:
            self.hitbox.y += 5

        if self.hitbox.y > 480:
            self.hitbox.y = 480
        if self.hitbox.y < 0:
            self.hitbox.y = 0

    def move_2(self):
        kl = pygame.key.get_pressed()
        if kl[pygame.K_UP] == True:
            self.hitbox.y -= 5
        if kl[pygame.K_DOWN] == True:
            self.hitbox.y += 5

        if self.hitbox.y > 480:
            self.hitbox.y = 480
        if self.hitbox.y < 0:
            self.hitbox.y = 0

    def collisions(self):
        if self.hitbox.colliderect(Ball.hitbox):
            print("connect")


class ball:
    def __init__(self, y, x, width, length, speed) -> None:
        self.hitbox = pygame.Rect(x, y, width, length)
        self.speedx = speed
        self.speedy = speed
    def move_b():
        Ball.hitbox.x += Ball.speedx
        Ball.hitbox.y += Ball.speedy
        if Ball.hitbox.colliderect(player.hitbox) or Ball.hitbox.colliderect(sharfi.hitbox):
            Ball.speedx = -Ball.speedx
            Ball.speedy = -Ball.speedy
        if Ball.hitbox.bottom > 600 or Ball.hitbox.top < 0:
            Ball.speedy = -Ball.speedy
 
   
         
            



player = platf(128, 64, 32, 128)

sharfi = platf(128, 896, 32, 128)

Ball = ball(224, 448, 32, 32, 2)

def reset():
    global score, player, sharfi, Ball

    player = platf(128, 64, 32, 128)

    sharfi = platf(128, 896, 32, 128)

    Ball = ball(224, 448, 32, 32, 2)

    score = 0

while game:
    window.fill("yellow")


    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            game = False

    player.move_1()
    sharfi.move_2()
    ball.move_b()
    pygame.draw.rect(window, "blue", (player.hitbox))  
    pygame.draw.rect(window, "red", (sharfi.hitbox))  
    pygame.draw.rect(window, "black", (Ball.hitbox))  
    def pigscoredef():
        global score
        if Ball.hitbox.colliderect(player.hitbox) or Ball.hitbox.colliderect(sharfi.hitbox):
            score += 1


    def img():
        if Ball.hitbox.x > 1024 or Ball.hitbox.x < 0:
            window.blit(dontwin, (260, 70))
            
        if Ball.hitbox.x > 1024 or Ball.hitbox.x < 0:
            window.blit(win, (260, 70))
            Ball.speedx = 0
        pigscoreimg = renderText("Счёт: " + str(score))
        window.blit(pigscoreimg, (400, 5))
    pigscoredef()
    img()
    fps.tick(128)

    pygame.display.update()






