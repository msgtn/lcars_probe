import time
import serial

a_exist = False

def connect_arduino():
    try:
        a = serial.Serial('/dev/ttyACM0', 9600)
        a_exist = True
        return a
    except:
        pass

def red_thruster(a, on_off):
    if (on_off):
        a.write('q')
    else:
        a.write('a')

def blue_thruster(a, on_off):
    if (on_off):
        a.write('w')
    else:
        a.write('s')

def yellow_dome(a, on_off):
    if (on_off):
        a.write('e')
    else:
        a.write('d')

def white_dome(a, on_off):
    if (on_off):
        a.write('r')
    else:
        a.write('f')

def glass(a, on_off):
    if (on_off):
        a.write('t')
    else:
        a.write('g')
    
def control_led(a, led_num, on_off):
    if (led_num == 1):
        if (on_off):
            a.write('q')
        else:
            a.write('a')
    elif (led_num == 2):
        if (on_off):
            a.write('w')
        else:
            a.write('s')
    elif (led_num == 3):
        if (on_off):
            a.write('e')
        else:
            a.write('d')
    elif (led_num == 4):
        if (on_off):
            a.write('r')
        else:
            a.write('f')
    elif (led_num == 5):
        if (on_off):
            a.write('t')
        else: a.write('g')

def door_fr(a, open_close):
    if (open_close):
        a.write('i')
    else:
        a.write('k')
    time.sleep(1)

def door_fl(a, open_close):
    if (open_close):
        a.write('o')
    else:
        a.write('l')
    time.sleep(1)

def door_br(a, open_close):
    if (open_close):
        a.write('p')
    else:
        a.write(';')
    time.sleep(1)

def door_bl(a, open_close):
    if (open_close):
        a.write('[')
    else:
        a.write('\'')
    time.sleep(1)

def servo_pos_test(a, ang):
    a.write(str(ang))
    time.sleep(2)
