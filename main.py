# -*- coding: utf-8 -*-


__author__ = "Haithem BEN ABDELAZIZ <haithem.ben.abdelaziz@gmail.com>"
__date__ = "08 August 2021"
__version__ = "Revision: 1.0 "


import time
from threading import Thread
import pygame
from bus import Bus
from station import Station
from utils import *

pygame.init()
def myEventCallback(event):
    #Informer la station
    station_1.set_positions_bus(event)

bus_1 = Bus(options=bus1_options, x_pos=120, y_pos=80, temperature=15)
bus_2 = Bus(options=bus2_options, x_pos=60, y_pos=400, temperature=15)
bus_3 = Bus(options=bus3_options, x_pos=600, y_pos=200, temperature=15)
station_1 = Station(id=1, x_pos=300, y_pos=35, options=station1_options)
station_2 = Station(id=1, x_pos=500, y_pos=355, options=station1_options)

thread_bus_1 = Thread(target=running_bus_1, args=(bus_1, False))
thread_bus_1.start()
thread_bus_2 = Thread(target=running_bus_2, args=(bus_2, False))
thread_bus_2.start()
thread_bus_3 = Thread(target=running_bus_3, args=(bus_3, False))
thread_bus_3.start()
thread_screen_up = Thread(target=screen_update, args=(bus_1, bus_2, bus_3, station_1, station_2))
thread_screen_up.start()
####################################

bus_1.connect()
bus_2.connect()
bus_3.connect()
#Les bus enovient leurs donnees
thread_send_data = Thread(target=send_data, args=(bus_1, bus_2, bus_3))
thread_send_data.start()
station_1.connect()
station_1.getData(myEventCallback)

#####################################
#time.sleep(60)
#thread_send_data._stop()
#station_1._stop()
#bus_1.disconnect()
#bus_2.disconnect()
#bus_3.disconnect()
#thread_bus_1._stop()
#thread_bus_2._stop()
#thread_bus_3._stop()

#pygame.quit()

# TODO: Test bus class - Connection , publishing ,
# TODO: Test Station Class -
# TODO: Add threading
# TODO: Integrate the GUI
# 
# TODO : replace the 3 config file to 1 file API
# TODO : tri des horaires
# TODO : Documentaion
