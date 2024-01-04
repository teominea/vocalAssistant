import pygame
import random

player_x = 0
player_y = 0
jump = False
y_change = 0
x_change = 0
player_speed = 0
platforms = []
score = 0
high_score = 0
game_over = False



def main():
    pygame.init()

    global player_x
    global player_y
    global jump
    global y_change
    global x_change
    global player_speed
    global platforms
    global score
    global high_score
    global game_over


    white = (255, 255, 255)
    black = (0, 0, 0)
    gray = (128, 128, 128)
    WIDTH = 400
    HEIGHT = 500
    background = white
    player = pygame.transform.scale(pygame.image.load('doodle-removebg-preview.png'), (80, 60))
    fps = 60
    font = pygame.font.Font('freesansbold.ttf', 16)
    timer = pygame.time.Clock()
    score = 0
    high_score = 0
    game_over = False

    player_x = 170
    player_y = 400
    platforms = [[175, 480, 70, 10], [85, 370, 70, 10], [265, 370, 70, 10], [175, 260, 70, 10], [85, 150, 70, 10],
                 [265, 150, 70, 10], [175, 40, 70, 10]]
    jump = False
    y_change = 0
    x_change = 0
    player_speed = 3

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Doodle Jump")

    def update_player(y_pos):
        global jump
        global y_change
        jump_height = 10
        gravity = .4
        if jump:
            y_change = -jump_height
            jump = False
        y_pos += y_change
        y_change += gravity
        return y_pos

    def update_platforms(platform_list, y_pos, y_vel):
        global score
        if y_pos < 250 and y_vel < 0:
            for i in range(len(platform_list)):
                platform_list[i][1] -= y_vel
        else:
            pass
        for item in range(len(platform_list)):
            if platform_list[item][1] > 500:
                platform_list[item] = [random.randint(10, 320), random.randint(-50, -10), 70, 10]
                score += 1
        return platform_list

    def check_collisions(rect_list, j):
        global player_x
        global player_y
        global y_change
        for i in range(len(rect_list)):
            if rect_list[i].colliderect([player_x + 20, player_y + 60, 35, 5]) and jump == False and y_change > 0:
                j = True
        return j

    running = True
    while running == True:
        timer.tick(fps)
        screen.fill(background)
        screen.blit(player, (player_x, player_y))
        blocks = []
        score_text = font.render("Score: " + str(score), True, black, background)
        screen.blit(score_text, (320, 20))
        high_score_text = font.render("High Score: " + str(high_score), True, black, background)
        screen.blit(high_score_text, (280, 0))

        for i in range(len(platforms)):
            block = pygame.draw.rect(screen, black, platforms[i], 0, 3)
            blocks.append(block)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and game_over:
                    game_over = False
                    score = 0
                    player_x = 170
                    player_y = 400
                    platforms = [[175, 480, 70, 10], [85, 370, 70, 10], [265, 370, 70, 10], [175, 260, 70, 10],
                                 [85, 150, 70, 10], [265, 150, 70, 10], [175, 40, 70, 10]]
                    jump = False
                    y_change = 0
                    x_change = 0
                if event.key == pygame.K_a:
                    x_change = -player_speed
                if event.key == pygame.K_d:
                    x_change = player_speed
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    x_change = 0
                if event.key == pygame.K_d:
                    x_change = 0

        jump = check_collisions(blocks, jump)
        player_x += x_change
        if player_y < 440:
            player_y = update_player(player_y)
        else:
            game_over = True
            y_change = 0
            x_change = 0

        platforms = update_platforms(platforms, player_y, y_change)

        if player_x < -20:
            player_x = -20
        elif player_x > 330:
            player_x = 330

        if x_change > 0:
            player = pygame.transform.scale(pygame.image.load('doodle-removebg-preview.png'), (80, 60))
        elif x_change < 0:
            player = pygame.transform.flip(
                pygame.transform.scale(pygame.image.load('doodle-removebg-preview.png'), (80, 60)), 1, 0)

        if score > high_score:
            high_score = score
        pygame.display.flip()

    pygame.quit()
