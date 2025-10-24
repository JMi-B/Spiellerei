# OpenCV Libary importiern

import cv2

# Bild lesen
bild = cv2.imread("c:/Users/juliane.bonenkamp/src/JMiArbeit/bilder/bild1.jpg")

# Bild in Graustufen umwandeln
graustufen = cv2.cvtColor(bild, cv2.COLOR_BGR2GRAY)

# Classifer auf rufen um Autos zu erennen
car_cascade = cv2.CascadeClassifier("c:/Users/juliane.bonenkamp/src/JMiArbeit/bilder/cars.xml")

# Bild nach Autos durch suchen

autos = car_cascade.detectMultiScale(graustufen, 1.1, 5)
# autos = car_cascade.detectMultiScale(graustufen, 1.1, 2)
# autos = car_cascade.detectMultiScale(graustufen, 1.1, 8)

# Rahmen um das Auto ziehen

for coord in autos:
    x = coord[0]
    y = coord[1]
    width = coord[2]
    height = coord[3]
    cv2.rectangle(bild, (x,y), (x+width, y+height), (0, 255, 0), 2)


# Bild zeigen

cv2.imshow("hgsdh", bild)
# cv2.imshow("hgsdh", graustufen)
cv2.waitKey(0)
cv2.destroyAllWindows()
