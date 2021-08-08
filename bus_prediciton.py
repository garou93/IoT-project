import ast
import os
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
__author__ = 'Haithem BEN ABDELAZIZ'

path = os.getcwd()
infile = path+'/data/activity.log' # Fichier log
outfile_txt = '/data/train.txt' # Fichier generer a partir du Fichier log
outfile_csv = '/data/train.csv' # Fichier final utilisé pour predire le temps d'attente du Bus 2018


def delete_duplicate():
    """ Supprimer les lignes dupliquees et Generer un fichier txt"""
    s = set()
    with open(outfile_txt, 'w') as out:
        for line in open(infile):
            if line not in s:
                out.write(line)
                s.add(line)


def text_to_csv():
    """ Mdifier le format du fichier de :
        02/01/18- 20:16:54  -- 2018 -- 192 -- 80 -- {'2019': 217.0, '2018': 52.0, '2020': 676.0}
        vers :  2018,192,80,52.0
    """
    with open(outfile_csv, 'w') as out:
        for line in open(outfile_txt):
            line.strip()
            l = line.split('--')
            #date_time = l[0].split('-')
            w_time = str(l[4]).translate(None," { } ' \n ").split(',')# [2019: 217.0, 2018: 52.0, 2020: 676.0]
            waiting_time = 0.0
            for i in range(3):

                if (w_time[i].find(str(l[1]).strip())) != -1:
                    #print("boucle + if")
                    waiting_time = w_time[i].split(':')[1]
            new_line = l[1]+","+l[2]+","+l[3]+","+str(waiting_time)#sans datetime
            
            #waiting_time = l[4]
            #new_line = l[0]+","+l[1]+","+l[2]+","+l[3]+","+str(waiting_time)#avec tous les champs
            #new_line = date_time[0]+","+date_time[1]+","+l[1]+","+l[2]+","+l[3]+","+str(waiting_time)
            if l[1]==" 2018 ":
                out.write(new_line+"\n")


def predict():
    """ Fonction qui applique la regression Bayes pour prédire le temps d'attente du bus id 2018"""
    data = np.loadtxt(open(path+"/data/train.csv", "rb"), delimiter=",", skiprows=1) #Importer le fichier  csv
    X = data[:,1:3] # Selectioner x_position et y_position comme variables d entrees
    y = data[:, 3] # Selectioner temps d'attente come variable de sotie

    reg = linear_model.BayesianRidge(compute_score=True)
    reg.fit(X, y)
    predicted = reg.predict(X)
    plt.plot(y,  color='navy', linewidth=2, label="Real Waiting Time")
    plt.plot(predicted, color='red', linewidth=0.5, label="Predicted Waiting Time")
    plt.title('Bayesian Regression', fontsize=12)
    plt.ylabel("Waiting time (s)")
    x = [32, 209]
    labels = ['Station', 'Station']
    labels
    plt.xticks(x, labels, rotation='vertical')
    plt.xlabel("Distance")
    plt.legend()
    plt.show()

if __name__ == '__main__':
    #preprocessing
    #delete_duplicate()
    #text_to_csv()
    #prediction
    predict()
    print("Exit")
