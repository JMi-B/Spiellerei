# Fragen
## Was ist Regression?

## Was sind Aggregationen?
- Zusammenfassen von Daten für [[Metadaten]]
- [Was ist: Aggregation - STATISTIK EINFACH LERNEN](https://de.statisticseasily.com/Glossar/Was-ist-Aggregation%3F/)
- mehrere Datenpunkte zu einem Wert zusammen fassen 
	- Komplexität vereinfachen
	- Interpretation erleichtern
### Welche gibt es?
- Summe
- Durchschnitt (Mittelwert)
- Median
- Modus
- Anzahl
- Standartabweichung
#### Aggregatfunktionen in SQL
SUM() AVG() COUNT() MIN() MAX()
mit GROUP BY
#### in der Visualisierung
Durch Aggregation die Daten leichter darstellbar
- Trends und Verteilung
#### Schwierigkeiten
- Informationsverlust
- Methode beeinflusst das Ergebnis
## Median und Mittelwert

zentrale Tendenzmaße
[Maße der zentralen Tendenz: Mittelwert, Modus, Median](https://de.statisticseasily.com/Ma%C3%9Fe-der-zentralen-Tendenz%2C-Mittelwert%2C-Modus%2C-Median/)
Welche Werte stellen einen Datensatz am besten dar
+ Mittelwert (Durchschnitt) (Mean)
	+ Summe aller Werte geteilt durch Anzahl der Werte
	+ Anfällig für Ausreißer
+ Modus (Mode)
	+ häufiges Vorkommender WErt
	+ "Der Modus ist der Wert, der in einem Datensatz am häufigsten vorkommt. Im Gegensatz zu Mittelwert und Median ist der Modus nicht unbedingt eindeutig, was zu Datensätzen führt, die unimodal (ein Modus), bimodal (zwei Modi) oder multimodal (mehr als zwei Modi) sein können. Zur Berechnung des Modus gehört die Ermittlung der Häufigkeit jedes Werts im Datensatz und die Bestimmung, welche Werte am häufigsten vorkommen."
	+ bei gleichmäßiger verteilung oder ähnlicher Häufigkeit schwach
+ Median (Median)
	+ in Geordnetem Datensatz der Wert in der Mitte
		+ bei ungrader Anzahl der Durchschnitt der beiden Werte in der der Mitte
		+ (n+1)/2 
	+ nicht von Extremwerten beeinflusst

## Aufgaben
- [ ] Trends abbilden
- [[Diagramme erstellen mit Supperset]]
-  Abweichung vom Mittelwert
	-  Wie bilden?
	- Wie Darstellen
		- Welche Aussage will ich
	
