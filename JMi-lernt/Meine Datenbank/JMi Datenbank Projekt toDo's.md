#sql #dbmodel #python #elt #meineRegel #workflow 
- Achte drauf die Variablen in der richtigen Reihenfolge zu übergeben. 
	- **Meine Regel: in der Reihenfolge wie sie in der DatenCSV steht, werden die Variablen und Parameter übergeben.**
- [x] ERM des aktuellen Stands der Datenbank
	- [x] Reinfolge der Befüllung
	- [x] unnötige FK löschen
	- [ ] constraint für pdftexte berichtigen
- [ ] Projekttabelle
	- [ ] Abhänigkeit zu festlegen ZwischenTabellen
		- Technik
		- Gegenstand
		- Medien
	- In AnleitungDB04 rausgenommen um das Eingaben zu erleichtern
- [x] DB füllen
- [x] Funktionen #funktion 
	- [x] Insert Medium
	- [x] Insert Buch
	- [x] Insert Autor
	- [x] insert Anleitung
- [x] n:m-Verbindnungen zur AutorTabelle
- [ ] Weitere Medienarten
	- [x] Zeitschriften
	- [x] pdf
		- [x] wie sieht die Tabelle für pdfs aus
	- [ ] Erweiterung der Tabelle Schnittmuster für PDFs
		-  Manche Schnittmuster sind PDFs
			- Diese müssen ausgedruckt werden
			- Aufruf der Datei aus der DB heraus
	- [ ] 
- [x] Dubletten vermeiden
	- [x] medium
		- [x] Buch
		- [x] Zeitschrift
	- [x] Autor
	- [x] Anleitung
		- [x] Zwischentabelle
- [ ] Verbindung mit der Datenbank nicht von Anfang an öffnen
	- [x] Daten auslesen und in Json schreiben
	- [x] aus Json insert in DB
		- Brauche ich mehrere Json ?
	- Macht beim normalem Befüllen keinen Sinn
		- Für pdf oder einzelne Tabellen 
- [ ] Einlesen von Texten in die DB
	- [ ] py aus der alten Vorlage neu bauen
		- [ ] Text erstellen
		- [ ] jpg aufräumen
	- [ ] DB Anbindung erst nach dem alle Texte erstellt sind
		- [x] Zwischenspeichern als txt
# Regeln für meine Datensätze
| Tabelle   | Spalte        | Enum        | Typ  | Schlüssel | Null |
| --------- | ------------- | ----------- | ---- | --------- | ---- |
| medium    | MediumID      |             | Int  | PK        | NN   |
|           | TitelMedium   |             | var  |           | NN   |
|           | MedienArt     |             | enum |           | NN   |
|           |               | Buch        |      |           |      |
|           |               | Zeitschrift |      |           |      |
|           |               | Flyer       |      |           |      |
|           |               | Datei       |      |           |      |
|           |               | Website     |      |           |      |
| Anleitung | AnleitungID   |             | Int  | PK        | NN   |
|           | NameAnleitung |             | var  |           | NN   |
|           | Seitenzahl    |             | int  |           | NN   |
|           | MediumID      |             | Int  | FK        | NN   |
| Autor     | AutiorID      |             | int  | PK        | NN   |
|           | Nachname      |             | var  |           |      |
|           | Vorname       |             | var  |           |      |
|           | Firma         |             | var  |           |      |