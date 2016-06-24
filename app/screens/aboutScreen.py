from datetime import datetime
import pygame
from pygame.mixer import Sound

from ui import colours
from ui.widgets.background import LcarsBackgroundImage, LcarsImage
from ui.widgets.gifimage import LcarsGifImage
from ui.widgets.lcars_widgets import LcarsText, LcarsButton, LcarsBlockHuge, LcarsBlockLarge, LcarsBlockSmall, LcarsTabBlock, LcarsElbow
from ui.widgets.screen import LcarsScreen
from ui.widgets.sprite import LcarsMoveToMouse


class ScreenAbout(LcarsScreen):
    def setup(self, all_sprites):
        
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
        #all_sprites.add(LcarsText(colours.WHITE, (192, 174), "WELCOME", 1.5),
        #                layer=3)
        #all_sprites.add(LcarsText(colours.BLUE, (244, 174), "TO THE Museum of Science Fiction", 1.5),
        #                layer=3)
        #all_sprites.add(LcarsText(colours.BLUE, (286, 174), "LONG RANGE PROBE EXHIBIT", 1.5),
        #                layer=3)
        #all_sprites.add(LcarsText(colours.BLUE, (330, 174), "LOOK AROUND", 1.5),
        #                layer=3)
        #self.info_text = all_sprites.get_sprites_from_layer(3)

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

        # specific buttons
        self.purpose = LcarsButton(colours.GREY_BLUE, (107, 127), "PURPOSE", self.purposeHandler)
        self.purpose.visible = True
        all_sprites.add(self.purpose, layer=4)

        self.details = LcarsButton(colours.ORANGE, (107, 262), "DETAILS", self.detailsHandler)
        self.details.visible = True
        all_sprites.add(self.details, layer=4)

        self.personnel = LcarsButton(colours.GREY_BLUE, (107, 398), "PERSONNEL", self.personnelHandler)
        self.personnel.visible = True
        all_sprites.add(self.personnel, layer=4)

        self.sources = LcarsButton(colours.ORANGE, (107, 533), "SOURCES", self.sourcesHandler)
        self.sources.visible = True
        all_sprites.add(self.sources, layer=4)

        # Purpose
        all_sprites.add(LcarsText(colours.WHITE, (172, 140), "To inspire the next generation of STEAM", 2.7), layer=3) 
        all_sprites.add(LcarsText(colours.WHITE, (217, 140), "(science, technology, engineering, art,", 2.7), layer=3)
        all_sprites.add(LcarsText(colours.WHITE, (262, 140), "mathematics) students to innovate with", 2.7), layer=3)
        all_sprites.add(LcarsText(colours.WHITE, (307, 140), "unique projects and boldly go where no", 2.7), layer=3)
        all_sprites.add(LcarsText(colours.WHITE, (352, 140), "one has gone before.", 2.7), layer=3)
        #all_sprites.add(LcarsText(colours.BLUE, (244, 174), "TO THE Museum of Science Fiction", 1),
        #                layer=3)
        #all_sprites.add(LcarsText(colours.BLUE, (286, 174), "LONG RANGE PROBE EXHIBIT", 1),
        #                layer=3)
        #all_sprites.add(LcarsText(colours.BLUE, (330, 174), "LOOK AROUND", 1),
        #                layer=3)
        self.purpose_text = all_sprites.get_sprites_from_layer(3)
        self.hideText(self.purpose_text) 

        # Details
        all_sprites.add(LcarsText(colours.ORANGE, (192, 140), "LENGTH: ", 1.25), layer=6)
        all_sprites.add(LcarsText(colours.WHITE, (192, 220), "1.5 m (4 ft 6 in)", 1.25), layer=6)
        all_sprites.add(LcarsText(colours.ORANGE, (212, 140), "WIDTH: ", 1.25), layer=6)
        all_sprites.add(LcarsText(colours.WHITE, (212, 220), "0.45 m (1 ft 6 in)", 1.25), layer=6)
        all_sprites.add(LcarsText(colours.ORANGE, (232, 140), "HEIGHT: ", 1.25), layer=6)
        all_sprites.add(LcarsText(colours.WHITE, (232, 220), "0.25 m (10 in)", 1.25), layer=6)
        all_sprites.add(LcarsText(colours.ORANGE, (252, 140), "MASS: ", 1.25), layer=6)
        all_sprites.add(LcarsText(colours.WHITE, (252, 220), "20 kg (30 slugs)", 1.25), layer=6)
        all_sprites.add(LcarsText(colours.ORANGE, (292, 140), "MATERIALS: ", 1.25), layer=6)
        all_sprites.add(LcarsText(colours.WHITE, (292, 220), "Carbon fiber reinforced fiberglass shell, internal components 3D-printed PLA plastic", 1.25), layer=6)
        all_sprites.add(LcarsText(colours.ORANGE, (332, 140), "CONTROL: ", 1.25), layer=6)
        all_sprites.add(LcarsText(colours.WHITE, (332, 220), "7-inch touchscreen via Rasberry Pi, lights & movement via Arduino Mega", 1.25), layer=6)
        all_sprites.add(LcarsText(colours.ORANGE, (372, 140), "COST: ", 1.25), layer=6)
        all_sprites.add(LcarsText(colours.WHITE, (372, 220), "$1,000, 800 man-hours", 1.25), layer=6)
        self.details_text = all_sprites.get_sprites_from_layer(6)
        self.hideText(self.details_text)

        # Personnel
        all_sprites.add(LcarsText(colours.RED_BROWN, (192, 140), "Designed and built by a team of four mechanical & aerospace", 1.25), layer=7)
        all_sprites.add(LcarsText(colours.RED_BROWN, (212, 140), "engineering students at North Carolina State University", 1.25), layer=7)
        self.personnel_text= all_sprites.get_sprites_from_layer(7)
        self.hideText(self.personnel_text)
        
        self.personnel_image1 = LcarsImage("assets/ncsu.png", (192, 560))
        self.personnel_image1.visible = False
        all_sprites.add(self.personnel_image1, layer=7)

        # Sources
        all_sprites.add(LcarsText(colours.GREY_BLUE, (192, 140), "SPECIAL THANKS TO:", 1.25), layer=8)
        all_sprites.add(LcarsText(colours.WHITE, (212, 180), "Toby Kurien (creator of LCARS Python Graphical Interface)", 1.25), layer=8)
        all_sprites.add(LcarsText(colours.WHITE, (232, 180), "NC State Mechanical Engineering Department", 1.25), layer=8)
        all_sprites.add(LcarsText(colours.WHITE,(252, 180), "NC State Entrepreneurship Initiative Garage", 1.25), layer=8)
        self.sources_text = all_sprites.get_sprites_from_layer(8)
        self.hideText(self.sources_text)
        

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

    def hideText(self, name):
        if name[0].visible:
            for sprite in name:
                sprite.visible = False

    def showText(self, name):
        for sprite in name:
            sprite.visible = True
    
    def logoutHandler(self, item, event, clock):
        demo()
#         from screens.authorize import ScreenAuthorize
#         self.loadScreen(ScreenAuthorize())

    def demoHandler(self, item, event, clock):
        demo()

    def exploreHandler(self, item, event, clock):
        demo()
#         from screens.exploreScreen import ScreenExplore
#         self.loadScreen(ScreenExplore())

    def mainHandler(self, item, event, clock):
        demo()
#         from screens.main import ScreenMain
#         self.loadScreen(ScreenMain())

    ## Specific Screen Handlers
        
    def aboutHandler(self, item, event, clock):
        self.hideText(self.purpose_text)
        self.hideText(self.details_text)
        self.hideText(self.personnel_text)
        self.personnel_image1.visible = False
        self.hideText(self.sources_text)

    def purposeHandler(self, item, event, clock):
        self.showText(self.purpose_text)
        self.hideText(self.details_text)
        self.hideText(self.personnel_text)
        self.personnel_image1.visible = False
        self.hideText(self.sources_text)
        
    def detailsHandler(self, item, event, clock):
        self.hideText(self.purpose_text)
        self.showText(self.details_text)
        self.hideText(self.personnel_text)
        self.personnel_image1.visible = False
        self.hideText(self.sources_text)

    def personnelHandler(self, item, event, clock):
        self.hideText(self.purpose_text)
        self.hideText(self.details_text)
        self.showText(self.personnel_text)
        self.personnel_image1.visible = True
        self.hideText(self.sources_text)

    def sourcesHandler(self, item, event, clock):
        self.hideText(self.purpose_text)
        self.hideText(self.details_text)
        self.hideText(self.personnel_text)
        self.personnel_image1.visible = False
        self.showText(self.sources_text)
        
