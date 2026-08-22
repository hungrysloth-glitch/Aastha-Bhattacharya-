import pygame
import random

def sprites():

    player_image = pygame.image.load("blobby.PNG").convert_alpha()
    player_image = pygame.transform.scale(player_image, (75, 75))

    sharky_image = pygame.image.load("sharky.png").convert_alpha()
    sharky_image = pygame.transform.scale(sharky_image,(90, 90))

    background_image = pygame.image.load("background.PNG").convert()
    background_image = pygame.transform.scale(background_image,(720, 1280))

    return player_image, sharky_image, background_image


def obstacles(obstacle_list, sharky_image, screen):

    sharky_rect = sharky_image.get_rect()

    sharky_rect.x = random.randint(0, (screen.get_width() - sharky_rect.width))

    sharky_rect.y = -sharky_rect.height
    obstacle_list.append(sharky_rect)


def player(player_pos, player_rect, screen, dt):

    keys = pygame.key.get_pressed()

    speed = 350

    if keys[pygame.K_w]:
        player_pos.y -= speed * dt

    if keys[pygame.K_s]:
        player_pos.y += speed * dt

    if keys[pygame.K_a]:
        player_pos.x -= speed * dt

    if keys[pygame.K_d]:
        player_pos.x += speed * dt

    player_rect.center = (round(player_pos.x), round(player_pos.y))

    player_rect.clamp_ip(screen.get_rect())

    player_pos.x = player_rect.centerx
    player_pos.y = player_rect.centery

def format_time(seconds):

    minutes = int(seconds // 60)
    seconds = int(seconds % 60)

    if minutes > 0:
        return f"{minutes} minute{'s' if minutes != 1 else ''} and {seconds} second{'s' if seconds != 1 else ''}"

    return f"{seconds} second{'s' if seconds != 1 else ''}"

def game_menu(screen, clock, game_over=False, survival_time=0):

    font = pygame.font.SysFont("Comic Sans MS", 70, bold=True)
    small_font = pygame.font.SysFont("Comic Sans MS", 40)

    while True:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return "quit"

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return "start"
                if event.key == pygame.K_x:
                    return "quit"

        screen.fill("midnightblue")

        if game_over:
            title = font.render("GAME OVER", True, "lightblue")
            message = small_font.render("Press SPACE to restart", True, "lightblue")
            survival_message = small_font.render(f"You survived for {format_time(survival_time)}.", True, "lightblue")
            survival_rect = survival_message.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + 70))
            screen.blit(survival_message, survival_rect)

        else:
            title = font.render("Sharky Dodger", True, "lightblue")
            message = small_font.render("Press SPACE to start", True, "lightblue")
            quit_y = screen.get_height()

        quit_message = small_font.render("Press X to quit", True, "lightblue")
        title_rect = title.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 - 60))
        message_rect = message.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + 20))
        quit_rect = quit_message.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + 120))

        screen.blit(title, title_rect)
        screen.blit(message, message_rect)
        screen.blit(quit_message, quit_rect)

        pygame.display.flip()

        clock.tick(60)

def main():

    pygame.init()
    screen = pygame.display.set_mode((720, 800))
    pygame.display.set_caption("Sharky Dodger")
    clock = pygame.time.Clock()

    player_image, sharky_image, background_image = sprites()

    menu_result = game_menu(screen,clock)

    if menu_result == "quit":
        pygame.quit()
        return

    running = True
    while running:

        player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
        player_rect = player_image.get_rect()
        player_rect.center = (round(player_pos.x), round(player_pos.y))

        obstacle_list = []
        obstacle_speed = 400
        spawn_timer = 0
        spawn_delay = 0.5

        playing = True
        start_time = pygame.time.get_ticks()

        while playing:

            dt = clock.tick(60) / 1000
            dt = min(dt, 0.1)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

            screen.blit(background_image, (0, 0))

            player(player_pos, player_rect, screen, dt)

            spawn_timer += dt
            if spawn_timer >= spawn_delay:
                obstacles(obstacle_list, sharky_image, screen)
                spawn_timer = 0

            for obstacle in obstacle_list:
                obstacle.y += obstacle_speed * dt

            obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.top < screen.get_height()]
            player_hitbox = player_rect.inflate(-30, -30)
 
            for obstacle in obstacle_list:
                shark_hitbox = obstacle.inflate(-25, -25)
                if player_rect.colliderect(shark_hitbox):
                    survival_time = (pygame.time.get_ticks() - start_time) / 1000
                    playing = False

            for obstacle in obstacle_list:
                screen.blit(sharky_image, obstacle)

            screen.blit(player_image, player_rect)

            pygame.display.flip()

        menu_result = game_menu(screen, clock, game_over=True, survival_time=survival_time)

        if menu_result == "quit":
            running = False

        elif menu_result == "start":
            continue

    pygame.quit()

main()
