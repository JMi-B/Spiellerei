import urllib.request, json, time
from datetime import datetime

# Die Daten auslesen und nach Json schreiben
# Vorlage test1.py
# Ziel ist ein übersichtlicher Code 

#funktion um Daten abzurufen

def aktuelle_daten_api_abholen():
    url = "https://open-data.dortmund.de/api/explore/v2.1/catalog/datasets/parkhauser/records?limit=40"
    response = urllib.request.urlopen(url)
    json_data = json.load(response)
    return json_data

# json mit Historischen daten aufrufen

def historische_daten_json_einlesen():
    with open('c:\\Users\\juliane.bonenkamp\\src\\JMiArbeit\\historische_daten02.json', 'r') as file:
        eingelesene_daten = json.load(file)
        #Timetamp formatieren
       # for entry in eingelesene_daten["Resultate"]:
        #    if (hasattr(entry, "Zeitstempel lesbar") != True):
         #       zeitstempel_lesbar = datetime.fromtimestamp(entry["Zeitstempel"]).strftime("%Y-%m-%d %H:%M")
          #      entry["Zeitstempel lesbar"] = zeitstempel_lesbar
 
        print(eingelesene_daten)
        return eingelesene_daten

# neuen Datensatz zu Historischen Daten in Json schreiben hinzufügen

def datensatz_historischen_daten_hinzufuegen(neuer_eintrag, historische_daten):
    historische_daten["Resultate"].append(neuer_eintrag)
    with open('c:\\Users\\juliane.bonenkamp\\src\\JMiArbeit\\historische_daten02.json', 'w') as file:
        json.dump(historische_daten, file)

# Datenverarbeiten 
# weiter Informaitonen dazu 

def daten_verarbeiten(aktuelle_information):
    count = 0
    countParkAndRide = 0
    
    summecapa = 0
    summebelegt = 0
    summefrei = 0
    kurzcapa = 0
    kurzbelegt = 0
    anteilsumme = 0
    zeitstempel = time.time()
    zeitstempel_lesbar = datetime.fromtimestamp(zeitstempel).strftime("%Y-%m-%d %H:%M")


    for entry in aktuelle_information["results"]:
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
        

    #print("\n")
    #print(zeitstempel)
    #print(zeitstempel_lesbar)
    #print("Anzahl: " + str(count))
    #print("Anzahl Park and Ride: " + str(countParkAndRide))
    #print("Summe aller Parkplätze: " + str(summecapa))
    #print("Summe aller belegten Parkplätze: " + str(summebelegt))
    #print("Summe der feien Parkplätz: " + str(summefrei))
    #print("Anteil der belegten Parkplätze: "+ str(anteilsumme))
    #print("Summe Kurzzeitparkplätze: " + str(kurzcapa))
    #print("Summe aller belegten Kurzzeitparkplätze: " + str(kurzbelegt))
    #print("Summe der feien Kurzzeit Parkplätze: " + str(kurzfrei))
    #print("Anteil der  Kurzzeit an den freien Parkplätze: " + str(anteilkurzfrei))

    neuer_eintrag = {
    "Zeitstempel" : zeitstempel_lesbar,
    #"Zeitstempel lesbar": zeitstempel_lesbar,
    "Anzahl" : count,
    "Anzahl Park and Ride" : countParkAndRide,
    "Alle Parkplätze" : summecapa,
    "Belegte Parkplätze" : summebelegt,
    "Freie Parkplätze" : summefrei,
    "Anteil der Belegung an allen" : anteilsumme,
    "Kurzzeit Parkplätze" : kurzcapa,
    "Belegte Kurzzeit Parkplätze" : kurzbelegt,
    "Freie Kurzzeit Parkplätze" : kurzfrei,
    "Anteil Kurzzeita an freien Parkplätze" : anteilkurzfrei


    }
    
    return neuer_eintrag

# funktionen aufrufen und durch führen

aktuelle_information = aktuelle_daten_api_abholen()
historische_daten = historische_daten_json_einlesen()
neuer_eintrag = daten_verarbeiten(aktuelle_information)
datensatz_historischen_daten_hinzufuegen(neuer_eintrag,historische_daten)

# Variablen für Summe der capacety und der belegten Prakplätze

#summecapa = 0
#summebelegt = 0
#anteil = 0


# capacity auslesen und zeilen weise print und auf addieren


# for entry in aktuelle_information["results"]:
 #   print("\n")
 #   print(entry["capacity"])
 #   print(entry["dtotalo"])
    # summecapa = summecapa + entry["capacity"]
    # summebelegt = summebelegt + entry["dtotalo"]
    # anteil = (summebelegt/summecapa) * 100
#print("Summe aller Parkplätze: " + str(summecapa))
#print("Summe aller belegten Parkplätze: " + str(summebelegt))
#print(anteil)


