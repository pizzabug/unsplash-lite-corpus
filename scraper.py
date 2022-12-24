import csv
import urllib.request
from PIL import Image

# Open the CSV file in append mode
with open('metdb/manifest.csv', 'a', newline='', encoding="utf-8") as manifest:
    with open('metdb/photos.csv', 'r', encoding="utf-8") as photos:
        # Open the CSV file and read the image path from it
        reader = csv.reader(photos)

        # Create a CSV writer object
        writer = csv.writer(manifest)

        # Reader iterator
        photositerator = 0;
        for row in reader:
            # Skip the header row
            if photositerator == 0:
                photositerator += 1
                continue

            image_name = row[0]
            image_path = row[2]
            image_caption= row[8]
            image_savePath = 'metdb/img/' + image_name + '.png'
            image_relPath = 'img/' + image_name + '.png'

            # Open the image from the URL and resize it
            with urllib.request.urlopen(image_path) as url:
                image = Image.open(url)
                # Calculate the width and height of the image
                width, height = image.size

                # Pick the shortest dimension from width and height
                if width < height:
                    idealWidth = width
                else:
                    idealWidth = height

                # Calculate the top-left and bottom-right coordinates of the cropping region
                left = (width - idealWidth) // 2
                top = (height - idealWidth) // 2
                right = left + idealWidth
                bottom = top + idealWidth

                # Crop the image to the desired size
                image = image.crop((left, top, right, bottom))
                image = image.resize((512, 512),resample=Image.Dither.NONE)

            # Save the resized image as a PNG
            image.save(image_savePath, format='PNG')

            print("Saved " + image_relPath + " to disk")
            
            # Write a new row to the file
            writer.writerow([image_relPath, image_caption])
