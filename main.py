import faces
import sys
import kivy
from PIL import Image

filename = input("Enter filename including extension:\n>")
face = open(filename, 'rb')

print(faces.KNOWN_FILTERS)
fil = input("Now enter the full name of the filter you want from the above list.\n>")

crop = True
c = input("Crop? [y/n]\n>")
if c == 'y':
    crop = True
elif c == 'n':
    crop = False
else:
    crop = True

try:
    image = faces.FaceAppImage(file=face)
except faces.ImageHasNoFaces:
    print('Your face is not recognized. Are you an alien?')
except faces.BadImageType:
    print('This image is not valid. Get some good bytes.')
except faces.BaseFacesException:
    print('Something Bad Happened.')

try:
    result = image.apply_filter(fil, cropped=crop)
except faces.BadFilterID:
    print('Bad Filter ID')

img = open('output.jpg', 'wb')
img.write(result)
img.close()
