#Schleife
- In Python gibt es nur Kopfgesteuerte Schleifen mit For oder While
- Die Fuss gesteuerte Do - While - Schleife gibt es nicht.
	- In der Do - While - Schleife wird der Code mindestens einmal ausgeführt
	- Dann wird die Bedingung überprüft.
	- Die Kopfgesteuerten For und While Schleifen prüfen die Bedingung zu erste
- Am Besten schreibe ich mir die Schleife als einen Satz auf 
`for zeichen in text:`
   `zeichen = zeichen.lower()`
   - jedes Zeichen aus Text in Kleinbuchstaben umwandeln
   - um Zeichen in Kleinbuchstaben umzuwandeln
   - ist Zeichen gleich Zeichen.MethodeKleinbuchstaben
	   - d.h. Jedes Element in der Variable Zeichen wird in einen Kleibuchstaben umgewandelt und als Kleinbuchstabe wieder in die Variable geschreiben

![[loops.py]] von Georg
[[Schleifen#Liste auslesen|Liste auslesen]]
[[Schleifen#Directory auslesen|Directory auslesen]]
[[Schleifen#Loop über String|Loop über String]]
[[Schleifen#Range|Range]]
[[Schleifen#Range mit condinue|Range mit condinue]]
[[Schleifen#Range mit break|Range mit break]]
[[#While-Schleife]]
[[#Kleiner als 5]]
[[#kleiner Gleich 5]]
[[#Endlosschleife]]
### Liste auslesen
`print("Loops")`
`print("=====")`
`print()`
`print("For loop with list:")`
`list = ["Bla", "Blub", "Nudelsuppe"]`
`for entry in list:`
    `print(entry)`
### Directory auslesen
`print("For loop with dict:")`
  `dict = {`
    `"Bla": 5,`
    `"Blub": 8,`
    `"Nudelsuppe": 10`
`}`
`for key in dict:`
    `value = dict[key]`
    `print(key +": "+ str(value))`
### Loop über String
`text = "Nudelsuppe"`
`for letter in text:`
    `print(letter)`
### Range
- Eine Schleife hat eine bestimmte Anzahl von Durchläufen
`for i in range(1, 10):`
    `print("Loop "+ str(i))`
#### Range mit condinue
- bei einer bestimmten Bedingung wird ein Eintrag übersprungen
`for i in range(1, 10):`
    `if i == 5:`
#### Range mit break
- Abbruch wenn Bedingung erfüllt
`for i in range(1, 10):`
    `if i == 5:`
        `break`
    `print("Loop "+ str(i))`
        `continue`
    `print("Loop "+ str(i))`
### While-Schleife
- Bedingung wird am Anfang gesetzt, die Schleife läuft bis diese erfüllt ist 
- **Vorsicht: Wenn die Bedingung unerfüllbar ist entsteht eine Dauerschleife**
- Alle boolschen Operatoren möglich
#### Kleiner als 5
`print("While loop with lower")`
`i = 1`
`while (i < 5):`
    `print(i)`
    `i += 1`
`input("press enter for next")`
`print()`
#### kleiner Gleich 5
`print("While loop with lower equals")`
`i = 1`
`while (i <= 5):`
    `print(i)`
    `i += 1`
`input("press enter for next")`
`print()`
#### Endlosschleife
`print("While loop infinite")`
`i = 1`
`while (True):`
    `print(i)`
    `i += 1`