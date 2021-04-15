import numpy as np
import os
import json


def writeAnns(ann_path,save_path):

	with open(ann_path) as f:
  		data = json.load(f)

	for annot in data:
		print(annot["filename"])
		with open(os.path.join(save_path,annot["filename"].split(".")[0]+".txt"),'w') as ann_file:
			for cordinates in annot["regions"]:
				
				region = cordinates["region_attributes"]
				coords = cordinates["shape_attributes"]
				print(region)
				if coords["name"]=="polygon":
					x_pts= coords["all_points_x"]
					y_pts= coords["all_points_y"]
					
					pts=list(zip(x_pts, y_pts))

					for pt in pts:
						ann_file.write(str(pt[0])+","+str(pt[1])+",")


				if coords["name"]=="rect":
					x,y,w,h= coords["x"],coords["y"],coords["width"],coords["height"]
					
					pts = [(x,y),(x+w,y),(x,y+h),(x+w,y+h)]
					
					for pt in pts:
						ann_file.write(str(pt[0])+","+str(pt[1])+",")
				
				if "value" in region.keys():
					ann_file.write(str(region["value"]))	
				else:
					ann_file.write("####")	
				ann_file.write("\n")
				

if __name__=='__main__':

	
	Train_ann_path="train_annotations.json"
	Train_save_path= "./train/"
	Test_ann_path="test_annotations.json"
	Test_save_path= "./test/"

	Val_ann_path="val_annotations.json"
	Val_save_path= "./val/"

	writeAnns(Train_ann_path,Train_save_path)
	writeAnns(Val_ann_path,Val_save_path)
	writeAnns(Test_ann_path,Test_save_path)
