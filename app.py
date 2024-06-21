import os
from PIL import Image

def convert_images_to_webp(source_folder):
    destination_folder = os.path.join(source_folder, 'webp_images')
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    valid_extensions = ['.jpg', '.jpeg', '.png', '.bmp']

    for filename in os.listdir(source_folder):
        file_path = os.path.join(source_folder, filename)
        file_extension = os.path.splitext(filename)[1].lower()

        if file_extension in valid_extensions:
            image = Image.open(file_path)
            webp_filename = os.path.splitext(filename)[0] + '.webp'
            webp_filepath = os.path.join(destination_folder, webp_filename)
            image.save(webp_filepath, 'webp')
            print(f"Converted {filename} to {webp_filename}")

if __name__ == "__main__":
    source_folder = input("Δώσε τη διαδρομή του φακέλου με τις εικόνες: ")
    convert_images_to_webp(source_folder)
