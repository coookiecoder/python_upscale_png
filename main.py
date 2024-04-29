from PIL import Image

# python image upscale

if __name__ == '__main__':
    image_name = input("image name : ")
    buffer = Image.open(image_name + ".png")
    output = Image.new('RGB', (buffer.size[0] * 2, buffer.size[1] * 2), (255, 255, 255))

    for y in range(0, buffer.size[0]):
        for x in range(0, buffer.size[1]):
            output.putpixel((x * 2, y * 2), buffer.getpixel((x, y)))
            output.putpixel((x * 2, y * 2 + 1), buffer.getpixel((x, y)))
            output.putpixel((x * 2 + 1, y * 2), buffer.getpixel((x, y)))
            output.putpixel((x * 2 + 1, y * 2 + 1), buffer.getpixel((x, y)))

    output.save(image_name + "_upscale.png", "PNG")
    buffer.close()
    output.close()
