import os
from PIL import Image
import xml.etree.ElementTree as ET
from xml.dom.minidom import parseString
from lxml.etree import Element, SubElement, tostring


dirs ="D:\\dataset\\person_reid\\Annotated\\person_4"
files = os.listdir(dirs)
dirs1="D:\\dataset\\person_reid\\Annotated\\Cropped" #saving directory
# os.makedirs(dirs+"\\"+"croped_image")
m = 0
for f in files:
	dirs2 = os.path.join(dirs,f)
	img_path = dirs2+'\\images'
	xml_path = dirs2+'\\labels'
	images = os.listdir(img_path)
	for file in images:
		img_id = file.split('.')
		tree = ET.parse(os.path.join(xml_path,img_id[0]+'.xml'))
		root = tree.getroot()
		file_name = root.find('object')
		node_root = Element('annotation')
		node_filename = SubElement(node_root, 'filename')
		for type_tag in root.findall('object'):
			name = type_tag.find('name').text
			xmin = int(type_tag.find('bndbox/xmin').text)
			ymin = int(type_tag.find('bndbox/ymin').text)
			xmax = int(type_tag.find('bndbox/xmax').text)
			ymax = int(type_tag.find('bndbox/ymax').text)
			# ymax=ymax+300
			if name == 'person':
				print(xmin,' ',ymin,' ',xmax,' ',ymax)
				new_folder = os.path.join(dirs1,f)
				if not os.path.exists(new_folder):
					try:
						os.makedirs(new_folder,mode=0o777)
					except:
						print('directory already exists')
				ff=new_folder+'\\'+str(img_id[0])+'.jpg'
				m += 1
				try:
					img = Image.open(os.path.join(img_path,img_id[0]+'.jpg'))
					crop_img = img.crop((xmin,ymin,xmax,ymax))
					crop_img.save(ff)
				except Exception as e:
					print (e)
