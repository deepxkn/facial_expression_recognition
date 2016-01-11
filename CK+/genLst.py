
import os
import numpy as np
import glob

emotion_directory='Emotion/'
label_file = 'label.lst'
image_directory = 'cohn-kanade-images/'

fo = open(label_file,'w')


def find_image_files(sub,seq):
	file_num = len(glob.glob(os.path.join(image_directory,sub,seq,'*.png')))
	idx = [1,file_num-2,file_num-1,file_num]
	file_lst = []
	for i,v in enumerate(idx):
		file_lst.append(os.path.join(image_directory,sub,seq)+os.sep+sub+'_'+seq+'_'+'%08d'% v+'.png')
	return file_lst


for root,_,files in os.walk(emotion_directory):
	if len(files)<1 or not files[0].endswith('txt'):
		continue
	sub = files[0].split('_')[0]
	seq = files[0].split('_')[1]
	label = np.loadtxt(os.path.join(root,files[0]))
	file_lst = find_image_files(sub,seq)
	fo.write(file_lst[0]+' 0\n')
	fo.write(file_lst[1]+' '+str(int(label))+'\n')
	fo.write(file_lst[2]+' '+str(int(label))+'\n')
	fo.write(file_lst[3]+' '+str(int(label))+'\n')

fo.close()