from classes import stats, in_game_assets_and_stats
import pygame


def test_input_p1(event):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            stats.game_running = False
        if event.key == pygame.K_t:
            print("aie_p1")
            if stats.current_screen == "title_menu":
                if stats.current_user_pos == "back":
                    stats.game_running = False
                if stats.current_user_pos == "next":
                    stats.black_transition = 300
                    stats.controlling_player = 1
                    stats.item_status["title_menu"] = True
                    stats.selection_num = 6
            if stats.current_screen == "char_select":
                if stats.current_user_pos == "back":
                    stats.controlling_player = 0
                    stats.black_transition = 300
                    stats.selection_num = 6
                    stats.item_status["title_menu"] = False
                if stats.current_user_pos == "next" and len(in_game_assets_and_stats.p1_cycle) >= 2:
                    if stats.controlling_player == 1:
                        stats.selection_num = 6
                        # Passes control over to the other player
                        stats.controlling_player = 2
                if len(in_game_assets_and_stats.p1_cycle) < 2:
                    if stats.current_user_pos == "option_1" and in_game_assets_and_stats.c1_available:
                        in_game_assets_and_stats.p1_cycle.append("character_1")
                        in_game_assets_and_stats.c1_available = False
                    if stats.current_user_pos == "option_2" and in_game_assets_and_stats.c2_available:
                        in_game_assets_and_stats.p1_cycle.append("character_2")
                        in_game_assets_and_stats.c2_available = False
                    if stats.current_user_pos == "option_3" and in_game_assets_and_stats.c3_available:
                        in_game_assets_and_stats.p1_cycle.append("character_3")
                        in_game_assets_and_stats.c3_available = False
                    if stats.current_user_pos == "option_4" and in_game_assets_and_stats.c4_available:
                        in_game_assets_and_stats.p1_cycle.append("character_4")
                        in_game_assets_and_stats.c4_available = False
                    if stats.current_user_pos == "option_5" and in_game_assets_and_stats.c5_available:
                        in_game_assets_and_stats.p1_cycle.append("character_5")
                        in_game_assets_and_stats.c5_available = False
                    if stats.current_user_pos == "option_6" and in_game_assets_and_stats.c6_available:
                        in_game_assets_and_stats.p1_cycle.append("character_6")
                        in_game_assets_and_stats.c6_available = False

            if stats.current_screen == "stage_select":
                if stats.current_user_pos == "back":
                    stats.black_transition = 300
                    stats.item_status["char_select"] = False
                if stats.current_user_pos == "next" and stats.stage_size is not None:
                    stats.game_playing = True
                    stats.black_transition = 900
                    stats.item_status["stage_select"] = True
                if stats.current_user_pos == "option_4":
                    stats.stage_size = "small"
                if stats.current_user_pos == "option_5":
                    stats.stage_size = "medium"
                if stats.current_user_pos == "option_6":
                    stats.stage_size = "large"

        if event.key == pygame.K_y:
            print("bie_p1")
        if event.key == pygame.K_a:
            print("leftie_p1")
            if stats.current_screen == "title_menu":
                if stats.selection_num > 6:
                    stats.selection_num -= 1
                else:
                    stats.selection_num = (len(stats.selection_cycle) - 1)
            elif stats.current_screen == "char_select":
                if stats.selection_num > 0:
                    stats.selection_num -= 1
                else:
                    stats.selection_num = (len(stats.selection_cycle) - 1)
            elif stats.current_screen == "stage_select":
                if stats.selection_num > 3:
                    stats.selection_num -= 1
                else:
                    stats.selection_num = (len(stats.selection_cycle) - 1)
        if event.key == pygame.K_d:
            print("rightie_p1")
            if stats.current_screen == "title_menu":
                if stats.selection_num < 8:
                    stats.selection_num += 1
                else:
                    stats.selection_num = 6
            elif stats.current_screen == "char_select":
                if stats.selection_num < 8:
                    stats.selection_num += 1
                else:
                    stats.selection_num = 0
            elif stats.current_screen == "stage_select":
                if stats.selection_num < 8:
                    stats.selection_num += 1
                else:
                    stats.selection_num = 3
        if event.key == pygame.K_w:
            print("uppie_p1")
            if stats.current_screen == "char_select":
                if stats.selection_num > 2:
                    stats.selection_num -= 3
            if stats.current_screen == "stage_select":
                if stats.selection_num > 5:
                    stats.selection_num -= 3
        if event.key == pygame.K_s:
            print("downie_p1")
            if stats.current_screen == "char_select":
                if stats.selection_num < 6:
                    stats.selection_num += 3
            if stats.current_screen == "stage_select":
                if stats.selection_num < 6:
                    stats.selection_num += 3


def test_input_p2(event):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            stats.game_running = False
        if event.key == pygame.K_p:
            print("aie_p2")
            if stats.current_screen == "title_menu":
                if stats.current_user_pos == "back":
                    stats.game_running = False
                if stats.current_user_pos == "next":
                    stats.black_transition = 300
                    stats.controlling_player = 1
                    stats.item_status["title_menu"] = True
                    stats.selection_num = 6
            if stats.current_screen == "char_select":
                if stats.current_user_pos == "back":
                    stats.controlling_player = 0
                    stats.black_transition = 300
                    stats.selection_num = 6
                    stats.item_status["title_menu"] = False
                if stats.current_user_pos == "next" and len(in_game_assets_and_stats.p2_cycle) >= 2:
                    if stats.controlling_player == 2:
                        stats.controlling_player = 0
                        stats.selection_num = 6
                        stats.item_status["char_select"] = True
                if len(in_game_assets_and_stats.p2_cycle) < 2:
                    if stats.current_user_pos == "option_1" and in_game_assets_and_stats.c1_available:
                        in_game_assets_and_stats.p2_cycle.append("character_1")
                        in_game_assets_and_stats.c1_available = False
                    if stats.current_user_pos == "option_2" and in_game_assets_and_stats.c2_available:
                        in_game_assets_and_stats.p2_cycle.append("character_2")
                        in_game_assets_and_stats.c2_available = False
                    if stats.current_user_pos == "option_3" and in_game_assets_and_stats.c3_available:
                        in_game_assets_and_stats.p2_cycle.append("character_3")
                        in_game_assets_and_stats.c3_available = False
                    if stats.current_user_pos == "option_4" and in_game_assets_and_stats.c4_available:
                        in_game_assets_and_stats.p2_cycle.append("character_4")
                        in_game_assets_and_stats.c4_available = False
                    if stats.current_user_pos == "option_5" and in_game_assets_and_stats.c5_available:
                        in_game_assets_and_stats.p2_cycle.append("character_5")
                        in_game_assets_and_stats.c5_available = False
                    if stats.current_user_pos == "option_6" and in_game_assets_and_stats.c6_available:
                        in_game_assets_and_stats.p2_cycle.append("character_6")
                        in_game_assets_and_stats.c6_available = False

            if stats.current_screen == "stage_select":
                if stats.current_user_pos == "back":
                    stats.black_transition = 300
                    stats.item_status["char_select"] = False
                if stats.current_user_pos == "next" and stats.stage_size is not None:
                    stats.game_playing = True
                    stats.black_transition = 900
                    stats.item_status["stage_select"] = True
                if stats.current_user_pos == "option_4":
                    stats.stage_size = "small"
                if stats.current_user_pos == "option_5":
                    stats.stage_size = "medium"
                if stats.current_user_pos == "option_6":
                    stats.stage_size = "large"

        if event.key == pygame.K_KP3:
            print("bie_p2")
        if event.key == pygame.K_LEFT:
            print("leftie_p2")
            if stats.current_screen == "title_menu":
                if stats.selection_num > 6:
                    stats.selection_num -= 1
                else:
                    stats.selection_num = (len(stats.selection_cycle) - 1)
            elif stats.current_screen == "char_select":
                if stats.selection_num > 0:
                    stats.selection_num -= 1
                else:
                    stats.selection_num = (len(stats.selection_cycle) - 1)
            elif stats.current_screen == "stage_select":
                if stats.selection_num > 3:
                    stats.selection_num -= 1
                else:
                    stats.selection_num = (len(stats.selection_cycle) - 1)
        if event.key == pygame.K_RIGHT:
            print("rightie_p2")
            if stats.current_screen == "title_menu":
                if stats.selection_num < 8:
                    stats.selection_num += 1
                else:
                    stats.selection_num = 6
            elif stats.current_screen == "char_select":
                if stats.selection_num < 8:
                    stats.selection_num += 1
                else:
                    stats.selection_num = 0
            elif stats.current_screen == "stage_select":
                if stats.selection_num < 8:
                    stats.selection_num += 1
                else:
                    stats.selection_num = 3
        if event.key == pygame.K_UP:
            print("uppie_p2")
            if stats.current_screen == "char_select":
                if stats.selection_num > 2:
                    stats.selection_num -= 3
            if stats.current_screen == "stage_select":
                if stats.selection_num > 2:
                    stats.selection_num -= 3
        if event.key == pygame.K_DOWN:
            print("downie_p2")
            if stats.current_screen == "char_select":
                if stats.selection_num < 6:
                    stats.selection_num += 3
            if stats.current_screen == "stage_select":
                if stats.selection_num < 6:
                    stats.selection_num += 3


def fade(surface, speed, directions, window):
    surface_resized = pygame.transform.scale(surface, (stats.max_width, stats.max_height))
    window.blit(surface_resized, (0, 0))
    stats.fade_surface.fill((0, 0, 0))
    stats.fade_surface.set_alpha(stats.black_transition)
    window.blit(stats.fade_surface, (0, 0))
    if stats.fade_direction == "in" and stats.black_transition > 1:
        # print("im in 1")
        stats.black_transition -= speed
        return True
    if stats.fade_direction == "in" and stats.black_transition <= 1:
        # print("im in 2")
        if directions == "both":
            pygame.time.wait(speed*1000)
            stats.fade_direction = "out"
        else:
            return False
    if stats.fade_direction == "out" and stats.black_transition > 301:
        # print("im in 3")
        stats.fade_direction = "in"
        return False
    if stats.fade_direction == "out":
        # print("im in 4")
        stats.black_transition += speed
        return True


def tint(picture, color):
    picture = picture.copy()
    picture.fill(color[0:3] + (0,), None, pygame.BLEND_RGBA_MULT)
    return picture


def draw_menu(name, window):
    # Tests which menu to draw
    if name == "title_menu":
        stats.current_screen = "title_menu"
        fade(surface=set_up_title(), speed=4, directions="in", window=window)
    if name == "char_select":
        stats.current_screen = "char_select"
        fade(surface=set_up_char_select(), speed=4, directions="in", window=window)
    if name == "stage_select":
        stats.current_screen = "stage_select"
        fade(surface=set_up_stage_select(), speed=4, directions="in", window=window)


def intro(window):
    if stats.company_fade_run:
        stats.company_fade_run = fade(surface=stats.company_screen, speed=3, directions="both", window=window)
    elif stats.title_fade_run:
        stats.title_fade_run = fade(surface=stats.icon, speed=3, directions="both", window=window)
        if not stats.title_fade_run:
            stats.item_status["intro"] = True


def set_up_title():
    # main_content box
    menu_surface = pygame.Surface((stats.max_width, stats.max_height))
    picture_resized = pygame.transform.scale(stats.menu_background, (stats.max_width, stats.max_height))
    menu_surface.blit(picture_resized, (0, 0))

    temp_x = int(stats.max_width / 16)
    temp_y = int(stats.max_height / 9)
    temp_width = int(stats.max_width / 1.1425)
    temp_height = int(stats.max_height / 2.25)
    stats.title_menu["main_content"] = pygame.draw.rect(menu_surface, (0, 0, 0), (temp_x, temp_y, temp_width, temp_height), 0)
    # Title blit
    text = stats.big_font.render("Haha Funnie", 1, (255, 255, 255))
    text2 = stats.big_font.render("The Gamie", 1, (255, 255, 255))
    menu_surface.blit(text, (int((temp_x / 2) + ((temp_width / 2) - (text.get_width() / 2.2))), int((temp_y / 2) + ((temp_height / 2.2) - (text.get_height() / 2)))))
    menu_surface.blit(text2, (int((temp_x / 2) + ((temp_width / 2) - (text2.get_width() / 2.2))), int((temp_y / 2) + ((temp_height / 1.2) - (text2.get_height() / 2)))))

    # back box
    temp_x = int(stats.max_width / 16)
    temp_y = int(stats.max_height / 1.636)
    temp_width = int(stats.max_width / 3.695)
    temp_height = int(stats.max_height / 4.5)
    # Test the selection
    if stats.current_user_pos == "back":
        stats.selection_box = pygame.draw.rect(menu_surface, stats.selection_color, (temp_x-(stats.max_width/64), temp_y-(stats.max_height/51.2), temp_width+(stats.max_width/32), temp_height+(stats.max_height/25.6)), 0)
    stats.title_menu["back"] = pygame.draw.rect(menu_surface, (0, 0, 0), (temp_x, temp_y, temp_width, temp_height), 0)
    # quit blit
    temp_text = stats.medium_font.render("Quit", 1, (255, 255, 255))
    menu_surface.blit(temp_text, (int((temp_x / 2) + ((temp_width / 2) - (temp_text.get_width() / 3))), int((temp_y / 2) + ((temp_height / 0.45) - (temp_text.get_height() / 1)))))

    # next box
    temp_x = int(stats.max_width / 1.5)
    temp_y = int(stats.max_height / 1.636)
    temp_width = int(stats.max_width / 3.695)
    temp_height = int(stats.max_height / 4.5)
    # Test the selection
    if stats.current_user_pos == "next":
        stats.selection_box = pygame.draw.rect(menu_surface, stats.selection_color, (temp_x-(stats.max_width/64), temp_y-(stats.max_height/51.2), temp_width+(stats.max_width/32), temp_height+(stats.max_height/25.6)), 0)
    stats.title_menu["next"] = pygame.draw.rect(menu_surface, (0, 0, 0), (temp_x, temp_y, temp_width, temp_height), 0)
    # start blit
    temp_text = stats.medium_font.render("Start", 1, (255, 255, 255))
    menu_surface.blit(temp_text, (int((temp_x / 1) + ((temp_width / 2) - (temp_text.get_width() / 2))), int((temp_y / 2) + ((temp_height / 0.45) - (temp_text.get_height() / 1)))))

    # other box
    temp_x = int(stats.max_width / 2.744)
    temp_y = int(stats.max_height / 1.285)
    temp_width = int(stats.max_width / 3.695)
    temp_height = int(stats.max_height / 9)
    # Test the selection
    if stats.current_user_pos == "other":
        stats.selection_box = pygame.draw.rect(menu_surface, stats.selection_color, (temp_x-(stats.max_width/64), temp_y-(stats.max_height/51.2), temp_width+(stats.max_width/32), temp_height+(stats.max_height/25.6)), 0)
    stats.title_menu["other"] = pygame.draw.rect(menu_surface, (0, 0, 0), (temp_x, temp_y, temp_width, temp_height), 0)
    # credits blit
    temp_text = stats.small_font.render("Credits", 1, (255, 255, 255))
    menu_surface.blit(temp_text, (int((temp_x / 1) + ((temp_width / 2) - (temp_text.get_width() / 2))), int((temp_y / 2) + ((temp_height / 0.263) - (temp_text.get_height() / 10)))))

    return menu_surface


def set_up_char_select():
    # main_content box
    menu_surface = pygame.Surface((stats.max_width, stats.max_height))
    picture_resized = pygame.transform.scale(stats.menu_background, (stats.max_width, stats.max_height))
    menu_surface.blit(picture_resized, (0, 0))

    temp_x = int(stats.max_width / 16)
    temp_y = int(stats.max_height / 9)
    temp_width = int(stats.max_width / 1.1425)
    temp_height = int(stats.max_height / 2.25)
    stats.char_menu["main_content"] = pygame.draw.rect(menu_surface, (0, 0, 0), (temp_x, temp_y, temp_width, temp_height), 0)

    character_list(menu_surface)

    # back box
    temp_x = int(stats.max_width / 16)
    temp_y = int(stats.max_height / 1.636)
    temp_width = int(stats.max_width / 3.695)
    temp_height = int(stats.max_height / 4.5)
    # Test the selection
    if stats.current_user_pos == "back":
        stats.selection_box = pygame.draw.rect(menu_surface, stats.selection_color, (temp_x-(stats.max_width/64), temp_y-(stats.max_height/51.2), temp_width+(stats.max_width/32), temp_height+(stats.max_height/25.6)), 0)
    stats.char_menu["back"] = pygame.draw.rect(menu_surface, (0, 0, 0), (temp_x, temp_y, temp_width, temp_height), 0)
    # back blit
    temp_text = stats.medium_font.render("Back", 1, (255, 255, 255))
    menu_surface.blit(temp_text, (int((temp_x / 2) + ((temp_width / 2) - (temp_text.get_width() / 3))), int((temp_y / 2) + ((temp_height / 0.45) - (temp_text.get_height() / 1)))))

    # next box
    temp_x = int(stats.max_width / 1.5)
    temp_y = int(stats.max_height / 1.636)
    temp_width = int(stats.max_width / 3.695)
    temp_height = int(stats.max_height / 4.5)
    # Test the selection
    if stats.current_user_pos == "next":
        stats.selection_box = pygame.draw.rect(menu_surface, stats.selection_color, (temp_x-(stats.max_width/64), temp_y-(stats.max_height/51.2), temp_width+(stats.max_width/32), temp_height+(stats.max_height/25.6)), 0)
    stats.char_menu["next"] = pygame.draw.rect(menu_surface, (0, 0, 0), (temp_x, temp_y, temp_width, temp_height), 0)
    # next blit
    temp_text = stats.medium_font.render("Next", 1, (255, 255, 255))
    menu_surface.blit(temp_text, (int((temp_x / 1) + ((temp_width / 2) - (temp_text.get_width() / 2))), int((temp_y / 2) + ((temp_height / 0.45) - (temp_text.get_height() / 1)))))

    # other box
    temp_x = int(stats.max_width / 2.744)
    temp_y = int(stats.max_height / 1.285)
    temp_width = int(stats.max_width / 3.695)
    temp_height = int(stats.max_height / 9)
    # Test the selection
    if stats.current_user_pos == "other":
        stats.selection_box = pygame.draw.rect(menu_surface, stats.selection_color, (temp_x-(stats.max_width/64), temp_y-(stats.max_height/51.2), temp_width+(stats.max_width/32), temp_height+(stats.max_height/25.6)), 0)
    stats.char_menu["other"] = pygame.draw.rect(menu_surface, (0, 0, 0), (temp_x, temp_y, temp_width, temp_height), 0)
    # Current Player blit
    temp_text = stats.small_font.render(stats.controlling_player_str, 1, stats.selection_color)
    menu_surface.blit(temp_text, (int((temp_x / 1) + ((temp_width / 2) - (temp_text.get_width() / 2))), int((temp_y / 2) + ((temp_height / 0.263) - (temp_text.get_height() / 10)))))

    return menu_surface


def character_list(menu_surface):
    # Player 1 Zone
    temp_x = int(stats.max_width / 16)
    temp_y = int(stats.max_height / 9)
    temp_width = int((stats.max_width / 1.1425) / 2)
    temp_height = int(stats.max_height / 2.25)
    pygame.draw.rect(menu_surface, (127, 0, 0), (temp_x, temp_y, temp_width, temp_height), 0)

    # Character 1
    # Test the selection
    in_game_assets_and_stats.temp_render = in_game_assets_and_stats.c1_render
    if stats.current_user_pos == "option_1" and stats.controlling_player == 1:
        stats.selection_box = pygame.draw.rect(menu_surface, stats.selection_color, (temp_x, temp_y, (stats.max_width/6.857), (stats.max_height/4.286)), 0)
    if not in_game_assets_and_stats.c1_available and "character_1" in in_game_assets_and_stats.p1_cycle:
        in_game_assets_and_stats.temp_render = tint(in_game_assets_and_stats.c1_render, (255, 0, 0))
    elif not in_game_assets_and_stats.c1_available and "character_1" in in_game_assets_and_stats.p2_cycle:
        in_game_assets_and_stats.temp_render = tint(in_game_assets_and_stats.c1_render, (0, 0, 255))
    menu_surface.blit(in_game_assets_and_stats.temp_render, (int(temp_x + (stats.max_width / 72)), int(temp_y + (stats.max_height / 45))))

    # Character 2
    # Test the selection
    in_game_assets_and_stats.temp_render = in_game_assets_and_stats.c2_render
    if stats.current_user_pos == "option_2" and stats.controlling_player == 1:
        stats.selection_box = pygame.draw.rect(menu_surface, stats.selection_color, (temp_x+(stats.max_width/6.857), temp_y, (stats.max_width/6.857), (stats.max_height/4.286)), 0)
    if not in_game_assets_and_stats.c2_available and "character_2" in in_game_assets_and_stats.p1_cycle:
        in_game_assets_and_stats.temp_render = tint(in_game_assets_and_stats.c2_render, (255, 0, 0))
    elif not in_game_assets_and_stats.c2_available and "character_2" in in_game_assets_and_stats.p2_cycle:
        in_game_assets_and_stats.temp_render = tint(in_game_assets_and_stats.c2_render, (0, 0, 255))
    menu_surface.blit(in_game_assets_and_stats.temp_render, (int(temp_x+(stats.max_width/6.26)), int(temp_y+(stats.max_height/45))))

    # Character 3
    # Test the selection
    in_game_assets_and_stats.temp_render = in_game_assets_and_stats.c3_render
    if stats.current_user_pos == "option_3" and stats.controlling_player == 1:
        stats.selection_box = pygame.draw.rect(menu_surface, stats.selection_color, (temp_x+(2*(stats.max_width/6.857)), temp_y, (stats.max_width/6.857), (stats.max_height/4.286)), 0)
    if not in_game_assets_and_stats.c3_available and "character_3" in in_game_assets_and_stats.p1_cycle:
        in_game_assets_and_stats.temp_render = tint(in_game_assets_and_stats.c3_render, (255, 0, 0))
    elif not in_game_assets_and_stats.c3_available and "character_3" in in_game_assets_and_stats.p2_cycle:
        in_game_assets_and_stats.temp_render = tint(in_game_assets_and_stats.c3_render, (0, 0, 255))
    menu_surface.blit(in_game_assets_and_stats.temp_render, (int(temp_x+(stats.max_width/3.272)), int(temp_y+(stats.max_height/45))))

    # Character 4
    # Test the selection
    in_game_assets_and_stats.temp_render = in_game_assets_and_stats.c4_render
    if stats.current_user_pos == "option_4" and stats.controlling_player == 1:
        stats.selection_box = pygame.draw.rect(menu_surface, stats.selection_color, (temp_x, temp_y+(stats.max_height/4.737), (stats.max_width/6.857), (stats.max_height/4.286)), 0)
    if not in_game_assets_and_stats.c4_available and "character_4" in in_game_assets_and_stats.p1_cycle:
        in_game_assets_and_stats.temp_render = tint(in_game_assets_and_stats.c4_render, (255, 0, 0))
    elif not in_game_assets_and_stats.c4_available and "character_4" in in_game_assets_and_stats.p2_cycle:
        in_game_assets_and_stats.temp_render = tint(in_game_assets_and_stats.c4_render, (0, 0, 255))
    menu_surface.blit(in_game_assets_and_stats.temp_render, (int(temp_x+(stats.max_width/72)), int(temp_y+(stats.max_height/4.286))))

    # Character 5
    # Test the selection
    in_game_assets_and_stats.temp_render = in_game_assets_and_stats.c5_render
    if stats.current_user_pos == "option_5" and stats.controlling_player == 1:
        stats.selection_box = pygame.draw.rect(menu_surface, stats.selection_color, (temp_x+(stats.max_width/6.857), temp_y+(stats.max_height/4.737), (stats.max_width/6.857), (stats.max_height/4.286)), 0)
    if not in_game_assets_and_stats.c5_available and "character_5" in in_game_assets_and_stats.p1_cycle:
        in_game_assets_and_stats.temp_render = tint(in_game_assets_and_stats.c5_render, (255, 0, 0))
    elif not in_game_assets_and_stats.c5_available and "character_5" in in_game_assets_and_stats.p2_cycle:
        in_game_assets_and_stats.temp_render = tint(in_game_assets_and_stats.c5_render, (0, 0, 255))
    menu_surface.blit(in_game_assets_and_stats.temp_render, (int(temp_x+(stats.max_width/6.26)), int(temp_y+(stats.max_height/4.286))))

    # Character 6
    # Test the selection
    in_game_assets_and_stats.temp_render = in_game_assets_and_stats.c6_render
    if stats.current_user_pos == "option_6" and stats.controlling_player == 1:
        stats.selection_box = pygame.draw.rect(menu_surface, stats.selection_color, (temp_x+(2*(stats.max_width/6.857)), temp_y+(stats.max_height/4.737), (stats.max_width/6.857), (stats.max_height/4.286)), 0)
    if not in_game_assets_and_stats.c6_available and "character_6" in in_game_assets_and_stats.p1_cycle:
        in_game_assets_and_stats.temp_render = tint(in_game_assets_and_stats.c6_render, (255, 0, 0))
    elif not in_game_assets_and_stats.c6_available and "character_6" in in_game_assets_and_stats.p2_cycle:
        in_game_assets_and_stats.temp_render = tint(in_game_assets_and_stats.c6_render, (0, 0, 255))
    menu_surface.blit(in_game_assets_and_stats.temp_render, (int(temp_x+(stats.max_width/3.272)), int(temp_y+(stats.max_height/4.286))))


    # Player 2 Zone
    temp_x = int((stats.max_width / 16) + int((stats.max_width / 1.1425) / 2))
    temp_y = int(stats.max_height / 9)
    temp_width = int((stats.max_width / 1.1425) / 2)
    temp_height = int(stats.max_height / 2.25)
    pygame.draw.rect(menu_surface, (0, 0, 127), (temp_x, temp_y, temp_width, temp_height), 0)

    # Character 1
    # Test the selection
    in_game_assets_and_stats.temp_render = in_game_assets_and_stats.c1_render
    if stats.current_user_pos == "option_1" and stats.controlling_player == 2:
        stats.selection_box = pygame.draw.rect(menu_surface, stats.selection_color, (temp_x, temp_y, (stats.max_width/6.857), (stats.max_height/4.286)), 0)
    if not in_game_assets_and_stats.c1_available and "character_1" in in_game_assets_and_stats.p1_cycle:
        in_game_assets_and_stats.temp_render = tint(in_game_assets_and_stats.c1_render, (255, 0, 0))
    elif not in_game_assets_and_stats.c1_available and "character_1" in in_game_assets_and_stats.p2_cycle:
        in_game_assets_and_stats.temp_render = tint(in_game_assets_and_stats.c1_render, (0, 0, 255))
    menu_surface.blit(in_game_assets_and_stats.temp_render, (int(temp_x+(stats.max_width/72)), int(temp_y+(stats.max_height/45))))

    # Character 2
    # Test the selection
    in_game_assets_and_stats.temp_render = in_game_assets_and_stats.c2_render
    if stats.current_user_pos == "option_2" and stats.controlling_player == 2:
        stats.selection_box = pygame.draw.rect(menu_surface, stats.selection_color, (temp_x+(stats.max_width/6.857), temp_y, (stats.max_width/6.857), (stats.max_height/4.286)), 0)
    if not in_game_assets_and_stats.c2_available and "character_2" in in_game_assets_and_stats.p1_cycle:
        in_game_assets_and_stats.temp_render = tint(in_game_assets_and_stats.c2_render, (255, 0, 0))
    elif not in_game_assets_and_stats.c2_available and "character_2" in in_game_assets_and_stats.p2_cycle:
        in_game_assets_and_stats.temp_render = tint(in_game_assets_and_stats.c2_render, (0, 0, 255))
    menu_surface.blit(in_game_assets_and_stats.temp_render, (int(temp_x+(stats.max_width/6.26)), int(temp_y+(stats.max_height/45))))

    # Character 3
    # Test the selection
    in_game_assets_and_stats.temp_render = in_game_assets_and_stats.c3_render
    if stats.current_user_pos == "option_3" and stats.controlling_player == 2:
        stats.selection_box = pygame.draw.rect(menu_surface, stats.selection_color, (temp_x+(2*(stats.max_width/6.857)), temp_y, (stats.max_width/6.857), (stats.max_height/4.286)), 0)
    if not in_game_assets_and_stats.c3_available and "character_3" in in_game_assets_and_stats.p1_cycle:
        in_game_assets_and_stats.temp_render = tint(in_game_assets_and_stats.c3_render, (255, 0, 0))
    elif not in_game_assets_and_stats.c3_available and "character_3" in in_game_assets_and_stats.p2_cycle:
        in_game_assets_and_stats.temp_render = tint(in_game_assets_and_stats.c3_render, (0, 0, 255))
    menu_surface.blit(in_game_assets_and_stats.temp_render, (int(temp_x+(stats.max_width/3.272)), int(temp_y+(stats.max_height/45))))

    # Character 4
    # Test the selection
    in_game_assets_and_stats.temp_render = in_game_assets_and_stats.c4_render
    if stats.current_user_pos == "option_4" and stats.controlling_player == 2:
        stats.selection_box = pygame.draw.rect(menu_surface, stats.selection_color, (temp_x, temp_y+(stats.max_height/4.737), (stats.max_width/6.857), (stats.max_height/4.286)), 0)
    if not in_game_assets_and_stats.c4_available and "character_4" in in_game_assets_and_stats.p1_cycle:
        in_game_assets_and_stats.temp_render = tint(in_game_assets_and_stats.c4_render, (255, 0, 0))
    elif not in_game_assets_and_stats.c4_available and "character_4" in in_game_assets_and_stats.p2_cycle:
        in_game_assets_and_stats.temp_render = tint(in_game_assets_and_stats.c4_render, (0, 0, 255))
    menu_surface.blit(in_game_assets_and_stats.temp_render, (int(temp_x+(stats.max_width/72)), int(temp_y+(stats.max_height/4.286))))

    # Character 5
    # Test the selection
    in_game_assets_and_stats.temp_render = in_game_assets_and_stats.c5_render
    if stats.current_user_pos == "option_5" and stats.controlling_player == 2:
        stats.selection_box = pygame.draw.rect(menu_surface, stats.selection_color, (temp_x+(stats.max_width/6.857), temp_y+(stats.max_height/4.737), (stats.max_width/6.857), (stats.max_height/4.286)), 0)
    if not in_game_assets_and_stats.c5_available and "character_5" in in_game_assets_and_stats.p1_cycle:
        in_game_assets_and_stats.temp_render = tint(in_game_assets_and_stats.c5_render, (255, 0, 0))
    elif not in_game_assets_and_stats.c5_available and "character_5" in in_game_assets_and_stats.p2_cycle:
        in_game_assets_and_stats.temp_render = tint(in_game_assets_and_stats.c5_render, (0, 0, 255))
    menu_surface.blit(in_game_assets_and_stats.temp_render, (int(temp_x+(stats.max_width/6.26)), int(temp_y+(stats.max_height/4.286))))

    # Character 6
    # Test the selection
    in_game_assets_and_stats.temp_render = in_game_assets_and_stats.c6_render
    if stats.current_user_pos == "option_6" and stats.controlling_player == 2:
        stats.selection_box = pygame.draw.rect(menu_surface, stats.selection_color, (temp_x+(2*(stats.max_width/6.857)), temp_y+(stats.max_height/4.737), (stats.max_width/6.857), (stats.max_height/4.286)), 0)
    if not in_game_assets_and_stats.c6_available and "character_6" in in_game_assets_and_stats.p1_cycle:
        in_game_assets_and_stats.temp_render = tint(in_game_assets_and_stats.c6_render, (255, 0, 0))
    elif not in_game_assets_and_stats.c6_available and "character_6" in in_game_assets_and_stats.p2_cycle:
        in_game_assets_and_stats.temp_render = tint(in_game_assets_and_stats.c6_render, (0, 0, 255))
    menu_surface.blit(in_game_assets_and_stats.temp_render, (int(temp_x+(stats.max_width/3.272)), int(temp_y+(stats.max_height/4.286))))


def set_up_stage_select():
    # main_content box
    menu_surface = pygame.Surface((stats.max_width, stats.max_height))
    picture_resized = pygame.transform.scale(stats.menu_background, (stats.max_width, stats.max_height))
    menu_surface.blit(picture_resized, (0, 0))

    temp_x = int(stats.max_width / 16)
    temp_y = int(stats.max_height / 9)
    temp_width = int(stats.max_width / 1.1425)
    temp_height = int(stats.max_height / 2.25)
    stats.stage_menu["main_content"] = pygame.draw.rect(menu_surface, (0, 0, 0), (temp_x, temp_y, temp_width, temp_height), 0)
    # Character Select blit

    stage_list(menu_surface)

    # back box
    temp_x = int(stats.max_width / 16)
    temp_y = int(stats.max_height / 1.636)
    temp_width = int(stats.max_width / 3.695)
    temp_height = int(stats.max_height / 4.5)
    # Test the selection
    if stats.current_user_pos == "back":
        stats.selection_box = pygame.draw.rect(menu_surface, stats.selection_color, (temp_x-(stats.max_width/64), temp_y-(stats.max_height/51.2), temp_width+(stats.max_width/32), temp_height+(stats.max_height/25.6)), 0)
    stats.stage_menu["back"] = pygame.draw.rect(menu_surface, (0, 0, 0), (temp_x, temp_y, temp_width, temp_height), 0)
    # back blit
    temp_text = stats.medium_font.render("Back", 1, (255, 255, 255))
    menu_surface.blit(temp_text, (int((temp_x / 2) + ((temp_width / 2) - (temp_text.get_width() / 3))), int((temp_y / 2) + ((temp_height / 0.45) - (temp_text.get_height() / 1)))))

    # next box
    temp_x = int(stats.max_width / 1.5)
    temp_y = int(stats.max_height / 1.636)
    temp_width = int(stats.max_width / 3.695)
    temp_height = int(stats.max_height / 4.5)
    # Test the selection
    if stats.current_user_pos == "next":
        stats.selection_box = pygame.draw.rect(menu_surface, stats.selection_color, (temp_x-(stats.max_width/64), temp_y-(stats.max_height/51.2), temp_width+(stats.max_width/32), temp_height+(stats.max_height/25.6)), 0)
    stats.stage_menu["next"] = pygame.draw.rect(menu_surface, (0, 0, 0), (temp_x, temp_y, temp_width, temp_height), 0)
    # start blit
    temp_text = stats.medium_font.render("Next", 1, (255, 255, 255))
    menu_surface.blit(temp_text, (int((temp_x / 1) + ((temp_width / 2) - (temp_text.get_width() / 2))), int((temp_y / 2) + ((temp_height / 0.45) - (temp_text.get_height() / 1)))))

    # other box
    temp_x = int(stats.max_width / 2.744)
    temp_y = int(stats.max_height / 1.285)
    temp_width = int(stats.max_width / 3.695)
    temp_height = int(stats.max_height / 9)
    # Test the selection
    if stats.current_user_pos == "other":
        stats.selection_box = pygame.draw.rect(menu_surface, stats.selection_color, (temp_x-(stats.max_width/64), temp_y-(stats.max_height/51.2), temp_width+(stats.max_width/32), temp_height+(stats.max_height/25.6)), 0)
    stats.stage_menu["other"] = pygame.draw.rect(menu_surface, (0, 0, 0), (temp_x, temp_y, temp_width, temp_height), 0)
    # credits blit
    temp_text = stats.small_font.render("Standard", 1, (255, 255, 255))
    menu_surface.blit(temp_text, (int((temp_x / 1) + ((temp_width / 2) - (temp_text.get_width() / 2))), int((temp_y / 2) + ((temp_height / 0.263) - (temp_text.get_height() / 10)))))

    return menu_surface


def stage_list(menu_surface):
    # Small Stage
    temp_x = int(stats.max_width/8.727)
    temp_y = int(stats.max_height/4.643)
    temp_width = int(stats.max_width/5.333)
    temp_height = int(stats.max_height/4.266)

    picture_resized = pygame.transform.scale(in_game_assets_and_stats.s_stage_render, (temp_width, temp_height))
    # Test the selection
    if stats.current_user_pos == "option_4":
        stats.selection_box = pygame.draw.rect(menu_surface, stats.selection_color, (temp_x - (stats.max_width / 64), temp_y - (stats.max_height / 51.2), temp_width + (stats.max_width / 32), temp_height + (stats.max_height / 25.6)), 0)
    if stats.stage_size == "small":
        picture_resized = tint(picture_resized, (127, 127, 127))
    menu_surface.blit(picture_resized, (temp_x, temp_y))

    # Medium Stage
    temp_x = int(stats.max_width / 2.461)
    temp_y = int(stats.max_height / 4.643)

    picture_resized = pygame.transform.scale(in_game_assets_and_stats.m_stage_render, (temp_width, temp_height))
    # Test the selection
    if stats.current_user_pos == "option_5":
        stats.selection_box = pygame.draw.rect(menu_surface, stats.selection_color, (temp_x - (stats.max_width / 64), temp_y - (stats.max_height / 51.2), temp_width + (stats.max_width / 32), temp_height + (stats.max_height / 25.6)), 0)
    if stats.stage_size == "medium":
        picture_resized = tint(picture_resized, (127, 127, 127))
    menu_surface.blit(picture_resized, (temp_x, temp_y))

    # Large Stage
    temp_x = int(stats.max_width / 1.433)
    temp_y = int(stats.max_height / 4.643)

    picture_resized = pygame.transform.scale(in_game_assets_and_stats.l_stage_render, (temp_width, temp_height))
    # Test the selection
    if stats.current_user_pos == "option_6":
        stats.selection_box = pygame.draw.rect(menu_surface, stats.selection_color, (temp_x - (stats.max_width / 64), temp_y - (stats.max_height / 51.2), temp_width + (stats.max_width / 32), temp_height + (stats.max_height / 25.6)), 0)
    if stats.stage_size == "large":
        picture_resized = tint(picture_resized, (127, 127, 127))
    menu_surface.blit(picture_resized, (temp_x, temp_y))
