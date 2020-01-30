# These are all Default Values before they are set

# Keeps record of the screen size to be used
max_width = 0
max_height = 0

# Keeps track of the things that have already been displayed. False = Not ran, True = Ran
item_status = {"intro": False, "title_menu": False, "char_select": False, "stage_select": False}

# The current screen the user is on
current_screen = None

# Title & icon for the game
title = "NONE"
icon = None

# Is true until user quits
game_running = True

# Faded company logo and name to be displayed before game starts
company_screen = None

# Darkness of the black transition
black_transition = 300

# To be played in intro and menus
intro_music = None

# A surface for the fade to be blitted on
fade_surface = None

# Determines if the object is fading in (black_transition is decreasing) or out (black_transition is increasing)
fade_direction = "in"

# Determines which object is to be faded
company_fade_run = True
title_fade_run = True

# Background Picture for title screen
menu_background = None

# Game Tiem???
game_playing = False

# A menu: Title screen
title_menu = {"background": menu_background, "main_content": None, "back": None, "next": None, "other": None}

# A menu: Character Select screen
char_menu = {"background": menu_background, "main_content": None, "back": None, "next": None, "other": None}
controlling_player = 0
controlling_player_str = "Player 0"
selection_color = (0, 0, 0)
# A menu: Stage Select screen
stage_menu = {"background": menu_background, "main_content": None, "back": None, "next": None, "other": None}

current_user_pos = "back"

selection_cycle = ["option_1", "option_2", "option_3", "option_4", "option_5", "option_6", "back", "other", "next"]

selection_num = 6

selection_box = None

small_font = None
medium_font = None
big_font = None

stage_size = None
