# -*- coding: utf-8 -*-
"""
Created on Sun Aug 08 2021

@author: Haithen BEN ABDELAZIZ
"""

import time, random
from ibmiotf.device import Client
from threading import Thread
import pygame
from utils import *


class Bus(Client):
    """
    Classe bus
    """
    def __init__(self, options, x_pos=60, y_pos=80, temperature=0, img="images/bus.png"):
        """
        Construire u nouveau Objet 'Bus'.
            
         
        :options dict: parametres de connexion de capetur ().
        :x_pos int: position x.
        :y_pos int: position y.
        :temperature int: temperature.
        :img str, optional: chemin de l'image du bus.
            
        """
        self.id = options['id']
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.temperature = temperature
        self.img = pygame.image.load(img)
        self.stop = False
        Client.__init__(self, options)
        Client.commandCallback = self.commandProcessor
    def commandProcessor(self, cmd):
        print("Commande recue: %s" % cmd.data)
        
    def myOnPublishCallback(self, event):
        #print("%s du Bus %s reçue par le Cloud\n" % (event, self.id))
        pass

    def send_temperature(self):
        data = { 'temperature' : self.temperature, 'time' : time.strftime('%x- %X')}
        self.publishEvent("Temperature", "json", data, qos=0, on_publish=self.myOnPublishCallback("Temperature"))
        
    def send_position(self):
        data = { 'x' : self.x_pos, 'y' : self.y_pos, 'time' : time.strftime('%x- %X')}
        self.publishEvent("Position", "json", data, qos=0, on_publish=self.myOnPublishCallback("Position"))
    
    def getPosition(self):
        """
        :return: retourne x position et y position du bus
        :rtype: type est tuple
        """
        return (self.x_pos, self.y_pos)
    
    def getTemperature(self):
        self._calculateTemperature()
        return self.temperature
    
    def setPosition(self, x, y):
        self.x_pos = x
        self.y_pos = y
    
    def setTemperature(self, t):
        self.temperature=t

    def _calculateTemperature(self):
        t = random.randint(8, 25)
        self.setTemperature(t)
