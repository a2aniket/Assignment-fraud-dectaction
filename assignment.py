from pdf2image import convert_from_path
from pdf2jpg import pdf2jpg
from os import listdir
from os.path import isfile, join
import pytesseract as tess
from PIL import Image
tess.pytesseract.tesseract_cmd =r'C:\Program Files\Tesseract-OCR\tesseract.exe'
merge_text=""

def pdf_to_text1(file):
    result = pdf2jpg.convert_pdf2jpg("./upload/"+file,"./upload/temp", pages="ALL")
    print("text to image complete...............")
    files = [f for f in listdir("./upload/temp/"+file+""+"_dir/") if isfile(join("./upload/temp/"+file+""+"_dir/", f))]
    print(files)
    file_name=file+""+"_dir/"
    print("path compltete...............")
    merge_text=""
    for i in files:
    	img=Image.open("./upload/temp/"+file_name+""+i)
    	print("./upload/temp/"+file_name+"/"+i)
    	text= tess.image_to_string(img)
    	merge_text=merge_text+text
    	print("image to text complete..................")

    return merge_text

	#return merge_text