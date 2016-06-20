import pygame
from pygame.mixer import Sound

from ui import colours
from ui.widgets.background import LcarsBackgroundImage
from ui.widgets.gifimage import LcarsGifImage
from ui.widgets.lcars_widgets import LcarsText
from ui.widgets.screen import LcarsScreen


class ScreenAuthorize(LcarsScreen):

    def setup(self, all_sprites):

        all_sprites.add(LcarsBackgroundImage("assets/intro_screen.png"),
                        layer=0)

        all_sprites.add(LcarsText(colours.ORANGE, (270, -1), "LONG RANGE PROBE", 3),
                        layer=1)

        all_sprites.add(LcarsText(colours.BLUE, (330, -1), "", 1.5),
                        layer=1)

        all_sprites.add(LcarsText(colours.BLUE, (360, -1), "", 1.5),
                        layer=1)

        all_sprites.add(LcarsText(colours.ORANGE, (390, -1), "TOUCH TERMINAL TO PROCEED", 1.5),
                        layer=1)

        all_sprites.add(LcarsGifImage("assets/gadgets/MOSF.gif", (90, 330), 35), layer=1)        

        # sounds
        Sound("assets/audio/panel/215.wav").play()
        self.sound_granted = Sound("assets/audio/accessing.wav")
        self.sound_beep1 = Sound("assets/audio/panel/206.wav")

    def handleEvents(self, event, fpsClock):
        LcarsScreen.handleEvents(self, event, fpsClock)

        if event.type == pygame.MOUSEBUTTONDOWN:
            self.sound_beep1.play()

        if event.type == pygame.MOUSEBUTTONUP:
            self.sound_granted.play()
            from screens.main import ScreenMain
            self.loadScreen(ScreenMain())        

        return False   
