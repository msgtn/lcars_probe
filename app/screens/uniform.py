from datetime import datetime
import pygame
from pygame.mixer import Sound

from ui import colours
from ui.widgets.background import LcarsBackgroundImage, LcarsImage
from ui.widgets.gifimage import LcarsGifImage
from ui.widgets.lcars_widgets import LcarsText, LcarsButton, LcarsBlockHuge, LcarsBlockLarge, LcarsBlockSmall, LcarsTabBlock, LcarsElbow
from ui.widgets.screen import LcarsScreen
from ui.widgets.sprite import LcarsMoveToMouse, LcarsWidget


class ScreenUniform(LcarsScreen):
    def __init__(self, all_sprites):
        
        all_sprites.add(LcarsBackgroundImage("assets/lcars_screen_1.png"),
                        layer=0)
        
        # panel text
        all_sprites.add(LcarsText(colours.BLACK, (11, 75), "MOSF"),
                        layer=1)
        all_sprites.add(LcarsText(colours.ORANGE, (0, 135), "LONG RANGE PROBE", 2.5),
                        layer=1)
        all_sprites.add(LcarsText(colours.BLACK, (54, 667), "192 168 0 3"),
                        layer=1)



        # permanent buttons        
        all_sprites.add(LcarsButton(colours.RED_BROWN, (6, 662), "LOGOUT"),
                        layer=1)
        all_sprites.add(LcarsBlockSmall(colours.ORANGE, (211, 16), "ABOUT", self.aboutHandler),
                        layer=1)
        all_sprites.add(LcarsBlockLarge(colours.BLUE, (145, 16), "DEMO", self.demoHandler),
                        layer=1)
        all_sprites.add(LcarsBlockHuge(colours.PEACH, (249, 16), "EXPLORE", self.exploreHandler),
                        layer=1)
        all_sprites.add(LcarsElbow(colours.BEIGE, (400, 16), "MAIN"),
                        layer=1)
        
        # Sounds
        self.beep1 = Sound("assets/audio/panel/201.wav")

    # Uniform

    #def update(self, screenSurface, fpsClock):
    #    if pygame.time.get_ticks() - self.lastClockUpdate > 1000:
    #        self.stardate.setText("EARTH DATE {}".format(datetime.now().strftime("%m.%d.%y %H:%M:%S")))
    #        self.lastClockUpdate = pygame.time.get_ticks()
    #    LcarsScreen.update(self, screenSurface, fpsClock)
##        
##    def handleEvents(self, event, fpsClock):
##        LcarsScreen.handleEvents(self, event, fpsClock)
##        
##        if event.type == pygame.MOUSEBUTTONDOWN:
##            self.beep1.play()
##
##        if event.type == pygame.MOUSEBUTTONUP:
##            return False

    # Screen Handlers
    
    def logoutHandler(self, item, event, clock):
        from screens.authorize import ScreenAuthorize
        self.loadScreen(ScreenAuthorize())
        print "uniform"

    def aboutHandler(self, item, event, clock):
        from screens.aboutScreen import ScreenAbout
        self.loadScreen(ScreenAbout())

    def demoHandler(self, item, event, clock):
        from screens.demoScreen import ScreenDemo
        self.loadScreen(ScreenDemo())

    def exploreHandler(self, item, event, clock):
        from screens.exploreScreen import ScreenExplore
        self.loadScreen(ScreenExplore())
