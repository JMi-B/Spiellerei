[[Einzelne Aufgabenblöcke#Datengrundlage]]
# Beschreibung
Die Probe Datenbank wird in SQl erstellt. Aus den vorgegebenen Daten werden anhand der Aufgabenstellungen Einsparmöglichkeiten ermittelt. Ich gebe aufgrund meiner Datenanalyse Handlungsempfelungen für die Zukunft.
# Akzepranzkriterien
- Die Datenbank funkitoniert und enthält alle vorgebenen DAtne
- Die Aufgaben 1-3 bilden die Grundlage für das weiterere Verogehn.
	- Aufgrund der groben Übersicht entscheide ich welche Aufgaben ich weiter bearbeite
	- 4 -5 Folien
- Das Einsparmöglichkeiten an hand der Aufgaben. 
	- Begründete Entscheidung für meinen Weg
	- Begründete Vorschläge für weiteres Vorgehen.
	- 4-5 Folien
# Umsetzung
- [x] Uml Model
	- [x] Welche Tabelle hängt von welcher ab
		- wichtig für das füllen
- wenn es mir die Zusammenhänge erklärt
- als Optischer Anreiz für die Präsentation
- [ ] Datenbank anlegen
- [ ] Einzel Fragen Grundlagen
	- [ ] Bestandsaufnahme
	- [ ] Kosten pro Lizenz
	- [ ] Nutzung je Lizenzvertrag
- [ ] Einzel Fragen Vertiefung
# Datenbank
## Tabellen
- bibliothek
- benutzerrollen
- nutzer
- lizenzmodell
- lizensvertrag
- lizenznutzung
## Insert
- lizenznutzung hat Anmerkungen zur Nutzungsintensität
## SQL Code

`CREATE TABLE bibliothek (`
    `id INT IDENTITY(1,1) PRIMARY KEY,`
    `name VARCHAR(100) NOT NULL,`
    `typ VARCHAR(50) NOT NULL`
`);`

`CREATE TABLE benutzerrolle (`
    `id INT IDENTITY(1,1) PRIMARY KEY,`
    `bezeichnung VARCHAR(50) NOT NULL`
`);`

`CREATE TABLE nutzer (`
    `id INT IDENTITY(1,1) PRIMARY KEY,`
    `name VARCHAR(100) NOT NULL,`
    `bibliothek_id INT NOT NULL,`
    `benutzerrolle_id INT NOT NULL,`
    `CONSTRAINT fk_nutzer_bibliothek`
        `FOREIGN KEY (bibliothek_id) REFERENCES bibliothek(id),`
    `CONSTRAINT fk_nutzer_rolle`
        `FOREIGN KEY (benutzerrolle_id) REFERENCES benutzerrolle(id)`
`);`

`CREATE TABLE lizenzmodell (`
    `id INT IDENTITY(1,1) PRIMARY KEY,`
    `name VARCHAR(50) NOT NULL,`
    `beschreibung VARCHAR(255),`
    `max_aktive_nutzer INT NULL`
`);`

`CREATE TABLE lizenzvertrag (`
    `id INT IDENTITY(1,1) PRIMARY KEY,`
    `bibliothek_id INT NOT NULL,`
    `lizenzmodell_id INT NOT NULL,`
    `anbieter VARCHAR(100) NOT NULL,`
    `startdatum DATE NOT NULL,`
    `enddatum DATE NOT NULL,`
    `anzahl_lizenzen INT NOT NULL CHECK (anzahl_lizenzen > 0),`
    `kosten_gesamt DECIMAL(10,2) NOT NULL CHECK (kosten_gesamt >= 0),`
    `CONSTRAINT fk_lv_bibliothek`
        `FOREIGN KEY (bibliothek_id) REFERENCES bibliothek(id),`
    `CONSTRAINT fk_lv_lizenzmodell`
        `FOREIGN KEY (lizenzmodell_id) REFERENCES lizenzmodell(id)`
`);`

`CREATE TABLE lizenznutzung (`
    `id INT IDENTITY(1,1) PRIMARY KEY,`
    `lizenzvertrag_id INT NOT NULL,`
    `nutzer_id INT NOT NULL,`
    `nutzungsdatum DATE NOT NULL,`
    `dauer_minuten INT NOT NULL CHECK (dauer_minuten >= 0),`
    `aktion VARCHAR(50) NOT NULL,`
    `CONSTRAINT fk_ln_lv`
        `FOREIGN KEY (lizenzvertrag_id) REFERENCES lizenzvertrag(id),`
    `CONSTRAINT fk_ln_nutzer`
        `FOREIGN KEY (nutzer_id) REFERENCES nutzer(id)`
`);`

`INSERT INTO bibliothek (name, typ) VALUES`
	`('Stadtbibliothek Mitte', 'Öffentlich'),`
	`('Stadtteilbibliothek Nord', 'Öffentlich'),`
	`('Stadtteilbibliothek Süd', 'Öffentlich'),`
	`('Uni-Bibliothek Campus', 'Wissenschaftlich'),`
	`('Fachhochschulbibliothek', 'Wissenschaftlich'),`
	`('Landesbibliothek', 'Öffentlich'),`
	`('Schulbibliothek Gymnasium A', 'Schule'),`
	`('Schulbibliothek Gymnasium B', 'Schule'),`
	`('Schulbibliothek Gesamtschule', 'Schule'),`
	`('Kirchliche Bibliothek St. Paul', 'Spezial'),`
	`('Musikbibliothek Stadt', 'Spezial'),`
	`('Kinder- und Jugendbibliothek', 'Öffentlich'),`
	`('Digitale Bibliothek Region', 'Virtuell'),`
	`('Archivbibliothek Stadtarchiv', 'Spezial'),`
	`('Technische Bibliothek Industriepark', 'Spezial'),`
	`('Krankenhausbibliothek', 'Spezial'),`
	`('Firmenbibliothek IT-Unternehmen', 'Firmenintern'),`
	`('Firmenbibliothek Ingenieurbüro', 'Firmenintern'),`
	`('Gemeindebibliothek Dorf A', 'Öffentlich'),`
	`('Gemeindebibliothek Dorf B', 'Öffentlich');`

`INSERT INTO benutzerrolle (bezeichnung) VALUES`
	`('Bibliothekar'),`
	`('Verwaltung'),`
	`('IT-Administrator'),`
	`('Leitung'),`
	`('Student'),`
	`('Schüler'),`
	`('Externer Forscher'),`
	`('Ehrenamtlicher'),`
	`('Praktikant'),`
	`('Auszubildender'),`
	`('Dozent'),`
	`('Professor'),`
	`('Archivmitarbeiter'),`
	`('Dokumentar'),`
	`('Medienpädagoge'),`
	`('Systembetreuer'),`
	`('Sachbearbeiter Lizenzen'),`
	`('Hausmeister'),`
	`('Projektmitarbeiter'),`
	`('Gastnutzer');`

`INSERT INTO nutzer (name, bibliothek_id, benutzerrolle_id) VALUES`
	`('Anna Schmidt', 1, 1),`
	`('Max Meier', 1, 2),`
	`('Lisa Keller', 4, 5),`
	`('Tom Schulz', 4, 11),`
	`('Julia Braun', 2, 1),`
	`('Peter Wolf', 3, 1),`
	`('Sabine König', 5, 12),`
	`('Markus Lange', 5, 3),`
	`('Laura Krüger', 6, 4),`
	`('Tim Becker', 7, 6),`
	`('Sarah Hoffmann', 8, 6),`
	`('Jonas Weber', 9, 6),`
	`('Nina Richter', 10, 13),`
	`('Daniel Vogel', 11, 1),`
	`('Katharina Fuchs', 12, 1),`
	`('Philipp Stein', 13, 16),`
	`('Miriam Schröder', 14, 14),`
	`('Moritz Keller', 15, 3),`
	`('Johanna Kraus', 16, 17),`
	`('Felix Brandt', 17, 2);`

`INSERT INTO lizenzmodell (name, beschreibung, max_aktive_nutzer) VALUES`
	`('Named User', 'Feste Benutzerkonten, 1 Lizenz pro Person', NULL),`
	`('Concurrent User', 'Pool-Lizenz, begrenzt gleichzeitige Nutzung', 10),`
	`('Concurrent User', 'Pool-Lizenz, begrenzt gleichzeitige Nutzung', 25),`
	`('Campuslizenz', 'Unbegrenzte Nutzung innerhalb der Institution', NULL),`
	`('Modul Ausleihe', 'Lizenz für Ausleihmodul', NULL),`
	`('Modul Erwerbung', 'Lizenz für Erwerbungsmodul', NULL),`
	`('Modul Katalogisierung', 'Lizenz für Katalogisierungsmodul', NULL),`
	`('E-Book Paket A', 'Lizenz für 500 E-Books', NULL),`
	`('E-Book Paket B', 'Lizenz für 2000 E-Books', NULL),`
	`('Datenbank A', 'Fach-Datenbank Geisteswissenschaften', NULL),`
	`('Datenbank B', 'Fach-Datenbank Technik', NULL),`
	`('Reports-Addon', 'Berichts- und Statistikmodul', NULL),`
	`('Self-Service-Terminals', 'Lizenz für Selbstverbucher', 5),`
	`('API-Zugriff', 'Schnittstellenlizenz für Integrationen', NULL),`
	`('Testinstanz', 'Testsystem für Schulungen', 5),`
	`('Mobile App', 'Mobile Zugriffslizenz', NULL),`
	`('Premium Support', 'Zusätzliche Support-Lizenz', NULL),`
	`('Altsystem-Lizenz', 'Alte Bibliothekssoftware', 5),`
	`('Digitales Lesesaalmodul', 'On-Site Zugriff auf E-Ressourcen', NULL),`
	`('Fernzugriffmodul', 'Remote Access für Nutzer', NULL);`

`INSERT INTO lizenzvertrag (bibliothek_id, lizenzmodell_id, anbieter, startdatum, enddatum, anzahl_lizenzen, kosten_gesamt) VALUES`
	`(1, 1, 'BiblioSoft GmbH', '2025-01-01', '2025-12-31', 15, 7500.00),`
	`(1, 2, 'BiblioSoft GmbH', '2025-01-01', '2025-12-31', 5, 3000.00),`
	`(4, 3, 'BiblioSoft GmbH', '2025-01-01', '2025-12-31', 25, 9000.00),`
	`(4, 4, 'UniLib AG', '2024-01-01', '2026-12-31', 1, 20000.00),`
	`(5, 8, 'E-Reads AG', '2025-01-01', '2025-12-31', 1, 12000.00),`
	`(5, 9, 'E-Reads AG', '2025-01-01', '2025-12-31', 1, 18000.00),`
	`(6, 10, 'FachDB GmbH', '2024-07-01', '2025-06-30', 3, 9000.00),`
	`(6, 11, 'FachDB GmbH', '2024-07-01', '2025-06-30', 2, 6000.00),`
	`(2, 5, 'BiblioSoft GmbH', '2023-01-01', '2025-12-31', 3, 4000.00),`
	`(2, 6, 'BiblioSoft GmbH', '2023-01-01', '2025-12-31', 3, 4000.00),`
	`(3, 7, 'BiblioSoft GmbH', '2023-01-01', '2025-12-31', 2, 3500.00),`
	`(7, 12, 'BiblioSoft GmbH', '2025-01-01', '2025-12-31', 1, 2500.00),`
	`(8, 13, 'SelfService AG', '2025-01-01', '2025-12-31', 4, 8000.00),`
	`(9, 13, 'SelfService AG', '2025-01-01', '2025-12-31', 4, 8000.00),`
	`(10, 14, 'APIConnect GmbH', '2024-03-01', '2026-02-28', 1, 5000.00),`
	`(11, 15, 'BiblioSoft GmbH', '2025-01-01', '2025-12-31', 5, 1000.00),`
	`(12, 16, 'BiblioSoft GmbH', '2025-01-01', '2025-12-31', 1, 3000.00),`
	`(13, 17, 'BiblioSoft GmbH', '2025-01-01', '2025-12-31', 1, 6000.00),`
	`(14, 18, 'OldLib GmbH', '2022-01-01', '2025-12-31', 5, 5000.00),`
	`(15, 19, 'UniLib AG', '2024-01-01', '2027-12-31', 1, 15000.00);`

`INSERT INTO lizenznutzung (lizenzvertrag_id, nutzer_id, nutzungsdatum, dauer_minuten, aktion) VALUES`
	`-- Stadtbibliothek Mitte, Named User (relativ hohe Nutzung)`
	`(1, 1, '2025-01-10', 45, 'Login'),`
	`(1, 2, '2025-01-10', 30, 'Verwaltung'),`
	`(1, 1, '2025-01-11', 60, 'Ausleihe'),`
	`(1, 2, '2025-01-11', 20, 'Verwaltung'),`
	`(1, 1, '2025-01-12', 90, 'Katalogisierung'),`
	`-- Stadtbibliothek Mitte, Concurrent User (potenziell überdimensioniert: nur wenige Sitzungen)`
	`(2, 1, '2025-01-10', 15, 'Login'),`
	`(2, 2, '2025-01-11', 10, 'Login'),`
	 `-- Uni-Bibliothek Campus, Concurrent 25 (viel weniger Nutzer als Lizenzen)`
	`(3, 3, '2025-01-10', 120, 'Recherche'),`
	`(3, 4, '2025-01-10', 60, 'Recherche'),`
	`(3, 3, '2025-01-11', 90, 'Recherche'),`
	`-- Uni-Bibliothek Campus, Campuslizenz (intensiv genutzt, evtl. angemessen)`
	`(4, 3, '2025-01-10', 180, 'E-Ressource'),`
	`(4, 4, '2025-01-11', 200, 'E-Ressource'),`
	`-- FH-Bibliothek, E-Book Pakete (Paket B teuer, aber gering genutzt)`
	`(5, 7, '2025-01-10', 30, 'E-Book Zugriff'),`
	`(6, 7, '2025-01-10', 10, 'E-Book Zugriff'),`
	`-- Landesbibliothek, Fachdatenbanken (eine deutlich weniger genutzt)`
	`(7, 9, '2025-01-10', 20, 'Datenbank A'),`
	`(8, 9, '2025-01-10', 5,  'Datenbank B'),`
	`-- Stadtteilbibliotheken, Module mit kaum Nutzung`
	`(9, 5, '2025-01-10', 10, 'Ausleihe'),`
	`(10, 5, '2025-01-10', 0,  'Erwerbung'),`
	`-- Altsystem-Lizenz praktisch ungenutzt`
	`(19, 18, '2025-01-10', 5,  'Login Alt-System');`
	
# Aufgaben zur Datenanalyse
[[Einzelne Aufgabenblöcke#Aufgaben zur Datenanalyse]]
### 1. Grundlegende Bestandsaufnahme
Formuliere eine SQL-Abfrage, die alle Lizenzverträge mit Bibliotheksname, Lizenzmodell, Anzahl Lizenzen und Gesamtkosten ausgibt. Erweitere die Abfrage um eine sortierte Ausgabe nach höchsten Gesamtkosten zuerst, um teure Verträge schnell zu erkennen.
- [x] Gesamtkosten
- [x] Sortierung von teuer nach preiswert
- Was sind die teuersten Verträge?
- [ ] geht auch ohne join [[2025-11-07#SQL Übungen]]
2025-12-17
#### Teil 1
- [x] Welche Tabellen?
- lizenzvertrag
- bibliothek
- lizenzmodell
- Select from Lizenzverträge
	- bibliotheksname  -> von id zum Namen
		- Join
	- Lizenzmodell -> von id zu Namen
		- Join
	- Gesamtkosten
- [x] wie lautet der Befehl um den Namen aus der Verbundenen Tabelle zu lesen
-  join
- [x] Wie speichere ich den Query
	-  view
#### Ergebnisse
`127.0.0.1/projektbibliotheklizenzen/lizenzvertrag/		http://localhost/phpmyadmin/index.php?route=/table/sql&db=projektbibliotheklizenzen&table=lizenzvertrag`

   `Zeige Datensätze 0 - 19 (20 insgesamt, Die Abfrage dauerte 0,0005 Sekunden.)`

`SELECT lizenzvertrag.anbieter, lizenzmodell.name, bibliothek.name, lizenzvertrag.anzahl_lizenzen, lizenzvertrag.kosten_gesamt`  
`FROM ((lizenzvertrag` 
`inner join lizenzmodell`
`on lizenzvertrag.lizenzmodell_id=lizenzmodell.id)`
      `INNER JOIN bibliothek`
      `on lizenzvertrag.bibliothek_id=bibliothek.id);`

`anbieter	name	name	anzahl_lizenzen	kosten_gesamt`	
`BiblioSoft GmbH	Named User	Stadtbibliothek Mitte	15	7500.00`	
`BiblioSoft GmbH	Concurrent User	Stadtbibliothek Mitte	5	3000.00`	
`BiblioSoft GmbH	Concurrent User	Uni-Bibliothek Campus	25	9000.00`	
`UniLib AG	Campuslizenz	Uni-Bibliothek Campus	1	20000.00`	
`E-Reads AG	E-Book Paket A	Fachhochschulbibliothek	1	12000.00`	
`E-Reads AG	E-Book Paket B	Fachhochschulbibliothek	1	18000.00`	
`FachDB GmbH	Datenbank A	Landesbibliothek	3	9000.00`	
`FachDB GmbH	Datenbank B	Landesbibliothek	2	6000.00`	
`BiblioSoft GmbH	Modul Ausleihe	Stadtteilbibliothek Nord	3	4000.00`	
`BiblioSoft GmbH	Modul Erwerbung	Stadtteilbibliothek Nord	3	4000.00`	
`BiblioSoft GmbH	Modul Katalogisierung	Stadtteilbibliothek Süd	2	3500.00`	
`BiblioSoft GmbH	Reports-Addon	Schulbibliothek Gymnasium A	1	2500.00`	
`SelfService AG	Self-Service-Terminals	Schulbibliothek Gymnasium B	4	8000.00`	
`SelfService AG	Self-Service-Terminals	Schulbibliothek Gesamtschule	4	8000.00`	
`APIConnect GmbH	API-Zugriff	Kirchliche Bibliothek St. Paul	1	5000.00`	
`BiblioSoft GmbH	Testinstanz	Musikbibliothek Stadt	5	1000.00`	
`BiblioSoft GmbH	Mobile App	Kinder- und Jugendbibliothek	1	3000.00`	
`BiblioSoft GmbH	Premium Support	Digitale Bibliothek Region	1	6000.00`	
`OldLib GmbH	Altsystem-Lizenz	Archivbibliothek Stadtarchiv	5	5000.00`	
`UniLib AG	Digitales Lesesaalmodul	Technische Bibliothek Industriepark	1	15000.00`	

#### Teil 2
- [x] Sortierung nach Gesamtkosten
-  order by
- [x] LizenzID in die View einfügen
### 2. Kosten pro Lizenz
Erstelle eine Abfrage, die für jeden Lizenzvertrag die Kosten pro einzelner Lizenz berechnet (kosten_gesamt / anzahl_lizenzen). Lasse dir die Verträge ausgeben, bei denen die Kosten pro Lizenz besonders hoch sind (z.B. > 1.000), und sortiere absteigend nach diesem Wert.
- Vergleichbarkeit der Modelle
##### Teil 1
- [x] pro Vertrag einzelne Kosten pro Lizenz
	- Aufbauend auf LizenzVertragKostenSortiert
	- [x] Spalte mit Berechung einfügen
	- Wie geht das?
		- Mit `/` als Operator
		- `Round(BERechnung,2)`Rundet auf zwei Nchkommerstellen
##### Teil 2
- [x] Auswahl von teuren Verträgen
##### Teil 3
- [x] von hoch nach niedrig sortiern
### 3. Nutzung je Lizenzvertrag
Formuliere eine Abfrage, die für jeden Lizenzvertrag die Anzahl unterschiedlicher Nutzer in Lizenznutzung ermittelt. Erweitere die Abfrage um die Gesamtzahl der Nutzungsvorgänge und die Summe der Nutzung in Minuten pro Lizenzvertrag.
- [x] Anzahl der Nutzer
	- [x] Anzahl der  Nutzer
	- select from Lizenznutzung 
		- Lizenzvertrag-id group by
		- count(nutzer-Id) 
- [x] Gesamtzahl der Nutzungsvorgänge
- [x] Summe der Nutzung in Minuten pro Lizenzvertrag
	- *was ist das?*
- Wie werden die Lizenzen genutzt
### 4. Kosten pro aktivem Nutzer
Baue auf Aufgabe 2 und 3 auf: Erstelle eine Abfrage, die Kosten pro aktivem Nutzer berechnet (kosten_gesamt / Anzahl unterschiedlicher Nutzer). Lasse dir alle Lizenzverträge anzeigen, bei denen die Kosten pro aktivem Nutzer besonders hoch sind (z.B. > 2.000), um Kandidaten für Einsparungen zu finden.
- [ ] Kosten und Nutzung verbinden
- besonders Hohekosten identifizieren
### 5. Verträge mit geringer Nutzung
Formuliere eine Abfrage, die alle Lizenzverträge zeigt, bei denen es entweder gar keine Einträge in lizenznutzung gibt oder weniger als 3 unterschiedliche Nutzer. Nutze dazu eine LEFT JOIN-Verknüpfung zwischen lizenzvertrag und lizenznutzung und eine Gruppierung.
- [ ] ungenutzte Verträge
	- [ ] ´sql LEFT-JOIN und Gruppierung´
	- wird nicht mehr gebraucht.
	- baut auf 2. und 3. auf
### 6. Teure Pakete mit wenig Nutzung
Formuliere eine Abfrage, die E-Book- oder Datenbank-Lizenzverträge (z.B. anhand des lizenzmodell-Namens oder einer LIKE-Bedingung) mit der Summe der Nutzungsminuten pro Vertrag ausgibt. Erzeuge zusätzlich eine berechnete Spalte „Kosten_pro_Minute“ und sortiere nach den höchsten Kosten pro Minute Nutzung, um besonders unwirtschaftliche Pakete zu identifizieren.
- [ ] E-Book und DB Lizenzen
	- [ ] Kosten pro Minute
	- [ ] Sortierung von hoch zu niedrig
- Unwirtschaftliche Lizenzen
### 7. Nutzung nach Rollen
Erstelle eine Abfrage, die zeigt, welche benutzerrolle welche Lizenzverträge wie stark nutzt (z.B. Anzahl Nutzungen pro Rolle und Vertrag). Leite daraus ab, welche Rollen ggf. zu viel Zugriff auf teure Lizenzen haben (z.B. wenn „Verwaltung“ teure Forschungsdatenbanken kaum fachlich benötigt).
- [ ] Welche Nutzerrollen nutzen welche Liezenzen
- Rechtevergabe
- *Was sind die Rollen, welche gibt es?*
### 8. Auslaufende Verträge mit geringer Nutzung
Formuliere eine Abfrage, die alle Lizenzverträge zeigt, deren enddatum innerhalb der nächsten 6 Monate liegt. Erweitere die Abfrage so, dass zusätzlich die Anzahl Nutzungen oder Nutzungsminuten der letzten 3 Monate angezeigt wird, um zu entscheiden, ob der Vertrag verlängert, reduziert oder gekündigt werden sollte.
- [ ] Ende der Laufzeit 
- [ ] Nutzung der letzten 3 Monaten
- Verträge verlängern, kündigen, beibehalten
### 9. Zusammenfassung pro Bibliothek
Erstelle eine Abfrage, die pro Bibliothek die Summe der Lizenzkosten (kosten_gesamt) und die Summe der Nutzungsminuten ausgibt. Berechne daraus Kosten pro Nutzungsminute je Bibliothek und sortiere nach den höchsten Werten, um Bibliotheken mit besonderem Optimierungspotenzial zu identifizieren.
- [ ] Lizenzkosten pro Bibliothek
- [ ] Kosten pro Minute
- [ ] Sortierung von hoch zu niedrig
- Optimierung bei den Bibliotheken
	- Ähnlich der Rollen