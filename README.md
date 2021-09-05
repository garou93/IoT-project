# Introduction to Internet of things:

Fundamental components of an IoT system: 

1) Sensors/Devices: Sensors or devices are a key component that helps you to collect live data from the surrounding environment. All this data may have various levels of complexities. It could be a simple temperature monitoring sensor, or it may be in the form of the video feed.

A device may have various types of sensors which performs multiple tasks apart from sensing. Example, A mobile phone is a device which has multiple sensors like GPS, camera but your smartphone is not able to sense these things.

2) Connectivity: All the collected data is sent to a cloud infrastructure. The sensors should be connected to the cloud using various mediums of communications. These communication mediums include mobile or satellite networks, Bluetooth, WI-FI, WAN, etc.

3) Data Processing: Once that data is collected, and it gets to the cloud, the software performs processing on the gathered data. This process can be just checking the temperature, reading on devices like AC or heaters. However, it can sometimes also be very complex like identifying objects, using computer vision on video.

4)User Interface: The information needs to be available to the end-user in some way which can be achieved by triggering alarms on their phones or sending them notification through email or text message. The user sometimes might need an interface which actively checks their IoT system. For example, the user has a camera installed in his home. He wants to access video recording and all the feeds with the help of a web server. 

# Simulation of a bus network

`` ``
the full report is in the data / folder
`` ``

## The objective of this work

the objective of this work is to develop an application in the field of connected objects, which consists
to simulate a network of buses and stations, considering that each bus has a sensor which
transmitted its position to the cloud, each bus station receives the position of the buses then calculates the
arrival time of each bus.
The second part of this work is to apply one of the machine learning algorithms
and predict the wait time for each bus.

## Program structure

to analyze the problem, we created 2 class Bus.py and Station.py, a file utils.py
for the utility functions and main.py for the main function.
The bus_predicition.py file analyzes the data collected by the stations, the weather
wait time, then it predicts the wait time with a machine learning algorithm.


#### Class Bus:

The bus class contains 6 attributes and 6 methods:
Id: a unique identifier of integer type for each bus.
Img: an image that represents the bus on the GUI.
Stop: a Boolean variable, true if the bus has stopped.
Temperature: refers to the temperature of the real-type bus, generated in a random fashion.
X_pos: an integer that represents the position of the bus in the GUI relative to the X axis.
Y_pos: an integer that represents the position of the bus in the GUI relative to the Y axis.
setPosition (): a method that is used to initialize the position of the bus.
getPosition (): a method used to get the position of the bus.
sendPosition (): a method that is used to send the position of the bus to the cloud.
setTemperature (): a method used to set the temperature of the bus.
getTemperature (): a method used to retrieve the temperature of the bus.
sendTemperature (): a method used to send the temperature from the bus to the cloud.

#### Station class:

The Bus class contains 7 attributes and 5 methods:
Id: a unique identifier of type integer for each station.
Img: an image that represents the bus station on the GUI.
logger: a log file used to save the data received and the calculated waiting time.
Schedule_bus: list type variable
X_pos: an integer that represents the position of the bus in the GUI relative to the X axis.
Y_pos: an integer that represents the position of the bus in the GUI relative to the Y axis.
setPosition (): a method that is used to initialize the position of the bus.
getPosition (): a method used to get the position of the bus.
sendPosition (): a method that is used to send the position of the bus to the cloud.
setTemperature (): a method used to set the temperature of the bus.
getTemperature (): a method used to retrieve the temperature of the bus.
sendTemperature (): a method used to send the temperature from the bus to the cloud.

#### Random speed generation

Buses advance a single pixel every t second, knowing that t is randomly generated to
simulate a real bus. `` t = time.sleep (uniform (T_MIN, T_MAX)). ''
#### Using Threads

In our application, we used the `` threads '' which are execution units
stand-alone that can perform tasks, in parallel with other threads, such as
for displaying each bus on the graphical interface, and sending data, and

### calculations made by each station.

`` thread_bus_1 = Thread (target = running_bus_1, args = (bus_1, False)). ''

`` thread_bus_1.start (). ''

`` thread_send_data = Thread (target = send_data, args = (bus_1, bus_2, bus_3)). ''

`` thread_send_data.start (). ''

## Machine learning

#### Pre-treatment

First, we collected the data in a log file `` activity.log '' which contains a
activity log of our application in the form of data separated by -
Example :
`` 02/01 / 18- 20:16:36 - 2018 - 131 - 80 - {'2019': 1000.0, '2018': 1000.0, '2020': 1000.0}. ''
Then we deleted the duplicate lines and generated a train.txt file, by the function
delete_duplicate ().
the text_to_csv () function allowed us to select all the data (lines) that
correspond to the 2018 bus and generate a file in csv format `` train.csv '' which will be used in the
prediction of the bus waiting time.
id_bus x_position, y_position wainting_time
2018 141 80 74.


#### Prédiction

Concernant la partie prédiction nous avons implémenté une fonction predict() qui applique la
régression bayésienne pour prédire le temps d'attente du bus 2018.
Le résultat est représenté sous format d’un graphe ci-dessous.


![comparaison des temps d’attente réel, prédis](https://github.com/fr33dz/IoT_bus/blob/master/images/Figure_2.png)



## Référence

[http://www.digitaldimension.solutions/blog/avis-d-experts/2015/02/mqtt-un-protocole-dedie-pour-liot/](http://www.digitaldimension.solutions/blog/avis-d-experts/2015/02/mqtt-un-protocole-dedie-pour-liot/)
[http://www.github.com/ibm-watson-iot/iot-python](http://www.github.com/ibm-watson-iot/iot-python)
https://console.bluemix.net/docs/services/IoT/applications/libraries/python.html#python
https://console.bluemix.net/docs/services/IoT/reference/mqtt/index.html#ref-mqtt
https://winpython.github.io
[http://scikit-learn.org/stable/](http://scikit-learn.org/stable/)
[http://scikit-learn.org/stable/modules/linear_model.html#bayesian-regression](http://scikit-learn.org/stable/modules/linear_model.html#bayesian-regression)

## Captures d'ecran

![screen 1 ](https://github.com/fr33dz/IoT_bus/blob/master/images/gui_1.png)
![screen 2 ](https://github.com/fr33dz/IoT_bus/blob/master/images/gui_2.png)
![screen 3 ](https://github.com/fr33dz/IoT_bus/blob/master/images/gui_3.png)



§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§
# If you like this depo, buy me a Coffee ! =)
- [Neteller](https://www.neteller.com/fr/features/money-transfer) 
 (haithem.ben.abdelaziz@gmail.com)
