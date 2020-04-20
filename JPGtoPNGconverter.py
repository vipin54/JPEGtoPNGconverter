from PIL import Image
import os
import sys

imagefolder=sys.argv[1]
outputfolder=sys.argv[2]

if not os.path.exists(outputfolder):
	os.makedirs(outputfolder)

for filename in os.listdir(imagefolder):
	img=Image.open(f'{imagefolder}{filename}')

	clean_name=os.path.splitext(filename)[0]
	img.save(f'{outputfolder}{clean_name}.png','png')
	print("All done")
