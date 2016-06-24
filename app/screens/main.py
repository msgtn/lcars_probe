from datetime import datetime
import pygame
from pygame.mixer import Sound

from ui import colours
from ui.widgets.background import LcarsBackgroundImage, LcarsImage
from ui.widgets.gifimage import LcarsGifImage
from ui.widgets.lcars_widgets import LcarsText, LcarsButton, LcarsImageButton, LcarsBlockHuge, LcarsBlockLarge, LcarsBlockSmall, LcarsTabBlock, LcarsElbow
from ui.widgets.screen import LcarsScreen
from ui.widgets.sprite import LcarsMoveToMouse, LcarsWidget

import time
import serial

from hardwareHandler import *
a = connect_arduino()
# try to connect to the arduino
#a_exist = False
#try:
#    a = serial.Serial('/dev/ttyACM0', 9600)
#    a_exist = True
#except:
#    pass
# USE LIKE THIS: ser.write('1')

class ScreenMain(LcarsScreen):
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
        all_sprites.add(LcarsElbow(colours.BEIGE, (400, 16), "MAIN"),
                        layer=1)
        
        # Sounds
        self.beep_1 = Sound("assets/audio/panel/201.wav")
        #Sound("assets/audio/panel/220.wav").play()

        #-----Screens-----#
        # ** Screen Handlers ** --------------------------------------------------------------------

    def mainHandler(self, item, event, clock):
#         self.hideAll()
        
        self.showText(self.main_text)
            
    def logoutHandler(self, item, event, clock):
        self.loadScreen(self, LogoutScreen)
        self.getNextScreen()
#         self.hideAll()
        
#         self.logout_image.visible = True
#         self.logout_gif.visible = True
#         self.showText(self.logout_text)

        # PUT TURN OFF COMMAND HERE

    def demoHandler(self, item, event, clock):
        #from screens.demoScreen import ScreenDemo
        #self.loadScreen(ScreenDemo())
        '''
        servo_pos_test(a, 90)
        
        servo_pos_test(a, 180)
        
        servo_pos_test(a, 90)
        
        servo_pos_test(a, 0)
        
        servo_pos_test(a, 90)
        '''

        for j in range(60, 0, -20):
            for i in range(1, 6):
                control_led(a, i, 1)
                time.sleep(float(j)/100)
                control_led(a, i, 0)
                

        door_fr(a, 1)
        door_fl(a, 1)
        door_br(a, 1)
        door_bl(a, 1)
        door_fr(a, 0)
        door_fl(a, 0)
        door_br(a, 0)
        door_bl(a, 0)

        
        
    def aboutHandler(self, item, event, clock):
        self.hideAll()
        
        self.purpose.visible = True
        self.details.visible = True
        self.personnel.visible = True
        self.sources.visible = True

    #def demoHandler(self, item, event, clock):
    #    from screens.demoScreen import ScreenDemo
    #    self.loadScreen(ScreenDemo())

    def exploreHandler(self, item, event, clock):
        self.hideAll()
        
        self.showText(self.explore_screen_text)
        self.probe_forward_image.visible = True
        self.probe_aft_image.visible = True


      
class DefaultScreen(LcarsScreen):
    def setup(self, all_sprites):  
        # Main Screen ------------------------------------------------------------------------------------
        #116-800: 684 : 342
        #90-440 : 350 : 175
        all_sprites.add(LcarsText(colours.WHITE, (192, 174), "WELCOME", 1.5),
                        layer=2)
        all_sprites.add(LcarsText(colours.BLUE, (244, 174), "TO THE Museum of Science Fiction", 1.5),
                        layer=2)
        all_sprites.add(LcarsText(colours.BLUE, (286, 174), "LONG RANGE PROBE EXHIBIT", 1.5),
                        layer=2)
        all_sprites.add(LcarsText(colours.BLUE, (330, 174), "LOOK AROUND", 1.5),
                        layer=2)
        self.main_text = all_sprites.get_sprites_from_layer(2)
        
class LogoutScreen(LcarsScreen):
    def setup(self, all_sprites):
        # Logout Screen ----------------------------------------------------------------------------------
        self.logout_image = LcarsImage("assets/intro_screen.png", (0,0), self.mainHandler)
        self.logout_image.visible = False
        all_sprites.add(self.logout_image, layer=2) #Previously layer2

        self.logout_gif = LcarsGifImage("assets/gadgets/MOSF.gif", (90, 330), 35)
        self.logout_gif.visible = False
        all_sprites.add(self.logout_gif, layer=2) #Previously 2

        all_sprites.add(LcarsText(colours.ORANGE, (270, -1), "LONG RANGE PROBE", 3), layer=3)
        all_sprites.add(LcarsText(colours.ORANGE, (390, -1), "TOUCH TERMINAL TO PROCEED", 1.5), layer=3)
        self.logout_text = all_sprites.get_sprites_from_layer(3)
        self.hideText(self.logout_text)
        

        # Demo Screen ------------------------------------------------------------------------------------


class AboutScreen(LcarsScreen):
    def setup(all_sprites):
        # About Screen -----------------------------------------------------------------------------------
        self.purpose = LcarsButton(colours.GREY_BLUE, (107, 127), "PURPOSE", self.purposeHandler)
        self.purpose.visible = False
        all_sprites.add(self.purpose, layer=2)

        self.details = LcarsButton(colours.ORANGE, (107, 262), "DETAILS", self.detailsHandler)
        self.details.visible = False
        all_sprites.add(self.details, layer=2)

        self.personnel = LcarsButton(colours.GREY_BLUE, (107, 398), "PERSONNEL", self.personnelHandler)
        self.personnel.visible = False
        all_sprites.add(self.personnel, layer=2)

        self.sources = LcarsButton(colours.ORANGE, (107, 533), "SOURCES", self.sourcesHandler)
        self.sources.visible = False
        all_sprites.add(self.sources, layer=2)

        
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
        all_sprites.add(LcarsText(colours.WHITE, (212, 180), "Toby Kurien (creator of LCARS Python Graphical Interface", 1.25), layer=8)
        all_sprites.add(LcarsText(colours.WHITE, (232, 180), "NC State Mechanical Engineering Department", 1.25), layer=8)
        all_sprites.add(LcarsText(colours.WHITE,(252, 180), "NC State Entrepreneurship Initiative Garage", 1.25), layer=8)
        self.sources_text = all_sprites.get_sprites_from_layer(8)
        self.hideText(self.sources_text)

        # Explore Screen ---------------------------------------------------------------------------------

        all_sprites.add(LcarsText(colours.RED_BROWN, (142, 140), "Select a section for more information", 1.25), layer=70)
        self.explore_screen_text = all_sprites.get_sprites_from_layer(70)
        self.hideText(self.explore_screen_text)
        
        self.probe_forward_image = LcarsImageButton("assets/forward_section.png", (172, 500), self.forwardHandler)
        self.probe_forward_image.visible = False
        all_sprites.add(self.probe_forward_image, layer =70)

        self.probe_aft_image = LcarsImageButton("assets/probe_rear.png", (172, 150), self.aftHandler)
        self.probe_aft_image.visible = False
        all_sprites.add(self.probe_aft_image, layer=70)



        ##### Forward Section #####
        all_sprites.add(LcarsText(colours.RED_BROWN, (142, 140), "Select a component for more information", 1.25), layer=71)
        self.forward_text = all_sprites.get_sprites_from_layer(71)

        self.forward_plate = LcarsImage("assets/forward/front_section.png", (172, 533))
        self.forward_plate.visible = False
        all_sprites.add(self.probe_forward_image, layer =71)

        ## Back Forward Button ##
        self.forward_button = LcarsTabBlock(colours.RED_BROWN, (372, 500), "BACK", self.forwardHandler)
        self.forward_button.visible = False
        all_sprites.add(self.forward_button, layer=60)

        ## Back Aft Button ##
        self.aft_button = LcarsTabBlock(colours.RED_BROWN, (372, 150), "BACK", self.exploreHandler)
        self.aft_button.visible = False
        all_sprites.add(self.aft_button, layer=60)

        # BTO ARRAY #
        all_sprites.add(LcarsText(colours.WHITE, (112, 140), "B.T.O. ARRAY", 1.75), layer=61)  
        all_sprites.add(LcarsText(colours.ORANGE, (162, 140), "The B.T.O. Array is the primary method of communication for the probe.", 1.25), layer=61)
        all_sprites.add(LcarsText(colours.ORANGE, (192, 140), "The array is entirely composed of the S.B.S. High-Gain Parabolic Antenna,", 1.25), layer = 61)
        all_sprites.add(LcarsText(colours.ORANGE, (222, 140), "which is capable of simultaneous dual transmission in the S and X bands", 1.25), layer=61)
        all_sprites.add(LcarsText(colours.ORANGE, (252, 140), "and receipt of control commands in the Ka and Ku bands.  The array is", 1.25), layer=61)
        all_sprites.add(LcarsText(colours.ORANGE, (282, 140), "paired with the Yokel Sensor Suite to determine physical properties of ", 1.25), layer=61)
        all_sprites.add(LcarsText(colours.ORANGE, (312, 140), "local bodies using microwave radiation.", 1.25), layer=61)
        self.communication_text = all_sprites.get_sprites_from_layer(61)
        self.hideText(self.communication_text)

        # YOKEL SENSOR SUITE #
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

        # Probe Computers #
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

        # Optical Data Chips #
        all_sprites.add(LcarsText(colours.WHITE, (112, 140), "OPTICAL DATA CHIPS", 1.75), layer=64)
        all_sprites.add(LcarsText(colours.ORANGE, (162, 140), "This probe is equipped with 24 optical data chips for the storage of sensor", 1.25), layer=64)
        all_sprites.add(LcarsText(colours.ORANGE, (192, 140), "and control data.  Each chip, which can store up to 830 TB of data, is", 1.25), layer=64)
        all_sprites.add(LcarsText(colours.ORANGE, (222, 140), "constructed of a nano-structured quartz composite.  Data is read/written", 1.25), layer=64)
        all_sprites.add(LcarsText(colours.ORANGE, (252, 140), "to the chips using a Smith-Taylor laser system.", 1.25), layer=64)
        self.chip_text = all_sprites.get_sprites_from_layer(64)
        self.hideText(self.chip_text)

        # Lofton Microfusion Core #
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

        

        ###### AFT SECTION ######
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

        
        
    # ** Event Handlers **

    def update(self, screenSurface, fpsClock):
        if pygame.time.get_ticks() - self.lastClockUpdate > 1000:
            self.stardate.setText("EARTH DATE {}".format(datetime.now().strftime("%m.%d.%y %H:%M:%S")))
            self.lastClockUpdate = pygame.time.get_ticks()
        LcarsScreen.update(self, screenSurface, fpsClock)
        
    def handleEvents(self, event, fpsClock):
        LcarsScreen.handleEvents(self, event, fpsClock)
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.beep_1.play()

        if event.type == pygame.MOUSEBUTTONUP:
            return False

    
    # ** Sub Screen Handlers ** -----------------------------------------------------------------

    #       About Screen -------------------------------------
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



    #       Explore Screen -----------------------------------
    # ** Main **
    def forwardHandler(self, item, event, clock):
        self.hideText(self.explore_screen_text)
        self.probe_forward_image.visible = False
        self.probe_aft_image.visible = False
        self.forward_button.visible = False
        
        self.hideText(self.communication_text)
        self.hideText(self.sensor_text)
        self.hideText(self.computer_text)
        self.hideText(self.chip_text)
        self.hideText(self.fusion_text)
        
        self.showText(self.forward_text)
        self.aft_button.visible = True        
        #Put others here
        self.forward_plate.visible = True

    def aftHandler(self, item, event, clock):
        self.hideAll()
        self.hideText(self.explore_screen_text)
        self.probe_forward_image.visible = False
        self.probe_aft_image.visible = False
        red_thruster(a, 1)
        time.sleep(1)
        red_thruster(a, 0)
        self.showText(propulsion_text)
        self.aft_button.visible = True

    # ** Forward **
    def communicationsHandler(self, item, event, clock):
        self.showText(self.communication_text)
        self.aft_button.visible = False
        self.forward_button.visible = True

    def sensorsHandler(self, item, event, clock):
        self.showText(sensor_text)
        self.aft_button.visible = False
        self.forward_button.visible = True

    def computerHandler(self, item, event, clock):
        self.showText(computer_text)
        self.aft_button.visible = False
        self.forward_button.visible = True

    def chipsHandler(self, item, event, clock):
        self.showText(chip_text)
        self.aft_button.visible = False
        self.forward_button.visible = True

    def powerHandler(self, item, event, clock):
        self.showText(fusion_text)
        self.aft_button.visible = False
        self.forward_button.visible = True





    # ** Content Handlers ** --------------------------------------------------------
    
    def hideText(self, name):
        if name[0].visible:
            for sprite in name:
                sprite.visible = False

    def showText(self, name):
        for sprite in name:
            sprite.visible = True

    def hideAll(self):
        #MAIN
        self.hideText(self.main_text)
        #LOGOUT
        self.logout_image.visible = False
        self.logout_gif.visible = False
        self.hideText(self.logout_text)
        #ABOUT
        self.purpose.visible = False
        self.details.visible = False
        self.personnel.visible = False
        self.sources.visible = False        
        self.hideText(self.purpose_text)
        self.hideText(self.details_text)
        self.hideText(self.personnel_text)
        self.personnel_image1.visible = False
        self.hideText(self.sources_text)
        #EXPLORE
        self.probe_forward_image.visible = False
        self.probe_aft_image.visible = False
        self.forward_plate.visible = False
        self.aft_button.visible = False
        self.forward_button.visible = False
        self.hideText(self.explore_screen_text)
        self.hideText(self.forward_text)
        self.hideText(self.propulsion_text)
        self.hideText(self.communication_text)
        self.hideText(self.sensor_text)
        self.hideText(self.computer_text)
        self.hideText(self.chip_text)
        self.hideText(self.fusion_text)



        
        


