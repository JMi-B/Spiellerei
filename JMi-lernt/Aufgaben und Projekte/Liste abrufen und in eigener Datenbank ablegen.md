[[2025-09-29]]
# Quelle
- [https://open-data.dortmund.de/explore/dataset/bader-besucher-seit-1960/information/?disjunctive.jah…](https://open-data.dortmund.de/explore/dataset/bader-besucher-seit-1960/information/?disjunctive.jahr&sort=jahr "https://open-data.dortmund.de/explore/dataset/bader-besucher-seit-1960/information/?disjunctive.jahr&sort=jahr")
## Vorlagen
![[MitKurzZeit.py]] 
Erstellt diese Json
![[historische_daten02.json]]
[]()![[parken_sql.py]]
Api direkt in SQL schreiben

## Schritte
- py url abrufen
- mit DB verbinden
	- DB muss existieren
	- py kann Tabelle erstellen
		-  Namen aus Vorgabe
		- variablen definieren - mit Werten aus der Json
		- for schleife zum schreiben.
