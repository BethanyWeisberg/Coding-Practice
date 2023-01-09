# Create thumbnails of images selected

from PIL import Image

original_dancer = "dancer.jpg"
tie_dye = "Tie-dye.png"
trippy_dancer_1 = "trippy_dancer_1.png"
trippy_dancer_2 = "trippy_dancer_2.png"

images = (original_dancer, tie_dye, trippy_dancer_1, trippy_dancer_2)

for image in images:
    open_image = Image.open(image)
    MAX_SIZE = (300, 300)
    open_image.thumbnail(MAX_SIZE)
  
# creating thumbnail
    open_image.save(f'thumbnail_{image}')
    open_image.show()