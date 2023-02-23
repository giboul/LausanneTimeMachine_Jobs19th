import pytesseract
from PIL import Image
from os import listdir
from os.path import join


pytesseract.pytesseract.tesseract_cmd = (
    r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    # https://github.com/UB-Mannheim/tesseract/wiki
)
images = listdir(join('Almanach', 'images'))
nimages = len(images)
ndigits = len(str(nimages))

txt = ''
for i, path in enumerate(images):
    # Separate pages (optional)
    txt += f"\n{f' page {i+1} ':#^50}\n\n"
    # Read images
    txt += pytesseract.image_to_string(
        Image.open(join('Almanach', 'images', path)),
        lang='fra'  # https://github.com/tesseract-ocr/tessdata
    )
    # Update progress bar
    print(f"\r{i+1:>{ndigits}}/{nimages} pages treated"
          f" |{'█'*round((i+1)/nimages*20):<20}| "
          f"({(i+1)/nimages:.0%})", end="")

# Write text to a file
with open(join('Almanach', 'Almanach.txt'), 'w', encoding='UTF-16') as file:
    file.write(txt)
