from os import mkdir
from os.path import join, isdir
from pdf2image import convert_from_path


# Poppler package: https://github.com/oschwartz10612/poppler-windows/releases/
POPPLER_PATH = r'C:\Program Files\poppler-23.01.0\Library\bin'
# Load pdf as pngs
print("Converting pdf to pngs...", end=' ')
images = convert_from_path(
    join('Almanach', 'Almanach.pdf'),
    poppler_path=POPPLER_PATH
)
print("Converted.")

nimages = len(images)
ndigits = len(str(nimages))

# Save each image
for i, image in enumerate(images):
    image.save(
        join('Almanach', 'images', f'page{i+1:0>{ndigits}}.png'),
        'PNG',
        dpi=(500, 500)
    )
    # Update progress bar
    print(f"\r{i+1:<{ndigits}}/{nimages} images saved"
          f" |{'█'*round((i+1)/nimages*20):<20}| "
          f"({(i+1)/nimages:.0%})", end="")
