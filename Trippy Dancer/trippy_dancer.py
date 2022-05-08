from simpleimage import SimpleImage

DANCER = "dancer.jpg"
BACK_IMAGE = "Tie-dye.png"
INTENSITY_THRESHOLD = 1.8


def main():
    """
    This program is a takes an image of a dancer and
    applies a background image around the dancer.
    """
    dancer = SimpleImage(DANCER)
    back = SimpleImage(BACK_IMAGE)
    dancer_trimmed = trim_crop_image(dancer, 16, 0)
    back = trim_crop_image(back, 150, 150)

    # Asks for user input for where the image screening should occur
    option = int(input("Write 1 for foreground & 2 for background: "))

    for pixel in dancer_trimmed:
        # Option 1 will change the red pixels to the other image pixels
        if option == 1:
            average = (pixel.red + pixel.green + pixel.blue) // 3
            # See if this pixel is "sufficiently" red
            if pixel.red >= average * INTENSITY_THRESHOLD:
                dancer_trimmed = image_screening(dancer_trimmed, back, pixel)
        # Option 2 will change the white-ish pixels to the other image pixels
        elif option == 2:
            if pixel.red >= 200 and pixel.blue >= 200 and pixel.green >= 200:
                dancer_trimmed = image_screening(dancer_trimmed, back, pixel)
        else:
            if option != 1 or option != 2:
                option = int(input("Write 1 for foreground & 2 for background: "))
    dancer_trimmed.show()

def image_screening(orig_img, texture_img, pixel):
    # Sets the pixels from one image to the desired location on the other image
    x = pixel.x
    y = pixel.y
    orig_img.set_pixel(x, y, texture_img.get_pixel(x, y))
    return orig_img

def trim_crop_image(original_img, trim_width, trim_height):
    # Crops the image pixels to desired width and height
    new_width = original_img.width - trim_width
    new_height = original_img.height - trim_height
    new_img = SimpleImage.blank(new_width, new_height)

    for x in range(new_width):
        for y in range(new_height):
            old_x = x + trim_width
            old_y = y + trim_height
            orig_pixel = original_img.get_pixel(old_x, old_y)
            new_img.set_pixel(x, y, orig_pixel)
    return new_img

if __name__ == "__main__":
    main()