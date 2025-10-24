#Exif sind die MetaDaten von Bildern, wie Auflösung, Kamara und Aufnahme Datum. Das was sich in den Eigenschaften eines Bild verbirgt.

Sie können mit Python ausgelesen werden.![[exif.py| exif von Georg]]
# Libery
#pillow ![[https://github.com/python-pillow/Pillow/]]
darin gibt es Module #PIL (Python ImageLibery)
Nur einzelne Module Importieren 
#os Modul um auf das DateiSystem zuzugreifen
## Funktion
#funktion #python 
Eine Funktion ist ein Kodeblock, der nur ausgeführt wird, wenn er aufgerufen wird. Das kann ganz einfach sein, wie `print()`.
Daten werden als Parameter an eine Funktion übergeben
Eine Funktion kann mit `return` Daten als Ergebnis zurück liefern.
Eine Funktion kann selbst definiert werden.

| Bedeutung               | Befehl                                           | Übersetzung                                                                                                                           |
| ----------------------- | ------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------- |
| Definiert eine Funktion | def name_funktion(argument):<br> print(argument) | erstelle eine Funktion mit dem Namen name_funktion. Mit dem Argument argument<br>print() steht für den code der ausgefürt werden soll |
| Aufruf meiner Funktion  | name_funktion()                                  | Rufe meine Funktion name_funktion auf . Der vorher definierte code  wird ausgeführt                                                   |
### Konkretes Beispiel
![[JMiexif.py]]

| was                                                                 | ist was                      | wofür                                                                       |
| ------------------------------------------------------------------- | ---------------------------- | --------------------------------------------------------------------------- |
| def ==getImageAndPrintExif==(pathtoimage):                          | Name der Funktion            | Definiert die Funktion mit dem Namen getImageAndPrintExif                   |
| (pathtoimage)                                                       | Argument der Funktion        | Der Pfad für die Datein                                                     |
| img = Image.open(pathtoimage)                                       | öffnet Bild                  | ließt Bild in dei Variable img                                              |
| exif = img.getexif()                                                | ließt exif                   | ließt die Exifdaten von dem Bild in img                                     |
| for tag_id in exif:<br><br>        tag = TAGS.get(tag_id, tag_id)   | Schleife                     | holt die ids der Tags                                                       |
| get                                                                 |                              | Holt den Key im dict                                                        |
| TAGS                                                                |                              | Directionary mit den Tags und ihren ID                                      |
| if (tag == "Make" or tag == "Model"):                               | IF-Abfrage                   | Wählt nur Make(Hersteller ) und Model Kamaramodel aus                       |
| data = exif.get(tag_id)                                             |                              | schreibt inhalt der Tag Id in die variable Data                             |
| print(f"{tag:25}{str(data)}")                                       | Ausgabe                      | formatiert die Ausgabe so das für den Tag immer 25 Zeichen ausgegben werden |
| path = "../exifAuslesen/Camera"                                     | Definition der Variable path | Hier sind die Bilder                                                        |
| files = os.listdir(path)                                            | Variabel files               | Liste der Bilder aus dem Pfad                                               |
| file                                                                |                              | Einzelnes Bild                                                              |
| for file in files:<br><br>    getImageAndPrintExif(path +"/"+ file) | For Schleife                 | Ruft die Funktion auf mit den Argumenten Pfad und Bild                      |



def ==getImageAndPrintExif==(path):
    print("load image from "+ path)
    img = Image.open(path)
    exif = img.getexif()
    for tag_id in exif:
        tag = TAGS.get(tag_id, tag_id)
        if (tag == "Make" or tag == "Model"):
            data = exif.get(tag_id)
            print(f"{tag:25}{str(data)}")
    TODO: createNewCamera(make, model)
path = "C:/Users/juliane.bonenkamp/src/JMiArbeit/exifAuslesen/Camera"
files = os.listdir(path)
print(files)
for file in files:

    getImageAndPrintExif(path +"/"+ file)


