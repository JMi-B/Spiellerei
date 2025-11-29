## Coding
- Libery `import cv2`
- Bild einlesen `cv2.imread(filename)` 
	- vielleicht vollständiger Pfad notwendig
- In Graustufen umwandeln `cv2.cvtColor(bild, cv2.COLOR_BGR2GRAY)`
![[JMIAuto01.py]]

| Bedeutung                                            | Befehl                                                                                                                                                                                        | Übersetzung                                                                                                                                                                  |
| ---------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Libery                                               | `import cv2`                                                                                                                                                                                  | Importiere Open Source Computer Vision Library                                                                                                                               |
| Bild einlesen                                        | `cv2.imread(filename)`                                                                                                                                                                        | image read                                                                                                                                                                   |
| In Graustufen umwandeln                              | `cv2.cvtColor(bild, cv2.COLOR_BGR2GRAY)`                                                                                                                                                      | convert color(bild, Farbe RGB zu Grau)                                                                                                                                       |
| Classifiere aufrufen um was auf dem Bild zu erkennen | cv2.CascadeClassifier(datei.xml)                                                                                                                                                              | Kaskadierende Klassifizierung                                                                                                                                                |
| Bild durchsuchen                                     | variableClassifier.detectMultiScale(VariableBildBearbeitet, rejectLevels,LevelWeigths)                                                                                                        | [Parameters of detectMultiScale in OpenCV using Python - Stack Overflow](https://stackoverflow.com/questions/36218385/parameters-of-detectmultiscale-in-opencv-using-python) |
| Rahmen zeihen                                        | `for coord in autos:<br>   `x = coord[0]`<br>   ` y = coord[1]`<br>   ` width = coord[2]`<br>   ` height = coord[3]`<br>    `cv2.rectangle(bild, (x,y), (x+width, y+height), (0, 255, 0), 2)` | Für die Koordinaten in Autos zeichen ein Rechteck mit den Koordinaten in RGB mit 2 PX breite                                                                                 |
| Bild in neuem Fenster anzeigen                       | `cv2.imshow("Fenster", bild)`                                                                                                                                                                 | bild zeignen                                                                                                                                                                 |
| Auf Taste warten                                     | `cv2.waitKey(0)`                                                                                                                                                                              | Warte auf Tastendruck                                                                                                                                                        |
| Fenster schleißen                                    | `cv2.destroyAllWindows()`                                                                                                                                                                     | Zerstöre alle Fenster                                                                                                                                                        |
# torch
Mashinlearning komplexer als OPENCV was die Analyse angeht. 
`for _, row in cars.iterrows():
   ` x = int(row["xmin"])
    `y = int(row["ymin"])
    `x2 = int(row["xmax"])
    `y2 = int(row["ymax"])
    `cv2.rectangle(bild, (x, y), (x2,y2), (0,255,0), 2)
   Funktion in #Pandas die einen Dataframe zeilenweise durchläuft und ein tupel mit einer Pandas Series mit dem Index und den Zeilendaten ausgibt.
   Den Index brauchen wir nicht er wird mit `_` verworfen, um keinen Arbeitsspeicher zu belegen
   und mit cv ractangels Boxen auf das Bild malt



![[JMIAuto02.py]]![[JMIBilder02.py]] Ausprobiert was auf verschieden Bildern erkannt wird