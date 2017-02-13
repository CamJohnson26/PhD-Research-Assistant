from fpdf import FPDF
from os import listdir
from os.path import isfile, join, basename
from PIL import Image
import os

def createPDFS(mypath):
	print("Processing folder " + mypath)
	folders = [join(mypath, f) for f in listdir(mypath) if not isfile(join(mypath, f))]
	imagelist = [join(mypath, f) for f in listdir(mypath) if isfile(join(mypath, f)) and "JPG" in f]

	pdf = FPDF()
	# imagelist is the list with all image filenames
	print(str(len(imagelist)) + " jpgs found")
	for image in imagelist:
		im = Image.open(image)
		w, h = im.size
		if w > h:
			img2 = im.rotate(90, expand=True)
			img2.save(image)
		pdf.add_page()
		pdf.image(image,0,0,200)
	if len(imagelist) > 0:
		newfile = join(mypath,basename(mypath) + ".pdf")
		pdf.output(newfile, "F")
		mycmd = "ocrmypdf \"" + newfile + "\" \"" + newfile[:-4] + "-ocr.pdf\""
		print(mycmd)
		os.system(mycmd)
	for f in folders:
		createPDFS(f)

mypath = "/Users/rahardhikautama/Desktop/Test JPG to PDF/"
createPDFS(mypath)
