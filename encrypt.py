from utils import *

image_path = input("Please enter path of the Image : \t")
cmy_folder_path = input("Please enter folder path in which CMY decomposed images to be stored : \t")
halftone_folder_path = input("Please enter folder path in which Halftone processed images to be stored : \t")
encrypted_images_folder_path = input("Please enter folder path in which Encrypted images to be stored : \t")

cmy_decomposition(image_path, cmy_folder_path)
halftone(cmy_folder_path, halftone_folder_path)
generate_encrypted_images(halftone_folder_path, encrypted_images_folder_path)

print("Please wait. It will take some time for processing...........")
print("Please check " + encrypted_images_folder_path + " folder for encrypted images")
