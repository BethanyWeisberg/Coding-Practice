from PIL import Image

DANCER = "dancer.jpg"
BACK_IMAGE = "Tie-dye.png"
INTENSITY_THRESHOLD = 2.5


def main():
    """
    This program takes an image of a dancer and either
    drops a psychedelic image behind the dancer or replaces any
    sufficiently red pixels with the pixels of the psychedelic image.
    """
    dancer = Image.open(DANCER)
    back = Image.open(BACK_IMAGE)
    dancer_trimmed = trim_crop_image(dancer, 16, 0)
    back_trimmed = trim_crop_image(back, 150, 150)
    dancer_color = detect_color_coordinates(dancer_trimmed)


    # Asks for user input for where the image screening should occur
    option = int(input("Write 1 for foreground & 2 for background: "))

    for pixel in dancer_color:
        x,y,red,green,blue = pixel[0],pixel[1],pixel[2],pixel[3],pixel[4]

        # Option 1 will change the red pixels to the other image pixels
        if option == 1:
            average = (red + green + blue) // 3
            # See if this pixel is "sufficiently" red
            if red >= average * INTENSITY_THRESHOLD:
                dancer_color = image_screening(dancer_trimmed, back_trimmed, pixel)
        # Option 2 will change the white-ish pixels to the other image pixels
        elif option == 2:
            if red >= 200 and green >= 200 and blue >= 200:
                dancer_color = image_screening(dancer_trimmed, back_trimmed, pixel)
        else:
            if option != 1 or option != 2:
                option = int(input("Write 1 for foreground & 2 for background: "))
    # trippy_dancer = dancer_color.save("trippy_dancer.png")
    dancer_color.save(f"trippy_dancer_{option}.png","PNG")
    dancer_color.show()

def image_screening(orig_img, texture_img, pixel):
    # Sets the pixels from one image to the desired location on the other image
    x = pixel[0]
    y = pixel[1]
    orig_img.putpixel((x, y), texture_img.getpixel((x, y)))
    return orig_img

def trim_crop_image(original_img, trim_width, trim_height):
    # Crops the image pixels to desired width and height
    new_width = original_img.width - trim_width
    new_height = original_img.height - trim_height
    new_img = Image.new(mode="RGB",size=(new_width, new_height))

    for x in range(new_width):
        for y in range(new_height):
            old_x = x + trim_width
            old_y = y + trim_height
            orig_pixel = original_img.getpixel((old_x,old_y))
            new_img.putpixel((x, y), orig_pixel)
    return new_img

# Retuns pixel xy coordinates and RGB values
def detect_color_coordinates(filename):
    img = filename.getdata()
    width, height = img.size
    coord_color_tpl = []
    for x in range(width):
        for y in range(height):
            r,g,b = img.getpixel((x,y))
            coord_color_tpl.append((x, y, r, g, b))
    return(coord_color_tpl)


if __name__ == "__main__":
    main()
