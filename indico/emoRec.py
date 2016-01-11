

import indicoio
import sys
import os

indicoio.config.api_key = 'adc14e7af6f166a04b95dd8aabf93a53'



source_image_directory = '../CK+'
source_image_lst = '../CK+/label_crop_face.lst'
result_file = 'ck+_indicoio.lst'

expression_list = ['Angry','Sad','Neutral','Surprise','Fear','Happy']
fo = open(result_file,'a')
fi = open(source_image_lst,'r')
lines = fi.readlines()

for l in lines:

	arr = l.split()
	file_path = os.path.join(source_image_directory,arr[0])
	print 'doing '+file_path+' '+str(l)+' of '+str(len(lines))
	result = indicoio.fer(file_path)
	fo.write(file_path+'\n')
	for e in expression_list:
		fo.write(e+':'+str(result[e])+' ')
	fo.write('\n')

fo.close()

