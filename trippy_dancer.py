from simpleimage import SimpleImage

DANCER = 'dancer.jpg'
BACK_IMAGE = 'Tie-dye.png'
INTENSITY_THRESHOLD = 1.8

def main():
    dancer = SimpleImage(DANCER)
    back = SimpleImage(BACK_IMAGE)
    # back.show()
    # dancer.show()
    dancer_trimmed = trim_crop_image(dancer, 16, 0)
    back = trim_crop_image(back, 150, 150)

    for pixel in dancer_trimmed:
        average = (pixel.red + pixel.green + pixel.blue) // 3
        # See if this pixel is "sufficiently" red
        # if pixel.red >= average * INTENSITY_THRESHOLD:
        if pixel.red >= 200 and pixel.blue >= 200 and pixel.green >= 200:
            # If so, we get the corresponding pixel from the
            # back image and overwrite the pixel in
            # the main image with that from the back image.
            x = pixel.x
            y = pixel.y
            dancer_trimmed.set_pixel(x, y, back.get_pixel(x, y))
    dancer_trimmed.show()


def trim_crop_image(original_img, trim_width, trim_height):
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

if __name__ == '__main__':
    main()