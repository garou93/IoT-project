# -*- coding: utf-8 -*-
"""
Created on Sun Aug 08 2021

@author: Haithen BEN ABDELAZIZ
"""
import logging
from logging.handlers import RotatingFileHandler
from ibmiotf.application import Client
import pygame


class Station(Client):
    """
    Classe STATION
     Args:
        id (int): Identifiant unique de la station.
        options (dict): parametres de connexion au Cloud.
        x_pos (int): position x.
        y_pos (int): position y.
        temperature (int): temperature.
        img (str, optional): chemin de l'image du bus.
    """

    def __init__(self, id, x_pos, y_pos, options, img="images/arret.jpg"):
        self.id = id
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.img = pygame.image.load(img).convert()
        self.bus_horaires = {'2018': 100.0, '2019': 200.0, '2020': 300.0}  #Bus 1 , Bus 2 , Bus 3
        self.arret = 0
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)
        formatter = logging.Formatter('%(message)s')
        file_handler = RotatingFileHandler('data/activity.log', 'a', 1000000, 1)
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)
        Client.__init__(self, options)

    def commandProcessor(cmd):
        print("Commande recue: %s" % cmd.data)

    def set_positions_bus(self, event):
        info_type = event.event
        event.timestamp
        bus_id = str.split(event.device, ":")[1]
        x = event.data["x"]
        y = event.data["y"]
        temps = event.data["time"]
        msg = temps+"  -- "+bus_id+" -- "+str(x)+" -- "+str(y)+" -- "+str(self.bus_horaires)
        self.logger.info(msg)
        if y == 80 and x <= 300: # de A à l'arret 1
            if x <= 300 and x > 295: # 20 pixel avant d'arriver a l'arret
                self._addHoraire(bus_id, 0.0) # < 4 s  ou < 10 pixel
            elif x < 290: # + de 20 pixel pr arriver a l'arret
                tmp_attente = round((300 - x)*0.435, 0)
                self._addHoraire(bus_id, tmp_attente)
        elif y == 80 and x > 300: #de l'arret 1  à B
            tmp_attente = round((600 - x + 320 + 540 + 320 + 240)*0.435, 0)
            self._addHoraire(bus_id, tmp_attente)
        elif x == 600 and y > 80:# de B à C
            tmp_attente = round((400 - y + 320 + 540 + 320 + 240)*0.435, 0)
            self._addHoraire(bus_id, tmp_attente)
        elif y == 400 and x < 480:  #de l'arret 2 à C
            # en moyenne le bus fait 1 pixel chaque 0.435 seconde
            tmp_attente = round((x - 60 + 320 + 240)*0.435, 0)
            self._addHoraire(bus_id, tmp_attente)
        elif x == 60 and y < 400: # de C à A
            # en moyenne le bus fait 1 pixel chaque 0.435 seconde
            tmp_attente = round((y - 80 + 240)*0.435, 0)
            self._addHoraire(bus_id, tmp_attente)

    def getHoraires(self):
        horaires = list()
        for temp in self.bus_horaires.values():
            horaires.append(temp)

        horaires.sort()
        for i in range(3):
            if horaires[i] < 1.0:
                horaires[i] = "Bus a l'arret"
            elif horaires[i] < 10.0:
                horaires[i] = "Bus a l'approche"
            else:
                m, s = divmod(horaires[i], 60)
                if m > 0:
                    horaires[i] = str(m)+" m: "+str(s)+" s"
                else:
                    horaires[i] = str(s) + " s"

        return horaires
        #return ['donnees indisponibles', 'donnees indisponibles', 'donnees indisponibles']

    def setPosition(self, x, y):
        self.x_pos = x
        self.y_pos = y

    def setHoraires(self, horaires):
        self.bus_horaires = horaires

    def getData(self, myEventCallback):
        #self.connect()
        self.deviceEventCallback = myEventCallback
        self.subscribeToDeviceEvents(deviceType="Python_client")

    def _addHoraire(self, bus_id, tmp_attente):
        """ Mettre à jour la liste des horaires """
        #Trier par ordre croissant les horaires
        if (all(isinstance(t, float) for t in self.bus_horaires.values())):
            self.bus_horaires[bus_id] = tmp_attente
            #print("Horaires Triées & mis a jour ")
