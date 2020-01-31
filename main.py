import pygame
from classes import stats, menu_functions, in_game_functions, in_game_assets_and_stats

# Sets up game stats
frames = 0
stats.title = "geremyspassion"
stats.icon = pygame.image.load("assets/pics/heldie.jpeg")
stats.company_screen = pygame.image.load("assets/pics/Socieyt.png")
stats.menu_background = pygame.image.load("assets/pics/menu_background.png")
stats.title_menu["background"] = stats.menu_background

# Sets up the new window
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

stats.max_width = screen.get_width()
stats.max_height = screen.get_height()
stats.fade_surface = pygame.Surface((stats.max_width, stats.max_height))

# Resize necessary assets
in_game_assets_and_stats.c1_render = pygame.transform.scale(pygame.image.load("assets/characters/character_1/download.jpg"), (int(stats.max_width/8.47), int(stats.max_height/5.294)))
in_game_assets_and_stats.c2_render = pygame.transform.scale(pygame.image.load("assets/characters/character_2/download.jpg"), (int(stats.max_width/8.47), int(stats.max_height/5.294)))
in_game_assets_and_stats.c3_render = pygame.transform.scale(pygame.image.load("assets/characters/character_3/download.jpg"), (int(stats.max_width/8.47), int(stats.max_height/5.294)))
in_game_assets_and_stats.c4_render = pygame.transform.scale(pygame.image.load("assets/characters/character_4/download.jpg"), (int(stats.max_width/8.47), int(stats.max_height/5.294)))
in_game_assets_and_stats.c5_render = pygame.transform.scale(pygame.image.load("assets/characters/character_5/download.jpg"), (int(stats.max_width/8.47), int(stats.max_height/5.294)))
in_game_assets_and_stats.c6_render = pygame.transform.scale(pygame.image.load("assets/characters/character_6/download.jpg"), (int(stats.max_width/8.47), int(stats.max_height/5.294)))




# Stylizes the window
pygame.display.set_caption(stats.title)
pygame.display.set_icon(stats.icon)

# Starts the pygame
pygame.init()
pygame.mixer.init()
stats.intro_music = pygame.mixer.music.load("assets/sounds/intro.ogg")

# big text
stats.big_font = pygame.font.Font("assets/fonts/rockoftimes.otf", int(((stats.max_width + stats.max_height) / 15)))
# medium text
stats.medium_font = pygame.font.Font("assets/fonts/rockoftimes.otf", int(((stats.max_width + stats.max_height) / 22)))
# small text
stats.small_font = pygame.font.Font("assets/fonts/rockoftimes.otf", int(((stats.max_width + stats.max_height) / 40)))

# Start of the game
pygame.mixer.music.play(1)

# Render text



def update():
    global frames
    stats.current_user_pos = stats.selection_cycle[stats.selection_num]
    pygame.time.Clock().tick(60)
    frames += 1
    # print(frames)
    # print(pygame.time.get_ticks())
    pygame.display.update()


# Infinite While loop to keep the game going
while stats.game_running:
    for event in pygame.event.get():
        # Tests to see who can control. 0 = Both
        if stats.controlling_player == 0:
            stats.selection_color = (255, 255, 255)
            menu_functions.test_input_p1(event=event)
            menu_functions.test_input_p2(event=event)
        elif stats.controlling_player == 1:
            stats.selection_color = (255, 0, 0)
            stats.controlling_player_str = "Player 1"
            menu_functions.test_input_p1(event=event)
        elif stats.controlling_player == 2:
            stats.selection_color = (0, 0, 255)
            stats.controlling_player_str = "Player 2"
            menu_functions.test_input_p2(event=event)


    if not stats.item_status.get("intro"):
        menu_functions.intro(window=screen)
    elif not stats.item_status.get("title_menu"):
        menu_functions.draw_menu(name="title_menu", window=screen)
    elif not stats.item_status.get("char_select"):
        menu_functions.draw_menu(name="char_select", window=screen)
    elif not stats.item_status.get("stage_select"):
        menu_functions.draw_menu(name="stage_select", window=screen)
    else:
        in_game_functions.game_time(screen, "small")
    # End of gaame

    update()
