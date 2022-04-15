from fileinput import filename
import threading
import numpy as np
import json


dict2npy_dict={}
trainlist=[]
classes=80+92 #set num_classes
txt=open('./coco/thing_stuff_train.txt','w')

# get data in the instances_train2017.json
with open("./coco/annotations/instances_train2017.json") as ins:
    coco_ins_17json=json.load(ins)
    for i in range(len(coco_ins_17json.get('annotations'))):
        OneHotmatrix=np.zeros(classes).astype(np.float32)
        filename=str(coco_ins_17json.get('annotations')[i].get('image_id')).rjust(12,'0')
        for k in range(len(coco_ins_17json.get('categories'))):
            if coco_ins_17json.get('annotations')[i].get('category_id') == coco_ins_17json.get('categories')[k].get('id'):
                OneHotmatrix[k]=1
                print(coco_ins_17json.get('annotations')[i].get('image_id'),coco_ins_17json.get('categories')[k].get('id'))
                if filename in trainlist:
                    dict2npy_dict[filename]= OneHotmatrix + dict2npy_dict[filename]
                else:
                    dict2npy_dict[filename]= OneHotmatrix
                    trainlist.append(filename)
                dict2npy_dict[filename][dict2npy_dict[filename]>1]=1
                break
            #print(coco_ins_17json.get('images')[i].get('file_name'))

# get data in the stuff_train2017.json        
with open("./coco/annotations/stuff_train2017.json") as pan:
    coco_pan_17json=json.load(pan)
    for i in range(len(coco_pan_17json.get('annotations'))):
        OneHotmatrix=np.zeros(classes).astype(np.float32)
        filename=str(coco_pan_17json.get('annotations')[i].get('image_id')).rjust(12,'0')
        for k in range(len(coco_pan_17json.get('categories'))):
            if coco_pan_17json.get('annotations')[i].get('category_id') == coco_pan_17json.get('categories')[k].get('id'):
                OneHotmatrix[k+80]=1
                print(coco_pan_17json.get('annotations')[i].get('image_id'),coco_pan_17json.get('categories')[k].get('id'))
                if filename in trainlist:
                    dict2npy_dict[filename]= OneHotmatrix + dict2npy_dict[filename]
                else:
                    dict2npy_dict[filename]= OneHotmatrix
                    trainlist.append(filename)
                dict2npy_dict[filename][dict2npy_dict[filename]>1]=1
                break

    np.save('./coco/thing_stuff_cls_labels_17.npy',dict2npy_dict)
    str='\n'
    txt.write(str.join(trainlist))
    txt.close()
