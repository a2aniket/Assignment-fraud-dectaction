from pdf import pdf_to_text
from imagetotext import get_text
from main import cosine_sim
from os import listdir
from os.path import isfile, join
from  flask import Flask,render_template,request
from werkzeug.utils import secure_filename
from  assignment import pdf_to_text1

app=Flask(__name__)

@app.route("/")
def hone():
	return render_template("home.html")

@app.route("/copycase",methods=["GET","POST"])
def copycase():
	paper_check()
	number1,number2,score=calulate_marks()
	return render_template("copycase.html",number1=number1,number2=number2,score=score,length=len(number1))


@app.route("/assmentupload",methods=["GET","POST"])
def assmentupload():
	return render_template("assmentupload.html")

@app.route("/assignment_check",methods=["GET","POST"])
def assignment_check():
	file = request.files['orignal']
	filename = secure_filename(file.filename)
	if file.filename != '':
		file.save("upload/{}".format("orignal.pdf"))
	file = request.files['check']
	filename = secure_filename(file.filename)
	if file.filename != '':
		file.save("upload/{}".format("check.pdf"))
	orignal=pdf_to_text1("orignal.pdf")
	check=pdf_to_text1("check.pdf")
	score=cosine_sim(orignal,check)*100
	return render_template("result.html",score=score)


def paper_check():
	pappers = [f for f in listdir("./pappers/") if isfile(join("./pappers/", f))]
	for file in pappers:
		files,file_name=pdf_to_text(file)
		if files:
			text=get_text(files,file_name)

		file_txt=open("./text_converted/"+file+".txt","w+")
		file_txt.write(text)




def calulate_marks():
	number = [f for f in listdir("./text_converted/") if isfile(join("./text_converted/", f))]
	number1=[]
	number2=[]
	score=[]
	processed=[(0,0)]
	for num in number:
		file1 = open("./text_converted/"+num,"r+")
		main=file1.read()
		for num1 in number:
			if num!=num1:
				if (num1,num) not in processed:
					processed.append((num,num1))
					file2 = open("./text_converted/"+num1,"r+")
					compare=file2.read()
					print(num[0:-8]+" vs "+num1[0:-8]+" Score "+str(cosine_sim(main,compare)))
					number1.append(num[0:-8])
					number2.append(num1[0:-8])
					score.append(cosine_sim(main,compare)*100)
	return number1,number2,score


if __name__ == '__main__':
    app.run(debug=True)