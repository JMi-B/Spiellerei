import cv2
import torch

# Model für die Datenanalyse aus GitHub repo laden
model = torch.hub.load("ultralytics/yolov5", "yolov5s") 

# Bild laden
bild = cv2.imread("c:/Users/juliane.bonenkamp/src/JMiArbeit/bilder/bild1.jpg")

# Colorpalett setzen
rgb = cv2.cvtColor(bild, cv2.COLOR_BGR2RGB)

# Model und Bild verbinden
results = model(rgb)

# Dataframe erstellen

df = results.pandas().xyxy[0]

# Dataframe veratbeiten

# gibt den df aus
# Index  xmin        ymin         xmax        ymax  confidence  class    name
# 0 1161.588501  768.233459  1238.861572  829.157471    Treffergenauigkeit       NRKlasse     NameKlasse
print(df)

# was gesucht wird und wie es heißt
cars = df[df["name"] == "car"]
trucks = df[df["name"] == "truck"]

# Car ein Rahmenamen 
for _, row in cars.iterrows():
    x = int(row["xmin"])
    y = int(row["ymin"])
    x2 = int(row["xmax"])
    y2 = int(row["ymax"])
    cv2.rectangle(bild, (x, y), (x2,y2), (0,255,0), 2)

for _, row in trucks.iterrows():
    x = int(row["xmin"])
    y = int(row["ymin"])
    x2 = int(row["xmax"])
    y2 = int(row["ymax"])
    cv2.rectangle(bild, (x, y), (x2,y2), (0,0,255), 2)

# Anzeige im eigenen Fenster

cv2.imshow("Fenster", bild)
cv2.waitKey(0)
cv2.destroyAllWindows()

