
import os
import numpy as np
import glob
import skimage.io as io
import matplotlib.pyplot as plt


def plot_sample(image,landmarks,axis):
	axis.imshow(image,cmap=plt.gray())
	if landmarks is not None:
		axis.scatter(landmarks[:,0],landmarks[:,1],marker = 'x')
	# for i in range(landmarks.shape[0]):
	# 	axis.text(landmarks[i,0],landmarks[i,1],str(i+1))

def crop_face_image(image,landmarks):
	centerx = landmarks[30,0]
	centery = landmarks[30,1]

	left_eye_x = np.mean(landmarks[36:41,0])
	left_eye_y = np.mean(landmarks[36:41,1])

	right_eye_x = np.mean(landmarks[42:47,0])
	right_eye_y = np.mean(landmarks[42:47,1])

	left_mounth_x = landmarks[48,0]
	left_mounth_y = landmarks[48,1]

	dis1 = np.sqrt(np.square(left_eye_x - right_eye_x)+np.square(left_eye_y - right_eye_y))
	dis2 = np.sqrt(np.square(left_eye_x - left_mounth_x)+np.square(left_eye_y - left_mounth_y))
	sz = 2*np.max([dis1,dis2])

	return image[centery-sz/2:centery+sz/2,centerx-sz/2:centerx+sz/2]

list_file = 'label.lst'
list_file2 = 'label_crop_face.lst'

landmark_directory = 'Landmarks/'
output_image_directory = 'crop_face/'
fi = open(list_file,'r')
fo = open(list_file2,'w')

lines = fi.readlines()


for l in lines:
	image_path = l.split(' ')[0]
	label = l.split(' ')[1].strip('\n')
	sub = image_path.split(os.sep)[1]
	seq = image_path.split(os.sep)[2]
	lamdmark_file_name = image_path.split(os.sep)[-1]
	lamdmark_file_name = lamdmark_file_name[0:lamdmark_file_name.find('.png')]+'_landmarks.txt'


	landmark_file = os.path.join(landmark_directory,sub,seq,lamdmark_file_name)
	landmarks = np.loadtxt(landmark_file)
	
	image = io.imread(image_path)
	image = crop_face_image(image,landmarks)

	image_file_name = image_path.split(os.sep)[-1]
	io.imsave(os.path.join(output_image_directory,image_file_name),image)
	fo.write(os.path.join(output_image_directory,image_file_name)+' '+label+'\n')
	# plot_sample(crop_face_image(image,landmarks),None,plt)
	
	# plt.show()
fo.close()