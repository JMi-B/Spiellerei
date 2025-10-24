# Direkt in SQL schreiben
#import
import urllib.request, json, time
from datetime import datetime
import mysql.connector

# api abrufen
url = "https://open-data.dortmund.de/api/explore/v2.1/catalog/datasets/parkhauser/records?limit=40"

response = urllib.request.urlopen(url)

data = json.load(response)

# print(data)

# mit db verbinden
# Verbindung zur Datenbank
mydb = mysql.connector.connect(
     host='localhost',
     user='Parken',
     password='Plaetze',
     database='parken'
 )

# Curser setzen
mycursor = mydb.cursor()


# daten auswählen und verarbeiten

count = 0
countParkAndRide = 0
    
summecapa = 0
summebelegt = 0
summefrei = 0
kurzcapa = 0
kurzfrei = 0
kurzbelegt = 0
anteilsumme = 0
anteilkurzfrei = 0
zeitstempel = time.time()
zeitstempel_lesbar = datetime.fromtimestamp(zeitstempel).strftime("%Y-%m-%d %H:%M")


for entry in data["results"]:
    count += 1
    if (entry["type"] == "Park and Ride"):
        countParkAndRide += 1

    summecapa = summecapa + entry["capacity"]
    summebelegt = summebelegt + entry["dtotalo"]
    summefrei = summecapa - summebelegt
    
    kurzcapa = kurzcapa + entry["short"]
    kurzbelegt = kurzbelegt + entry["dshorto"]
    kurzfrei = kurzcapa - kurzbelegt
    
    # nicht durch Nullteilen
        
    if summecapa == 0:
        anteilsumme = 0
    else: anteilsumme = (summebelegt/summecapa) * 100
    
    
    if summefrei == 0:
        anteilkurzfrei = 0
    else: anteilkurzfrei = (kurzfrei/summefrei) * 100
    
mycursor.execute("Insert into plaetze(Zeitstempel, Anzahl, AnzahlPR, AllePP, BelegtPP, FreiPP, AnteilAlle, KurzPP, KurzBelegt, KurzFrei, AnteilKurz) Values ('"+ str(zeitstempel_lesbar) +"','"+ str(count) + "','" + str(countParkAndRide) + "',' " + str(summecapa) + "',' " + str(summebelegt) + "',' " + str(summefrei) +"',' " + str(anteilsumme) + "',' " + str(kurzcapa) +" ',' " + str(kurzbelegt) +"', '" +str(kurzfrei)+ "','" +str(anteilkurzfrei) +"') ")
    

    # print("\n")
    # print(zeitstempel)
    # print(zeitstempel_lesbar)
    # print("Anzahl: " + str(count))
    # print("Anzahl Park and Ride: " + str(countParkAndRide))
    # print("Summe aller Parkplätze: " + str(summecapa))
    # print("Summe aller belegten Parkplätze: " + str(summebelegt))
    # print("Summe der feien Parkplätz: " + str(summefrei))
    # print("Anteil der belegten Parkplätze: "+ str(anteilsumme))
    # print("Summe Kurzzeitparkplätze: " + str(kurzcapa))
    # print("Summe aller belegten Kurzzeitparkplätze: " + str(kurzbelegt))
    # print("Summe der feien Kurzzeit Parkplätze: " + str(kurzfrei))
    # print("Anteil der  Kurzzeit an den freien Parkplätze: " + str(anteilkurzfrei))




# in db schreiben
#Daten einfügen


    # mycursor.execute("Insert into plaetze(Zeitstempel, Anzahl, AnzahlPR, AllePP, BelegtPP, FreiPP, AnteilAlle, KurzPP, KurzBelegt, KurzFrei, AnteilKurz) Values ('zeitstempel_lesbar','count','countParkAndRide','summecapa', 'summebelegt','summefrei','anteilsumme','kurzcapa','kurzbelegt','kurzfrei','anteilkurz') ")
    # mycursor.execute("Insert into plaetze(Zeitstempel, Anzahl, AnzahlPR, AllePP, BelegtPP, FreiPP, AnteilAlle, KurzPP, KurzBelegt, KurzFrei, AnteilKurz) Values ('"+ str(entry["Zeitstempel"]) +"','"+ str(entry["Anzahl"]) +"','"+ str(entry["Anzahl Park and Ride"]) +"','"+ str(entry["Alle Parkplätze"]) +"', '"+ str(entry["Belegte Parkplätze"]) +"','"+ str(entry["Freie Parkplätze"]) +"','"+ str(entry["Anteil der Belegung an allen"]) +"','"+ str(entry["Kurzzeit Parkplätze"]) +"','"+ str(entry["Belegte Kurzzeit Parkplätze"]) +"','"+ str(entry["Freie Kurzzeit Parkplätze"]) +"','"+ str(entry["Anteil Kurzzeita an freien Parkplätze"]) +"') ")
    
mydb.commit()

#Datenbank trennen
mydb.close()