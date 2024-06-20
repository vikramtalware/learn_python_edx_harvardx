import sys
from PIL import Image, ImageOps
import os.path

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        try:
            extensions = [".jpg",".jpeg",".png"]
            input = os.path.splitext(sys.argv[1].lower())[1]
            output = os.path.splitext(sys.argv[2].lower())[1]
            if input != output:
                sys.exit("Input and output have different extensions")
            else:
                 overlay(sys.argv[1], sys.argv[2])
        except(IndexError):
            sys.exit("Invalid Input")

def overlay(input, output):
    try:
        overlay_shirt = Image.open("shirt.png")
        size = overlay_shirt.size
        with Image.open(input) as photo:
            cropped_photo = ImageOps.fit(photo, size)
            cropped_photo.paste(overlay_shirt, overlay_shirt)
            cropped_photo.save(output)
    except(FileNotFoundError):
        sys.exit("File not found")

if __name__ == "__main__":
    main()
