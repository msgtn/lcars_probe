from screens.main import ScreenMain
from ui.ui import UserInterface

# global config
UI_PLACEMENT_MODE = True
RESOLUTION = (800, 480)
FPS = 60
DEV_MODE = True

if __name__ == "__main__":
    firstScreen = ScreenMain()
    ui = UserInterface(firstScreen, RESOLUTION, UI_PLACEMENT_MODE, FPS, DEV_MODE)

    while (True):
        ui.tick()
