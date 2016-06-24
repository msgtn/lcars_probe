from datetime import datetime
import pygame
from pygame.mixer import Sound

from ui import colours
from ui.widgets.background import LcarsBackgroundImage, LcarsImage
from ui.widgets.gifimage import LcarsGifImage
from ui.widgets.lcars_widgets import LcarsText, LcarsButton, LcarsBlockHuge, LcarsBlockLarge, LcarsBlockSmall, LcarsTabBlock, LcarsElbow
from ui.widgets.screen import LcarsScreen
from ui.widgets.sprite import LcarsMoveToMouse

class ScreenExplore(LcarsScreen):
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



        ######################################################################

        ##### Explore Screen #####

        all_sprites.add(LcarsText(colours.RED_BROWN, (142, 140), "Select a section for more information", 1.25), layer=70)
        self.explore_screen_text = all_sprites.get_sprites_from_layer(70)
        
        self.probe_forward_image = LcarsImage("assets/probe_front.png", (172, 500), self.forwardHandler)
        self.probe_forward_image.visible = True
        all_sprites.add(self.probe_forward_image, layer =70)

        self.probe_aft_image = LcarsImage("assets/probe_rear.png", (172, 150), self.aftHandler)
        self.probe_aft_image.visible = True
        all_sprites.add(self.probe_aft_image, layer=70)

        ##### Forward Screen #####
        all_sprites.add(LcarsText(colours.RED_BROWN, (142, 140), "Select a component for more information", 1.25), layer=71)
        self.about_text = all_sprites.get_sprites_from_layer(71)

        self.forward_plate = LcarsImage("assets/forward/front_section.png", (172, 533))
        self.forward_plate.visible = False
        all_sprites.add(self.probe_forward_image, layer =71)
        
        



        
        
        #self.forward_port = LcarsTabBlock(colours.BEIGE, (224, 650), "FORWARD PORT", self.fpHandler)
        #self.forward_port.visible = True
        #all_sprites.add(self.forward_port, layer=4)

        #self.aft_starboard = LcarsTabBlock(colours.BEIGE, (278, 650), "AFT STARBOARD", self.asHandler)
        #self.aft_starboard.visible = True
        #all_sprites.add(self.aft_starboard, layer=4)
        
        # specific buttons
        #self.forward_starboard = LcarsTabBlock(colours.BEIGE, (170, 650), "FORWARD SECTION", self.forwardHandler)
        #self.forward_starboard.visible = True
        #all_sprites.add(self.forward_starboard, layer=4)

        #self.aft_port = LcarsTabBlock(colours.BEIGE, (332, 650), "AFT SECTION", self.aftHandler)
        #self.aft_port.visible = True
        #all_sprites.add(self.aft_port, layer=4)

        #######   FORWARD SECTION ######

        #all_sprites.add(LcarsText(colours.RED_BROWN, (192, 140), "Select a component for more information", 1.25), layer=10)

                        
        # Make each component slowly rotate
        #self.sensor_gadget = LcarsGifImage("assets/gadgets/lcars_anim2.gif", (235, 150), 100) 
        #self.sensor_gadget.visible = False
        #all_sprites.add(self.sensor_gadget, layer=2)

        # Forward Section
        #   - Open front hatches & activate red interior lighting
        # Communications Array communicationsHandler
        #   - Illuminate
        # Sensors Array sensorsHandler
        #   - Change spin speed & light up and down? sonar beep?
        # Data Acquisition & Processing Node  computerHandler
        #   - Illuminate (fiber optic lighting)
        # Optical Data Storage Modules  chipsHandler
        #   - Pulse
        # Power System  powerHandler
        #   - Pulse


        ###### AFT SECTION ######

        # Aft Section
        #   - Open rear hatches
        # Ion Thrusters  thrustersHandler
        #   - Pulse (have 2 LED colors, Red & Blue)
        # Ion Drive  driveHandler
        #   - Pulse (have 2 LED colors, Red & Blue)
        # Fuel Tanks  tanksHandler
        #   - illumate section by section
        # Impulse Chemical Reaction Tank  impulseHandler
        #   - Illuminate

        # Also have a way to select the background for the physical specs?

        ##### Back Button #####
        self.aft_port = LcarsTabBlock(colours.RED_BROWN, (372, 650), "BACK", self.backForwardHandler)
        self.aft_port.visible = True
        all_sprites.add(self.aft_port, layer=60)

        ##### More Info Button #####
        self.moreInfo = LcarsTabBlock(colours.BLUE, (318, 650), "MORE INFORMATION", self.moreSensorHandler)
        self.moreInfo.visible = True
        all_sprites.add(self.aft_port, layer=60)

        ########## FORWARD SECTION ##########

        ##### BTO ARRAY #####
        all_sprites.add(LcarsText(colours.WHITE, (112, 140), "B.T.O. ARRAY", 1.75), layer=61)  
        all_sprites.add(LcarsText(colours.ORANGE, (162, 140), "The B.T.O. Array is the primary method of communication for the probe.", 1.25), layer=61)
        all_sprites.add(LcarsText(colours.ORANGE, (192, 140), "The array is entirely composed of the S.B.S. High-Gain Parabolic Antenna,", 1.25), layer = 61)
        all_sprites.add(LcarsText(colours.ORANGE, (222, 140), "which is capable of simultaneous dual transmission in the S and X bands", 1.25), layer=61)
        all_sprites.add(LcarsText(colours.ORANGE, (252, 140), "and receipt of control commands in the Ka and Ku bands.  The array is", 1.25), layer=61)
        all_sprites.add(LcarsText(colours.ORANGE, (282, 140), "paired with the Yokel Sensor Suite to determine physical properties of ", 1.25), layer=61)
        all_sprites.add(LcarsText(colours.ORANGE, (312, 140), "local bodies using microwave radiation.", 1.25), layer=61)
        self.communication_text = all_sprites.get_sprites_from_layer(61)
        self.hideText(self.communication_text)

        ##### YOKEL SENSOR SUITE #####
        all_sprites.add(LcarsText(colours.WHITE, (112, 140), "YOKEL SENSOR SUITE", 1.75), layer=62)
        all_sprites.add(LcarsText(colours.ORANGE, (162, 140), "The Yokel Sensor Suite houses the scientific payload and guidance", 1.25), layer=62)
        all_sprites.add(LcarsText(colours.ORANGE, (192, 140), "system on the probe.  The instruments contained within are:", 1.25), layer=62)
        all_sprites.add(LcarsText(colours.WHITE, (222, 150), "Autonomous Telemetry Guidance Unit", 1.25), layer=62)
        all_sprites.add(LcarsText(colours.WHITE, (242, 150), "Energetic Particle Detector", 1.25), layer=62)
        all_sprites.add(LcarsText(colours.WHITE, (262, 150), "Gravitational Mapping Unit", 1.25), layer=62)
        all_sprites.add(LcarsText(colours.WHITE, (282, 150), "High Energy Multi-Spectral Analyzer", 1.25), layer=62)
        all_sprites.add(LcarsText(colours.WHITE, (302, 150), "Magnetometry Suite", 1.25), layer=62)
        all_sprites.add(LcarsText(colours.WHITE, (322, 150), "Radar Detection & Tracking System", 1.25), layer=62)
        all_sprites.add(LcarsText(colours.WHITE, (342, 150), "Radio Science Array", 1.25), layer=62)
        all_sprites.add(LcarsText(colours.WHITE, (362, 150), "Space Radiation Measurement System", 1.25), layer=62)
        all_sprites.add(LcarsText(colours.ORANGE, (392, 140), "Collected data is stored in the Optical Data Chips for later processing.", 1.25), layer=62)
        self.sensor_text = all_sprites.get_sprites_from_layer(62)
        self.hideText(self.sensor_text)

        ##### Probe Computers #####
        all_sprites.add(LcarsText(colours.WHITE, (112, 140), "PROBE COMPUTERS", 1.75), layer=63)
        all_sprites.add(LcarsText(colours.ORANGE, (162, 140), "This probe features two onboard computers, the Guidance Computer and", 1.25), layer=63)        
        all_sprites.add(LcarsText(colours.WHITE, (162, 473), "Guidance Computer", 1.25), layer=63)
        all_sprites.add(LcarsText(colours.ORANGE, (192, 140), "the Data Processing Unit , which handle all data and control processes.", 1.25), layer=63)
        all_sprites.add(LcarsText(colours.WHITE, (192, 165), "Data Processing Unit", 1.25), layer=63)
        all_sprites.add(LcarsText(colours.ORANGE, (222, 140), "The Guidance Computer receives control commands through the BTO ", 1.25), layer=63)
        all_sprites.add(LcarsText(colours.ORANGE, (252, 140), "Array, and local object data from the Yokel Sensor Suite, to ensure safe", 1.25), layer=63)
        all_sprites.add(LcarsText(colours.ORANGE, (282, 140), "travel.  The Data Processing Unit receives all raw data from the Optical", 1.25), layer=63)
        all_sprites.add(LcarsText(colours.ORANGE, (312, 140), "and processes the data for transmission.  For redundancy, both", 1.25), layer=63)
        all_sprites.add(LcarsText(colours.ORANGE, (342, 140), "computers are independently capable of assuming the others' duties.", 1.25), layer=63)
        self.computer_text = all_sprites.get_sprites_from_layer(63)
        self.hideText(self.computer_text)

        ##### Optical Data Chips #####
        all_sprites.add(LcarsText(colours.WHITE, (112, 140), "OPTICAL DATA CHIPS", 1.75), layer=64)
        all_sprites.add(LcarsText(colours.ORANGE, (162, 140), "This probe is equipped with 24 optical data chips for the storage of sensor", 1.25), layer=64)
        all_sprites.add(LcarsText(colours.ORANGE, (192, 140), "and control data.  Each chip, which can store up to 830 TB of data, is", 1.25), layer=64)
        all_sprites.add(LcarsText(colours.ORANGE, (222, 140), "constructed of a nano-structured quartz composite.  Data is read/written", 1.25), layer=64)
        all_sprites.add(LcarsText(colours.ORANGE, (252, 140), "to the chips using a Smith-Taylor laser system.", 1.25), layer=64)
        self.chip_text = all_sprites.get_sprites_from_layer(64)
        self.hideText(self.chip_text)

        ##### Lofton Microfusion Core #####
        all_sprites.add(LcarsText(colours.WHITE, (112, 140), "LOFTON MICROFUSION CORE", 1.75), layer=65)
        all_sprites.add(LcarsText(colours.ORANGE, (162, 140), "All of the required power for the probe is provided by the Lofton", 1.25), layer=65)
        all_sprites.add(LcarsText(colours.ORANGE, (192, 140), "Microfusion Core.  Encased within a shielded tungsten-titanium shell,", 1.25), layer=65)
        all_sprites.add(LcarsText(colours.ORANGE, (222, 140), "11.3 KW of power are produced from a micro-aneutronic fusion reaction ", 1.25), layer=65)
        all_sprites.add(LcarsText(colours.ORANGE, (252, 140), "which is converted to electricity via electrostatic direct conversion.", 1.25), layer=65)
        all_sprites.add(LcarsText(colours.ORANGE, (282, 140), "Of the 11.3 KW produced, 8 KW are used by the ion propulsion system,", 1.25), layer=65)
        all_sprites.add(LcarsText(colours.ORANGE, (312, 140), "1.4 KW by the sensor suite, 1 KW by the computers, and 0.9 KW by the", 1.25), layer=65)
        all_sprites.add(LcarsText(colours.ORANGE, (342, 140), "communication array during normal operation. Helium is used for the", 1.25), layer=65)
        all_sprites.add(LcarsText(colours.ORANGE, (372, 140), "fusion reaction which is provided by the monopropellant tank.", 1.25), layer=65)
        self.fusion_text = all_sprites.get_sprites_from_layer(65)
        self.hideText(self.fusion_text)

        ########## AFT SECTION ##########
        all_sprites.add(LcarsText(colours.WHITE, (112, 140), "PROPULSION SYSTEM", 1.75), layer=66)
        all_sprites.add(LcarsText(colours.ORANGE, (162, 140), "After launch, the probe is driven by the Kehrer Hybrid Ion Drive, is", 1.25), layer=66)
        all_sprites.add(LcarsText(colours.ORANGE, (192, 140), "capable of both ion and chemical propulsion, and is comprised of the ", 1.25), layer=66)
        all_sprites.add(LcarsText(colours.ORANGE, (222, 140), "engine, thrusters, and fuel tanks. Ion propulsion creates thrust by drawing", 1.25), layer=66)
        all_sprites.add(LcarsText(colours.ORANGE, (252, 140), "power from the fusion core to accelerate and expel Xenon ions from the", 1.25), layer=66)
        all_sprites.add(LcarsText(colours.ORANGE, (282, 140), "two, 420 kg storage tanks, and is the main method of propulsion. For quick", 1.25), layer=66)
        all_sprites.add(LcarsText(colours.ORANGE, (312, 140), "changes in velocity, the chemical propulsion system is activated.  This", 1.25), layer=66)
        all_sprites.add(LcarsText(colours.ORANGE, (342, 140), "system uses the monopropellant hydrazine, which is stored in the 300 kg ", 1.25), layer=66)
        all_sprites.add(LcarsText(colours.ORANGE, (372, 140), "storage tank.  The combination of two different propulsion methods allows", 1.25), layer=66)
        all_sprites.add(LcarsText(colours.ORANGE, (402, 140), "the probe a versatile mix of range and maneuverability.", 1.25), layer=66)
        self.propulsion_text = all_sprites.get_sprites_from_layer(66)
        self.hideText(self.propulsion_text)
                





        #TEST
        self.test = LcarsButton(colours.RED_BROWN, (6, 662), "LOGOUT", self.logoutHandler)
        self.test.visible = False
        all_sprites.add(self.test, layer = 4)

    def hideText(self, name):
        if name[0].visible:
            for sprite in name:
                sprite.visible = False

    def showText(self, name):
        for sprite in name:
            sprite.visible = True

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
        from screens.demoScreen import ScreenDemo
        self.loadScreen(ScreenDemo())

    def exploreHandler(self, item, event, clock):
        # Turn off all content here
        self.test.visible = False

    def mainHandler(self, item, event, clock):
        from screens.main import ScreenMain
        self.loadScreen(ScreenMain())

    ## ****** Explore Screen Handlers ******

        # Forward Section  forwardHandler
        #   - Open front hatches & activate red interior lighting
        # Communications Array communicationsHandler
        #   - Illuminate
        # Sensors Array sensorsHandler
        #   - Change spin speed & light up and down? sonar beep?
        # Data Acquisition & Processing Node  computerHandler
        #   - Illuminate (fiber optic lighting)
        # Optical Data Storage Modules  chipsHandler
        #   - Pulse
        # Power System  powerHandler
        #   - Pulse

        # Aft Section  aftHandler
        #   - Open rear hatches
        # Ion Thrusters  thrustersHandler
        #   - Pulse (have 2 LED colors, Red & Blue)
        # Ion Drive  driveHandler
        #   - Pulse (have 2 LED colors, Red & Blue)
        # Fuel Tanks  tanksHandler
        #   - illumate section by section
        # Impulse Chemical Reaction Tank  impulseHandler
        #   - Illuminate 

    # ** Main **
    def forwardHandler(self, item, event, clock):
        self.hideText(self.explore_screen_text)
        self.probe_forward_image.visible = False
        self.probe_aft_image.visible = False

    def aftHandler(self, item, event, clock):
        self.hideText(self.explore_screen_text)
        self.probe_forward_image.visible = False
        self.probe_aft_image.visible = False

    # ** Forward **
    def communicationsHandler(self, item, event, clock):
        self.test.visible = False

    def sensorsHandler(self, item, event, clock):
        self.hideText(self.sensor_text)

    def computerHandler(self, item, event, clock):
        self.test.visible = False

    def chipsHandler(self, item, event, clock):
        self.test.visible = False

    def powerHandler(self, item, event, clock):
        self.test.visible = False

    # ** Aft **
    def thrustersHandler(self, item, event, clock):
        self.test.visible = False

    def driveHandler(self, item, event, clock):
        self.test.visible = False

    def tanksHandler(self, item, event, clock):
        self.test.visible = False

    def impulseHandler(self, item, event, clock):
        self.test.visible = False

    def backForwardHandler(self, item, event, clock):
        self.test.visible = False

    def moreSensorHandler(self, item, event, clock):
        self.test.visible = False

        
