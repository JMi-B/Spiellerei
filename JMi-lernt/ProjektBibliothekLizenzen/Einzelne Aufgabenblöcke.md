
Worum geht es. 
# Grundlagen recherche
[[Recherche der Grundlagen]]
- [ ] Prozesse verstehen und einordnen
### Grundlagen des Lizenzmanagements und typische Prozesse (Beschaffung, Inventarisierung, Nutzung, Rückgabe, Audit).
### Spezielle Anforderungen an Lizenzverwaltung in Bibliotheken (elektronische Resourcen, Campus- und Konsortiallizenzen)
### Rechtliche Rahmenbedingungen (Urheberrecht, Nutzungsrechte, Open-Access-Modelle)
### Kennzahlen und Nutzungsanalysen für Lizenzoptimierung (z.B. Kosten pro Nutzung, Auslastung, Low-Use-Titel)
### Rolle moderner Bibliotheksmanagementsysteme (BMS/ILS) bei der Automatisierung von Lizenzverwaltungsprozessen.
# IST-Analyse des Datenbestands
## Datengrundlage
- [ ] Datenbank erstellen [[Datengrundlage]]
- [ ] Abfragen für die Präsentation
	- [ ] 4 aus 9
## Aufgaben zur Datenanalyse
[[Datengrundlage#Aufgaben zur Datenanalyse]]
### 1. Grundlegende Bestandsaufnahme
Formuliere eine SQL-Abfrage, die alle Lizenzverträge mit Bibliotheksname, Lizenzmodell, Anzahl Lizenzen und Gesamtkosten ausgibt. Erweitere die Abfrage um eine sortierte Ausgabe nach höchsten Gesamtkosten zuerst, um teure Verträge schnell zu erkennen.
- [ ] Gesamtkosten
- [ ] Sortierung von teuer nach preiswert
- Was sind die teuersten Verträge
### 2. Kosten pro Lizenz
Erstelle eine Abfrage, die für jeden Lizenzvertrag die Kosten pro einzelner Lizenz berechnet (kosten_gesamt / anzahl_lizenzen). Lasse dir die Verträge ausgeben, bei denen die Kosten pro Lizenz besonders hoch sind (z.B. > 1.000), und sortiere absteigend nach diesem Wert.
- [ ] pro Vertrag einzelne Kosten pro Lizenz
- [ ] von hoch nach niedrig sortiern
- Vergleichbarkeit der Modelle
### 3. Nutzung je Lizenzvertrag
Formuliere eine Abfrage, die für jeden Lizenzvertrag die Anzahl unterschiedlicher Nutzer in Lizenznutzung ermittelt. Erweitere die Abfrage um die Gesamtzahl der Nutzungsvorgänge und die Summe der Nutzung in Minuten pro Lizenzvertrag.
- [ ] Anzahl der Nutzer
- [ ] Gesamtzahl der Nutzungsvorgänge
- [ ] Summe der Nutzung in Minuten pro Lizenzvertrag
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
# Verbesserungsmöglichkeiten finden und vorschlagen
Das ist das Ziel- Folien

# [[Präsentation]]

pro Minute eine Folie Plus Titel, Begrüßung und Verabschiedung
Ich lese Folien nicht vor.
Sie enthalten die wichtigsten Stichworte und Zusammenhänge.
 15 min Zeit
## Teile
1. Ausgangssituation und Zielsetzung (2-3 Minuten): Kurzbeschreibung der Bibliothek, des Lizenzproblems und des Projektziels.
2. Vorgehen und Datenmodell (4-5 Minuten): Prozessaufnahme, Datenbankschema, Beispielabfragen, verwendete Tools.
3. Ergebnisse und Optimierungsvorschläge (4-5 Minuten): Zentrale Kennzahlen, identifizierte Über-/Unterlizenzierung, Verbesserungsvorschläge für Prozesse und Systemunterstützung.
4. Fazit und Ausblick (2-3 Minuten): Nutzen für die Bibliothek und mögliche Erweiterung (z.B. automatische Reports, Dashboards).

| Folien | Nur | Thema                                 |     |
| ------ | --- | ------------------------------------- | --- |
| 0.1    | 1   | Titel                                 |     |
| 0.2    | 2   | Begrüßung                             |     |
| 1-3    | 3   | Ausgangsituatuin und Zielsetzung      |     |
|        | 4   |                                       |     |
|        | 5   |                                       |     |
| 4-5    | 6   | Vorgehen und Datenmodelle             |     |
|        | 7   |                                       |     |
|        | 8   |                                       |     |
|        | 9   |                                       |     |
|        | 10  |                                       |     |
| 4-5    | 11  | Ergebnisse und Optimierungsvorschläge |     |
|        | 12  |                                       |     |
|        | 13  |                                       |     |
|        | 14  |                                       |     |
|        | 15  |                                       |     |
| 2-3    | 16  | Fazit und Ausblick                    |     |
|        | 17  |                                       |     |
|        | 18  |                                       |     |
| 0.3    | 19  | Nochfragen                            |     |
| 0.4    | 20  | Dank und Verabschiedung               |     |

## Form
- Literaturnachweis
## Optik
- Tamplats auf confluence mit FirmenLAyout
- Grafische Aufarbeitung der Daten.
	- Tool?
	- Reicht PP-Bordmittel?
		- 
