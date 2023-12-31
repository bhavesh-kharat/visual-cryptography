from PIL import Image

folder_path = input("Please enter folder path for encrypted images : \t")
infile1 = Image.open(folder_path + "/encrypt1.jpg")
infile2 = Image.open(folder_path + "/encrypt2.jpg")
infile3 = Image.open(folder_path + "/encrypt3.jpg")

outfile = Image.new('CMYK', infile1.size)

for x in range(0,infile1.size[0],2):
    for y in range(0,infile1.size[1],2):

        C = infile1.getpixel((x+1, y))[0]
        M = infile2.getpixel((x+1, y))[1]
        Y = infile3.getpixel((x+1, y))[2]


        outfile.putpixel((x, y), (C,M,Y,0))
        outfile.putpixel((x+1, y), (C,M,Y,0))
        outfile.putpixel((x, y+1), (C,M,Y,0))
        outfile.putpixel((x+1, y+1), (C,M,Y,0))

outfile.save("final.jpg")
print("Please open decrypted image : final.jpg")
