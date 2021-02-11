import pygame
import pygame_menu
from random import randrange
from typing import Tuple, Any, Optional, List

DIFFICULTY = ['ASTAR']
pygame.init()
surface = pygame.display.set_mode((600, 600))



def change_difficulty(value: Tuple[Any, int], difficulty: str) -> None:
    """
    Change difficulty of the game.
    :param value: Tuple containing the data of the selected object
    :param difficulty: Optional parameter passed as argument to add_selector
    """
    selected, index = value
    DIFFICULTY[0] = difficulty

def play_function(difficulty: List) -> None:
    assert isinstance(difficulty, list)
    difficulty = difficulty[0]
    assert isinstance(difficulty, str)

    if difficulty == 'ASTAR':
       import astar
     


mytheme = pygame_menu.themes.THEME_DARK.copy()

font = pygame_menu.font.FONT_MUNRO
font2 = pygame_menu.font.FONT_COMIC_NEUE
mytheme.widget_font=font
mytheme.title_font = font
mytheme.title_font_size = 28

menu = pygame_menu.Menu(
			300, 400,
        	theme=mytheme,
        	title="Menu")
menu.add_selector('Select Algorithm ',[('A *', 'ASTAR'),('Kruskal', 'KRUSKAL'),('DIJKSTRA', 'DIJKSTRA')],onchange=change_difficulty,selector_id='select_difficulty')
menu.add_button('Run', play_function, DIFFICULTY)
menu.add_button('Quit', pygame_menu.events.EXIT)
menu.add_label(" ", max_char=-1, font_size=16,  )
menu.add_label(" ", max_char=-1, font_size=16,  )
menu.add_label(" ", max_char=-1, font_size=16,  )
menu.add_label("by Yahya Al-Marshoud", max_char=-1, font_size=16, font_color= (245,245,245) )
menu.mainloop(surface)
