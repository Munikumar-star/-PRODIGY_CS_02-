from PIL import Image
import numpy as np

print("------------- Image Encryption Tool --------------")

def encrypt_image(image_path, key):
    # Opening the image
    original_image = Image.open(image_path)

    # Converting the image to a NumPy array
    image_array = np.array(original_image, dtype=np.uint8)

    # Ensure the key is in the range of 1-255
    key = key % 256  # Make sure key is within valid range

    # Adding the key to each pixel and clipping to stay within the range 0-255
    encrypted_image_array = np.clip(image_array + key, 0, 255)

    # Creating a new image from the encrypted NumPy array
    encrypted_image = Image.fromarray(np.uint8(encrypted_image_array))

    # Saving the encrypted image
    encrypted_image_path = "encrypted_image.png"
    encrypted_image.save(encrypted_image_path)
    print(f"Image encrypted successfully. Encrypted image saved at: {encrypted_image_path}")

def decrypt_image(encrypted_image_path, key):
    # Opening the encrypted image
    encrypted_image = Image.open(encrypted_image_path)

    # Converting the encrypted image to a NumPy array
    encrypted_image_array = np.array(encrypted_image, dtype=np.uint8)

    # Ensure the key is in the range of 1-255
    key = key % 256  # Make sure key is within valid range

    # Reversing the encryption by subtracting the key and clipping to stay within the range 0-255
    decrypted_image_array = np.clip(encrypted_image_array - key, 0, 255)

    # Creating a new image from the decrypted NumPy array
    decrypted_image = Image.fromarray(np.uint8(decrypted_image_array))

    # Saving the decrypted image
    decrypted_image_path = "decrypted_image.png"
    decrypted_image.save(decrypted_image_path)
    print(f"Image decrypted successfully. Decrypted image saved at: {decrypted_image_path}")

def main():
    while True:
        print("Select an option:")
        print("e - Encrypt image")
        print("d - Decrypt image")
        print("q - Quit")
        choice = input("Your choice: ")

        if choice == 'e':
            encrypt_choice()
        elif choice == 'd':
            decrypt_choice()
        elif choice == 'q':
            print("Exiting the program.")
            exit()
        else:
            print("Invalid choice. Please choose 'e' for encryption, 'd' for decryption, or 'q' to quit.")

def encrypt_choice():
    key = int(input("Enter encryption key: "))
    image_location = input("Enter the location or URL of the image: ")

    try:
        encrypt_image(image_location, key)
    except FileNotFoundError:
        print("Invalid location. Image not found. Please try again.")
        encrypt_choice()

def decrypt_choice():
    key = int(input("Enter decryption key: "))
    encrypted_image_location = input("Enter the location of the encrypted image: ")

    try:
        decrypt_image(encrypted_image_location, key)
    except FileNotFoundError:
        print("Invalid location. Encrypted image not found. Please try again.")
        decrypt_choice()

if __name__ == "__main__":
    main()
