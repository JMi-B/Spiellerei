# einzelne Module aus pillow importieren um Arbeitsspeicher zu schonen

from PIL import Image
from PIL.ExifTags import TAGS
# Dateisystem lesen 
import os

# example images from https://www.dpreview.com/reviews/image-comparison/fullscreen?attr18=daylight&attr13_0=panasonic_dmcgh4&attr13_1=google_pixel_2&attr13_2=nikon_z6ii&attr13_3=oly_em5ii&attr15_0=jpeg&attr15_1=jpeg&attr15_2=jpeg&attr15_3=jpeg&attr16_0=100&attr16_1=50&attr16_2=100&attr16_3=200&attr126_0=1&attr126_3=1&normalization=full&widget=1&x=0&y=0

# Funtion um exif Tags aus zu lesen 
def getImageAndPrintExif(path):
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
