import pygame


class OnScreenObject:
    def __init__(self, is_vis=False):
        self.is_vis = is_vis

    # Draws the object, hopefully the image was loaded before
    # asset, type, x, y, width, height, font, font_size, window
    def draw(self, pic=None, text=None, list=[], window=None):
        if self.is_vis:
            # If it is text
            if list[0] is "text":
                if list[5] is "rockoftimes":
                    rockoftimes = open("assets/fonts/rockoftimes.otf")
                    font = pygame.font.Font(rockoftimes, list[6])
                    written_text = font.render(text, True, (255, 255, 255))
                    window.blit(written_text, (list[1], list[2]))
                    rockoftimes.close()
            # If it is a picture
            elif list[0] is "pic":
                rescaled = pygame.transform.scale(pic, (list[3], list[4]))
                window.blit(rescaled, (list[1], list[2]))
        else:
            pass
