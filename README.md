# visual-cryptography

Visual cryptography is a cryptographic technique that allows for the secure sharing of secret information without the need for complex computations or cryptographic algorithms. It is primarily focused on the visual perception of images and employs the principles of steganography and encryption.

In this implementation, we have developed a visual cryptography encryption framework that offers enhanced security for color images. The framework takes a color image as input and employs the CMY color space to decompose it into three separate monochromatic images: Cyan, Magenta, and Yellow. These individual monochromatic images serve as the basis for the visual encryption process. Using halftone techniques, we generate shares for each monochromatic image, ensuring that no share reveals any discernible information about the original color image. The halftone patterns applied to the shares introduce visual noise and distortions, making it nearly impossible for unauthorized users to obtain any meaningful insight into the secret image. Through comprehensive computer simulations, we have confirmed that the resulting halftoned shares maintain a satisfactory level of visual quality, preserving the privacy and integrity of the encrypted information. This implementation provides a robust and visually secure solution for protecting color images using visual cryptography techniques based on CMY color decomposition and halftoning.

### Steps to run this application:
- Clone this repo:
```python
git clone https://github.com/bhavesh-kharat/visual-cryptography
```
- Install Pillow library:
```python
pip install pillow
```
- Run encrypt.py for get encrypted images.
- Run decrypt.py for get decryption of encrypted images.
