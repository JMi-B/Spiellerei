#python 
Tipps und Tricks
Zeilenumbruch bei langem insert 
sql = "insert into tabele(col1, col2)values(%s,%s)
data =(variable1,variable2)
mycursor.execute(sql,data)

 **Anzahl der Werte in einer Zeile**
	meine_zeile_als_liste = ["WertA", "WertB", "WertC"]
    anzahl_elemente = len(meine_zeile_als_liste)
    print(f"Anzahl der Elemente in der Liste: {anzahl_elemente}") # Ausgabe: Anzahl der Elemente in der Liste: 3
## Variablen
#variablen
- Benennung nach Funktionalität und Inhalt
- eindeutig machen
	- Funktion in jedem Programm / Schleife die gleiche
	- Um sie zu definieren mir einen Satz aufschreiben
		- "Für jedes Wort aus dem Text erstelle ich ein Dictionary mit Key und Wert"
#### Häufige Variablen für Funktionalitäten
list für eine Liste
entry für einen Eintrag in einer Liste
dict für ein Dictionary
key für den Schlüssel im Schlüssel-Wert-Paar
value für den Wert im Schlüssel-Wert-Paar
text für einen string
string für einen string
letter für einen Buchstaben in einem String
i für Intiger in einer Bedingung
file für ein File (eine eingelesene Datei)
db für eine Datenbank

Diese Variablen können speziaisiert werden für den Zweck für den sie gebraucht werden.
aus thisdict = dict()

## Listen und Dictionary
#### List
- Eine Liste wird in eckigen Klammern geschrieben [] 
- Die Einträge sind durch Kommata getrennte
- Strings stehen in ""
#### Dict
- Ein Dictionaty steht in {} geschweiften Klammern
- Ein Dictionary besteht aus SChlüsel-Wert-Paaren (Key:Value)
- Die Schlüssel und Wert (Key:Value) wird ein Doppelpunkt gesetzt
- Die Paar werden durch Kommata getrennt
- Strings stehen in ""

[[Schleifen]]
- [[Schleifen#Liste auslesen|Liste auslesen]]
- [[Schleifen#Directory auslesen|Directory auslesen]]
- [[Schleifen#Loop über String|Loop über String]]
- [[Schleifen#Range|Range]]
- [[Schleifen#Range mit condinue|Range mit condinue]]
- [[Schleifen#Range mit break|Range mit break]]
- [[Schleifen#While-Schleife|While-Schleifen]]
- [[Schleifen#Kleiner als 5|Kleiner als 5]]
- [[Schleifen#kleiner Gleich 5|kleiner Gleich 5]] 
- [[Schleifen#Endlosschleife|Endlosschleife]]

## Leerzeichen entfernen
Was tun mit den Leerzeichen? Sie werden mit eingelesen und von Py beim Austausch von Goblingogh Zeichen erzeugt.
- Identifizieren mit `zeichen.isspace()`
- Nicht mit ins Directory übergeben durch zusätzliches `if` 
	`if zeichen.isspace() or len(zeichen) == 0 : ## leerzeichen löschen       continue
	`if zeichen in thisdict: ### zählen der Buchstaben
	  `thisdict[zeichen] += 1
   `else:
        `thisdict[zeichen] = 1`


## Zeichensatz
Problem:
- Text wird von Python eingelesen. 
- Py erkennt Deutsche Sonderzeichen nicht
	- Lösung: 
	## `Datei einlesen`
	`with open('WordcloudDE.txt', 'r', encoding='utf-8') as file:`
    `text = file.read()`
	 - Zeichensatz beim einlesen mit geben.
 - Die Sonderzeichen werden in der Datenbank angezeigt bei `select group by` gehen sie wieder verloren
	 - Lösung
		 - Die DB oder die Col mit dem richtigen Zeichensatz anlegen
		 - Kollation utf8_german2_ci
Das ist eins der Probleme warum ich den Beruf ergreife. Das ist ein alltägliches Problem, dass immer wieder auftritt. Man muss die Zusammenhänge verstehen um es zu lösen.

# [[OpenCV]]
# [[EXIF]]
[[EXIF#Funktion|Funktion]]
# DataFrame
#csv #Pandas 
`df= pd.read_csv(csv_path, encoding='latin-1', sep=";")
Wenn in der csv Datei ein anderes Trennzeichen als ein `,` genutzt wird kann Pandas das nicht lesen. Deshalb `sep=` als Paramenter übergeben. **Das hat mir exl eingebrockt**

