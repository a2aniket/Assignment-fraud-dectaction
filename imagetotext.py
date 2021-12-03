import pytesseract as tess
from PIL import Image
tess.pytesseract.tesseract_cmd =r'C:\Program Files\Tesseract-OCR\tesseract.exe'
merge_text=""
def get_text(files,file_name):
	merge_text=""
	for i in files:
		img=Image.open("./temp/"+file_name+""+i)
		print("./temp/"+file_name+"/"+i)
		text= tess.image_to_string(img)
		
		merge_text=merge_text+text
		print("image to text complete..................")

	return merge_text