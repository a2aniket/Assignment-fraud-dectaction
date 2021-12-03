from pdf2image import convert_from_path
from pdf2jpg import pdf2jpg
from os import listdir
from os.path import isfile, join
def pdf_to_text(file_name):
    file=file_name
    result = pdf2jpg.convert_pdf2jpg("./pappers/"+file_name,"./temp/", pages="ALL")
    print("text to image complete...............")
    files = [f for f in listdir("./temp/"+file+""+"_dir/") if isfile(join("./temp/"+file+""+"_dir/", f))]
    print(files)
    file_name=file+""+"_dir/"
    print("path compltete...............")
    return files,file_name