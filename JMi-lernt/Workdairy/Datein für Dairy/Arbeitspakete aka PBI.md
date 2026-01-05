PBI : Product Backlog Item
Titel: Implementierung Galgenmännchen

Beschreibung:

Galgenmänchen ist ein Spiel, bei dem ein Benutzer ein zufälliges Wort erraten muss. Das Wort wird aus beim Start des Programms einer Liste von bekannten Wörtern ausgewählt. Der Benutzer bekommt das Wort nicht angezeigt, sondern eine Reihe von Platzhaltern, die der Länge des Wortes entsprechen.

Der Benutzer kann einzelne Buchstaben eingeben und mit Enter bestätigen. Nach jeder Eingabe wird geprüft, ob der Buchstabe im Wort enthalten ist oder nicht. Ist der Buchstabe nicht enthalten, wird ein Fehlerzähler hochgezählt. Erreicht der Benutzer die maximale Anzahl an Fehlversuchen (Vorgabe ist 6), ist der Ratevorgang gescheitert, es wird eine entsprechende Meldung ausgegeben und das Programm wird beendet.

Gibt der Benutzer einen richtigen Buchstaben ein, wird der Platzhalter an der entsprechenden Stelle im Wort nicht mehr angezeigt, stattdessen wird der Buchstabe angezeigt.

Beispiel:

Wort ist "Wunderbar".  
Platzhalteransicht ist "_________".

Wenn der Benutzer den Buchstaben "e" eingibt und mit Enter bestätigt, dann wird die folgende Zeichenkette angezeigt:

"____e____"

Hat der Benutzer alle Buchstaben richtig erraten, ohne die maximale Anzahl an Fehler erreicht zu haben, so wird eine Erfolgsmeldung ausgegeben.

Akzeptanzkriterien:

- Der Benutzer kann Buchstaben eingeben und mit Enter bestätigen.  
- Bei richtigen Buchstaben werden die Platzhalter an der entsprechenden Stelle ersetzt. Das funktioniert auch, wenn ein Buchstabe mehrfach im Wort vorkommt.  
- Bei falschen Buchstaben werden die Fehlversuche gezählt. Die maximale Anzahl von 6 Fehlversuchen kann nicht überschritten werden.  
- Bei der maximalen Anzahl von Fehlversuchen wird das Programm mit einer Fehlermeldung beendet.  
- Wenn alle Buchstaben richtig geraten wurden, wird das Programm mit einer Erfolgsmeldung beendet.  
- Beim Start des Programms wird ein zufälliges Wort aus einer Liste ausgewählt.  
- Das Programm funktioniert mit Worten unterschiedlicher Länge.  
- Das Programm behandelt Fehleingaben ausserhalb von einzelnen Buchstaben korrekt. D.h. wenn Zahlen, Sonderzeichen oder mehrere Buchstaben eingegeben werden, stürzt das Programm nicht ab.

Abschätzungen:

L1 -> L2 -> L3

Level 1: Sehr grob (S - M - L) => Feature zeitlich einplanen  
Level 2: Feiner (Manntage) => Aufbereitung für Feature Teams  
Level 3: Sehr fein => Aufbereitung durch komplettes Team

Ziel: 3 Manntage Aufwand pro PBI