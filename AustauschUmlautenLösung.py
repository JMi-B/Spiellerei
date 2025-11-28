# Teil 1
# von Jmi

text = "Zügig wird der Faden durch das Nadelöhr der Nähmaschiene gefädelt."
neuerText = ""
print(text)
for buchstabe in text:
    if (buchstabe not in "äöü"):
        neuerText = neuerText + buchstabe
    else:
        if buchstabe == "ä":
            neuerText = neuerText +"ae"
        elif buchstabe == "ö":
            neuerText = neuerText + "oe"
        else:
            buchstabe == "ü"
            neuerText = neuerText + "ue"

print(neuerText)        

# Teil 2
# Lösung von Georg

textUmkehr = ""
index = 0
umlautgefunden = False
# Umkehr
for buchstabe in neuerText:
    if umlautgefunden:
        umlautgefunden = False
        continue
 
    print(neuerText[index] +" / "+ buchstabe)
 
    if (buchstabe not in "aou"):
        textUmkehr = textUmkehr + buchstabe
        index = index +1
       
    else:
        if buchstabe == "a":
            if neuerText[index +1] == "e":
                textUmkehr = textUmkehr + "ä"
                index = index +2
                umlautgefunden = True
            else:
                textUmkehr = textUmkehr + buchstabe
                index = index + 1
        elif buchstabe == "o":
            if neuerText[index +1] == "e":
                textUmkehr = textUmkehr + "ö"
                index = index +2
                umlautgefunden = True
            else:
                textUmkehr = textUmkehr + buchstabe
                index = index + 1
        elif buchstabe == "u":
            if neuerText[index +1] == "e":
                textUmkehr = textUmkehr + "ü"
                index = index +2
                umlautgefunden = True
            else:
                textUmkehr = textUmkehr + buchstabe
                index = index + 1
 
print(textUmkehr)