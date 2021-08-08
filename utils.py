# -*- coding: utf-8 -*-
"""
Created on Sun Aug 08 2021

@author: Haithen BEN ABDELAZIZ
"""
import os, time
from random import uniform
from ibmiotf.application import ParseConfigFile as ReadCfgStation
from ibmiotf.device import ParseConfigFile as ReadCfgDevice
import pygame


POINT_A = 60
POINT_B = 80
POINT_C = 400
POINT_D = 600
WIDTH = 800
HEIGHT = 600
BREAK_TIME = 10 # Temps d'arret a la station de bus
DEADLINE_SENDING_DATA = 3 # periode d'envoie de donnees au Cloud
T_MIN = 0.15
T_MAX = 0.45
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Simulation Bus')
clock = pygame.time.Clock()
clock.tick(65)
circuit_img = pygame.image.load("images/circuit.png")
myfont = pygame.font.SysFont("arial", 12, True)
bus1_h = myfont.render("15 min ", 1, (0,0,0))
bus2_h = myfont.render("25 min ", 1, (0,0,0))
config_path = os.getcwd()+'/config/'
bus1_options = ReadCfgDevice(config_path+'config_bus_1.cfg')
bus2_options = ReadCfgDevice(config_path+'config_bus_2.cfg')
bus3_options = ReadCfgDevice(config_path+'config_bus_3.cfg')
station1_options = ReadCfgStation(config_path+'config_station.cfg')


def sleep():
    """
    - Fonction qui retourne un reel t  en secondes
    - t est choisie d'une maniere aleatoire entre T_MAX t T_MIN
    - Utilisé dans le mouvement des bus
    - Les bus avance de 1 pixel chaque t seconde
    - La fenetre d'affichage est mis a jour chaque t
    """
    time.sleep(uniform(T_MIN, T_MAX))


def running_bus_1(bus, stop):
    """
    :bus (Bus): bus.
    :stop (boolean): Condition d'arret.
    """
    while not stop:
        ##Arrets
        if bus.x_pos == 300 and bus.y_pos == 80: #arret 1
            time.sleep(BREAK_TIME)
        if bus.x_pos == 500 and bus.y_pos == 400: #arret 2
            time.sleep(BREAK_TIME)
        ##Mouvement bus 1
        if bus.x_pos < POINT_D and bus.y_pos == POINT_B:
            bus.x_pos += 1
        elif bus.x_pos == POINT_D and bus.y_pos < POINT_C:
            bus.y_pos += 1
        elif bus.y_pos == POINT_C and bus.x_pos > POINT_A:
            bus.x_pos -= 1
        elif bus.x_pos == POINT_A and bus.y_pos > POINT_B:
            bus.y_pos -= 1
        sleep()
        #print("id :%s x:%d - y:%d " % (bus.id, bus.x_pos, bus.y_pos))


def running_bus_2(bus, stop):
    while not stop:
         ##Arrets
        if bus.x_pos == 300 and bus.y_pos == 80: #arret
            time.sleep(BREAK_TIME)
        if bus.x_pos == 500 and bus.y_pos == 400: #arret
            time.sleep(BREAK_TIME)
        if bus.x_pos < POINT_D and bus.y_pos == POINT_B:
            bus.x_pos += 1
        elif bus.x_pos == POINT_D and bus.y_pos < POINT_C:
            bus.y_pos += 1
        elif bus.y_pos == POINT_C and bus.x_pos > POINT_A:
            bus.x_pos -= 1
        elif bus.x_pos == POINT_A and bus.y_pos > POINT_B:
            bus.y_pos -= 1
        sleep()
        #print("id :%s x:%d - y:%d " % (bus.id, bus.x_pos, bus.y_pos))


def running_bus_3(bus, stop):
    while not stop:
         ##Arrets
        if bus.x_pos == 300 and bus.y_pos == 80: #arret 1
            time.sleep(BREAK_TIME)
        if bus.x_pos == 500 and bus.y_pos == 400: #arret 2
            time.sleep(BREAK_TIME)
        if bus.x_pos < POINT_D and bus.y_pos == POINT_B:
            bus.x_pos += 1
        elif bus.x_pos == POINT_D and bus.y_pos < POINT_C:
            bus.y_pos += 1
        elif bus.y_pos == POINT_C and bus.x_pos > POINT_A:
            bus.x_pos -= 1
        elif bus.x_pos == POINT_A and bus.y_pos > POINT_B:
            bus.y_pos -= 1
        sleep()
        #print("id :%s x:%d - y:%d " % (bus.id, bus.x_pos, bus.y_pos))


def screen_update(bus1, bus2, bus3, station1, station2, stop=False): #station2
    """ Mis à jour de la fenetre d'affichage
        - Affichage du circuit , Stations, Bus ..."""
    while not stop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                stop = True
        screen.blit(circuit_img,(0, 0))
        screen.blit(station1.img, (station1.x_pos, station1.y_pos))
        screen.blit(station2.img, (station2.x_pos, station2.y_pos))
        screen.blit(bus1.img, (bus1.x_pos, bus1.y_pos))
        screen.blit(bus2.img, (bus2.x_pos, bus2.y_pos))
        screen.blit(bus3.img, (bus3.x_pos, bus3.y_pos))
        horaires = station1.getHoraires()
        bus1_h = myfont.render(str(horaires[0]).encode('utf-8'), 1, (0,0,0))
        bus2_h = myfont.render(str(horaires[1]).encode('utf-8'), 1, (0,0,0))
        screen.blit(bus1_h, (330, 35)) # Horaire Bus 1
        screen.blit(bus2_h, (330, 55)) # Horaire Bus 2
        pygame.display.update()
        sleep()


def send_data(bus1, bus2, bus3, stop=False):
    """ Envoyer les donnees des bus au Cloud"""
    while not stop:
        bus1.send_position()
        bus2.send_position()
        bus3.send_position()
        time.sleep(DEADLINE_SENDING_DATA)
