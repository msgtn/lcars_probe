from datetime import datetime
import pygame
from pygame.mixer import Sound

from ui import colours
from ui.widgets.background import LcarsBackgroundImage, LcarsImage
from ui.widgets.gifimage import LcarsGifImage
from ui.widgets.lcars_widgets import LcarsText, LcarsButton, LcarsBlockHuge, LcarsBlockLarge, LcarsBlockSmall, LcarsTabBlock, LcarsElbow
from ui.widgets.screen import LcarsScreen
from ui.widgets.sprite import LcarsMoveToMouse
from ui import arduino_send
import time

class ScreenDemo(LcarsScreen):
    def setup(self, all_sprites):
        arduino_send(str(180))
        time.sleep(2)
        arduino_send(str(90))
        all_sprites.add(LcarsBackgroundImage("assets/lcars_screen_1.png"),
                        layer=0)
        
        # panel text
        all_sprites.add(LcarsText(colours.BLACK, (11, 75), "MOSF"),
                        layer=1)
        all_sprites.add(LcarsText(colours.ORANGE, (0, 135), "LONG RANGE PROBE", 2.5),
                        layer=1)
        all_sprites.add(LcarsText(colours.BLACK, (54, 667), "192 168 0 3"),
                        layer=1)

        # info text
        all_sprites.add(LcarsText(colours.WHITE, (192, 174), "WELCOME", 1.5),
                        layer=3)
        all_sprites.add(LcarsText(colours.BLUE, (244, 174), "TO THE Museum of Science Fiction", 1.5),
                        layer=3)
        all_sprites.add(LcarsText(colours.BLUE, (286, 174), "LONG RANGE PROBE EXHIBIT", 1.5),
                        layer=3)
        all_sprites.add(LcarsText(colours.BLUE, (330, 174), "LOOK AROUND", 1.5),
                        layer=3)
        self.info_text = all_sprites.get_sprites_from_layer(3)

        # date display
        self.stardate = LcarsText(colours.BLACK, (444, 506), "", 1)
        self.lastClockUpdate = 0
        all_sprites.add(self.stardate, layer=1)

        # permanent buttons        
        all_sprites.add(LcarsButton(colours.RED_BROWN, (6, 662), "LOGOUT", self.logoutHandler),
                        layer=1)
        all_sprites.add(LcarsBlockSmall(colours.ORANGE, (211, 16), "ABOUT", self.aboutHandler),
                        layer=1)
        all_sprites.add(LcarsBlockLarge(colours.BLUE, (145, 16), "DEMO", self.demoHandler),
                        layer=1)
        all_sprites.add(LcarsBlockHuge(colours.PEACH, (249, 16), "EXPLORE", self.exploreHandler),
                        layer=1)
        all_sprites.add(LcarsElbow(colours.BEIGE, (400, 16), "MAIN", self.mainHandler),
                        layer=1)
        
        # Sounds
        self.beep1 = Sound("assets/audio/panel/201.wav")
        #Sound("assets/audio/panel/220.wav").play()

        ################################ specific buttons

        #Have a launch Button
        #with Step by step description

##        -Open all hatches
##        -activate power
##        -activate onboard computer and chips
##        -activate commmunications array (have static fade to beeping, followed by confirmation beep
##        - Begin sensors array
##        -close front hatches
##        - Illuminate impulse tank
##        - fire red thrusters
##        - illuminate ion drive & pulse tanks
##        -blue thrusters
##        -close rear hatches
       
        #TEST
        self.test = LcarsButton(colours.RED_BROWN, (6, 662), "LOGOUT", self.logoutHandler)
        self.test.visible = False
        all_sprites.add(self.test, layer = 4)

    def update(self, screenSurface, fpsClock):
        if pygame.time.get_ticks() - self.lastClockUpdate > 1000:
            self.stardate.setText("EARTH DATE {}".format(datetime.now().strftime("%m.%d.%y %H:%M:%S")))
            self.lastClockUpdate = pygame.time.get_ticks()
        LcarsScreen.update(self, screenSurface, fpsClock)
        
    def handleEvents(self, event, fpsClock):
        LcarsScreen.handleEvents(self, event, fpsClock)
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.beep1.play()

        if event.type == pygame.MOUSEBUTTONUP:
            return False
    
    def logoutHandler(self, item, event, clock):
        from screens.authorize import ScreenAuthorize
        self.loadScreen(ScreenAuthorize())

    def aboutHandler(self, item, event, clock):
        from screens.aboutScreen import ScreenAbout
        self.loadScreen(ScreenAbout())

    def demoHandler(self, item, event, clock):
        # Turn off all content here
        self.test.visible = False

    def exploreHandler(self, item, event, clock):
        from screens.exploreScreen import ScreenExplore
        self.loadScreen(ScreenExplore())

    def mainHandler(self, item, event, clock):
        from screens.main import ScreenMain
        self.loadScreen(ScreenMain())

    ## Specific Screen Handlers


        
