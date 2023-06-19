from PIL import Image
import os

def validate_directory(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)
        

def cmy_decomposition(img_path, cmy_folder_path):
    image = Image.open(img_path)
    color_image = image.convert('CMYK')
    bw_image = image.convert('1')

    outfile1 = Image.new("CMYK", [dimension for dimension in image.size])
    outfile2 = Image.new("CMYK", [dimension for dimension in image.size])
    outfile3 = Image.new("CMYK", [dimension for dimension in image.size])

    for x in range(0, image.size[0], 1):
        for y in range(0, image.size[1], 1):
            sourcepixel = image.getpixel((x, y))

            outfile1.putpixel((x, y),(sourcepixel[0],0,0,0))

            outfile2.putpixel((x, y),(0,sourcepixel[1],0,0))

            outfile3.putpixel((x, y),(0,0,sourcepixel[2],0))

    validate_directory(cmy_folder_path)
      
    outfile1.save(cmy_folder_path + '/cmy1.jpg')
    outfile2.save(cmy_folder_path + '/cmy2.jpg')
    outfile3.save(cmy_folder_path + '/cmy3.jpg')
    
    
def halftone(cmy_folder_path, halftone_folder_path):
    
    image1 = Image.open(cmy_folder_path + "/cmy1.jpg")
    image2 = Image.open(cmy_folder_path + "/cmy2.jpg")
    image3 = Image.open(cmy_folder_path + "/cmy3.jpg")
    
    image1 = image1.convert('1')
    image2 = image2.convert('1')
    image3 = image3.convert('1')

    hf1 = Image.new("CMYK", [dimension for dimension in image1.size])
    hf2 = Image.new("CMYK", [dimension for dimension in image1.size])
    hf3 = Image.new("CMYK", [dimension for dimension in image1.size])

    for x in range(0, image1.size[0]):
        for y in range(0, image1.size[1]):
            pixel_color1 = image1.getpixel((x, y))
            pixel_color2 = image2.getpixel((x, y))
            pixel_color3 = image3.getpixel((x, y))
            if pixel_color1 == 255:
                hf1.putpixel((x, y),(255,0,0,0))
            else:
                hf1.putpixel((x, y),(0,0,0,0))

            if pixel_color2 == 255:
                hf2.putpixel((x, y),(0,255,0,0))
            else:
                hf2.putpixel((x, y),(0,0,0,0))

            if pixel_color3 == 255:
                hf3.putpixel((x, y),(0,0,255,0))
            else:
                hf3.putpixel((x, y),(0,0,0,0))

    validate_directory(halftone_folder_path)
    
    hf1.save(halftone_folder_path + '/hf1.jpg')
    hf2.save(halftone_folder_path + '/hf2.jpg')
    hf3.save(halftone_folder_path + '/hf3.jpg')
    
    
def generate_encrypted_images(halftone_folder_path, encrypted_images_folder_path):
    
    image1 = Image.open(halftone_folder_path + "/hf1.jpg")
    image1 = image1.convert('CMYK')

    image2 = Image.open(halftone_folder_path + "/hf2.jpg")
    image2 = image2.convert('CMYK')

    image3 = Image.open(halftone_folder_path + "/hf3.jpg")
    image3 = image3.convert('CMYK')

    share1 = Image.new("CMYK", [dimension * 2 for dimension in image1.size])

    share2 = Image.new("CMYK", [dimension * 2 for dimension in image2.size])

    share3 = Image.new("CMYK", [dimension * 2 for dimension in image3.size])

    for x in range(0, image1.size[0]):
        for y in range(0, image1.size[1]):
            pixelcolor = image1.getpixel((x, y))

            if pixelcolor[0]+pixelcolor[1]+pixelcolor[2] == 0:
                share1.putpixel((x * 2, y * 2), (255,0,0,0))
                share1.putpixel((x * 2 + 1, y * 2), (0,0,0,0))
                share1.putpixel((x * 2, y * 2 + 1), (0,0,0,0))
                share1.putpixel((x * 2 + 1, y * 2 + 1), (255,0,0,0))

            else:
                share1.putpixel((x * 2, y * 2), (0,0,0,0))
                share1.putpixel((x * 2 + 1, y * 2), (255,0,0,0))
                share1.putpixel((x * 2, y * 2 + 1), (255,0,0,0))
                share1.putpixel((x * 2 + 1, y * 2 + 1), (0,0,0,0))

            pixelcolor = image2.getpixel((x, y))

            if pixelcolor[0]+pixelcolor[1]+pixelcolor[2] == 0:
                share2.putpixel((x * 2, y * 2), (0,255,0,0))
                share2.putpixel((x * 2 + 1, y * 2), (0,0,0,0))
                share2.putpixel((x * 2, y * 2 + 1), (0,0,0,0))
                share2.putpixel((x * 2 + 1, y * 2 + 1), (0,255,0,0))

            else:
                share2.putpixel((x * 2, y * 2), (0,0,0,0))
                share2.putpixel((x * 2 + 1, y * 2), (0,255,0,0))
                share2.putpixel((x * 2, y * 2 + 1), (0,255,0,0))
                share2.putpixel((x * 2 + 1, y * 2 + 1), (0,0,0,0))

            pixelcolor = image3.getpixel((x, y))

            if pixelcolor[0]+pixelcolor[1]+pixelcolor[2] == 0:
                share3.putpixel((x * 2, y * 2), (0,0,255,0))
                share3.putpixel((x * 2 + 1, y * 2), (0,0,0,0))
                share3.putpixel((x * 2, y * 2 + 1), (0,0,0,0))
                share3.putpixel((x * 2 + 1, y * 2 + 1), (0,0,255,0))

            else:
                share3.putpixel((x * 2, y * 2), (0,0,0,0))
                share3.putpixel((x * 2 + 1, y * 2), (0,0,255,0))
                share3.putpixel((x * 2, y * 2 + 1), (0,0,255,0))
                share3.putpixel((x * 2 + 1, y * 2 + 1), (0,0,0,0))

    validate_directory(encrypted_images_folder_path)

    share1.save(encrypted_images_folder_path + '/encrypt1.jpg')
    share2.save(encrypted_images_folder_path + '/encrypt2.jpg')
    share3.save(encrypted_images_folder_path + '/encrypt3.jpg')
    