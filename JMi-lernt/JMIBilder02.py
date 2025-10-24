import cv2
import torch

# Model für die Datenanalyse aus GitHub repo laden
model = torch.hub.load("ultralytics/yolov5", "yolov5s") 

# Bild laden
# wald
# bild = cv2.imread("C:/Users/juliane.bonenkamp/src/JMiArbeit/bilder/csm_WaldposterA3_send_311a3e20c7.jpg")
# zoo
# bild = cv2.imread("C:/Users/juliane.bonenkamp/src/JMiArbeit/bilder/best-zoo-in-the-world-1200x700.jpg")
# schule
# bild = cv2.imread("C:/Users/juliane.bonenkamp/src/JMiArbeit/bilder/Schuleundbildung1200x.jpg")
# stadt
bild = cv2.imread("C:/Users/juliane.bonenkamp/src/JMiArbeit/bilder/thueringen-erfurt-domplatz.webp")

# Colorpalett setzen
rgb = cv2.cvtColor(bild, cv2.COLOR_BGR2RGB)

# Model und Bild verbinden
results = model(rgb)

# Dataframe erstellen

df = results.pandas().xyxy[0]

# Dataframe veratbeiten

# gibt den df aus

print(df)

# # was gesucht wird und wie es heißt
# horse = df[df["name"] == "horse"]
# bird = df[df["name"] == "bird"]

# # Car ein Rahmenamen 
# for _, row in horse.iterrows(): # fuchs
#     x = int(row["xmin"])
#     y = int(row["ymin"])
#     x2 = int(row["xmax"])
#     y2 = int(row["ymax"])
#     cv2.rectangle(bild, (x, y), (x2,y2), (0,255,0), 2)

# for _, row in bird.iterrows(): # waschbär
#     x = int(row["xmin"])
#     y = int(row["ymin"])
#     x2 = int(row["xmax"])
#     y2 = int(row["ymax"])
#     cv2.rectangle(bild, (x, y), (x2,y2), (0,0,255), 2)

# # was gesucht wird und wie es heißt
person = df[df["name"] == "person"]
car = df[df["name"] == "car"]
# chair = df[df["name"] == "chair"]

# Car ein Rahmenamen 
for _, row in person.iterrows(): # fuchs
    x = int(row["xmin"])
    y = int(row["ymin"])
    x2 = int(row["xmax"])
    y2 = int(row["ymax"])
    cv2.rectangle(bild, (x, y), (x2,y2), (0,255,0), 2)
person = df[df["name"] == "person"]
# chair = df[df["name"] == "chair"]

# Car ein Rahmenamen 
for _, row in car.iterrows(): # fuchs
    x = int(row["xmin"])
    y = int(row["ymin"])
    x2 = int(row["xmax"])
    y2 = int(row["ymax"])
    cv2.rectangle(bild, (x, y), (x2,y2), (0,255,255), 2)


# for _, row in chair.iterrows(): # waschbär
#     x = int(row["xmin"])
#     y = int(row["ymin"])
#     x2 = int(row["xmax"])
#     y2 = int(row["ymax"])
#     cv2.rectangle(bild, (x, y), (x2,y2), (0,0,255), 2)

# Anzeige im eigenen Fenster

cv2.imshow("Fenster", bild)
cv2.waitKey(0)
cv2.destroyAllWindows()

