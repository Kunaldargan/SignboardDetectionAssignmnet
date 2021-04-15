import numpy as np
import cv2
import json
import os

def writeAnns(ann_path,save_path, name):
	with open(ann_path) as f:
  		data = json.load(f)
	
	file = open(name+".txt",'w')
	for id, annot in enumerate(data):
		print(annot["filename"])
		img=cv2.imread(os.path.join(name,annot["filename"]))
		h,w = img.shape[:2]
		file.write(str(id)+" "+os.path.join(name,annot["filename"])+" "+str(h)+" "+str(w))
		
		for cordinates in annot["regions"]:	
			coords = cordinates["shape_attributes"]

			if coords["name"]=="rect":
				x,y,w,h= int(coords["x"]),int(coords["y"]),int(coords["width"]),int(coords["height"])
				
				file.write(" 0"+" "+str(x)+" "+str(y)+" "+str(x+w)+" "+str(y+h))
					
		file.write("\n")
				

if __name__=='__main__':

	
	Train_ann_path="train_annotations.json"
	Train_save_path= "./train/"
	Test_ann_path="test_annotations.json"
	Test_save_path= "./test/"

	Val_ann_path="val_annotations.json"
	Val_save_path= "./val/"

	writeAnns(Train_ann_path,Train_save_path,"train")
	writeAnns(Val_ann_path,Val_save_path,"val")
	writeAnns(Test_ann_path,Test_save_path,"test")
