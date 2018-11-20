import img2pdf 
from PIL import Image 
import os
import sys
import shutil




def convert():
	for fileName in os.listdir("input"):
		if not fileName.endswith(".png"):
			continue
		print("Converting: ", fileName)	
		pdf_path = "output/" + fileName[:-4]
		pdf_path += ".pdf"
		image = Image.open("input/" + fileName)
		pdf_bytes = img2pdf.convert(image.filename)

		outputFile = open(pdf_path, "wb")
		outputFile.write(pdf_bytes)

		image.close()
		outputFile.close()



def clear_out():
	try:
		print("Clearing output...")
		shutil.rmtree('output/')
		os.mkdir('output')
	except:
		print("Nothing to clear")


def clear_in():
	try:
		print("Clearing input...")
		shutil.rmtree('input')
		os.mkdir('input')
	except:
		print("Nothing to clear")

def clear():
	clear_in()
	clear_out()




def main():
	choice = {
	"clear_out": clear_out,
	"clear_in" : clear_in,
	"clear" : clear,
	"convert": convert
	}


	if len(sys.argv) is 2:
		method = choice.get(sys.argv[1])
		if method:
			method()


if __name__ == "__main__":
	main()