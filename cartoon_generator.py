import cv2
from PIL import Image
import os
import json

class CartoonGenerator:
	"""
		Generates cartoons given a swatch fabric and a config file containing body types, skin types and stencils
		for each combination of skin type and body type

		Methods
		-------
		generate_cartoons(path) : generates cartoons for an image at path
		get_cartoons(path) : returns list of paths of generated cartoons
		convert_to_pil(img) : coverts cv2 image array to pil array
		resize(img) : resizes the image to the dimensions of stencil
	"""
	def __init__(self,fabric, out_dir, config):
		"""
			Parameters
			----------
			fabric : str
				path of the swatch fabric
			out_dir : str/None
				path of the output directory in which all generated cartoons will be stored
			config : str
				path of the config json file  which contains body types, skin types, paths to stencils

		"""
		self.fabric = fabric
		if out_dir:
			self.out_dir = out_dir
		else:
			self.out_dir = './output'
		self.cartoons = []
		json_file = open(config).read()
		json_config = json.loads(json_file)
		self.stencils = json_config["stencils"]
		self.body_types = json_config["body_types"]
		self.skin_types = json_config["skin_types"]
		filename, ext = os.path.splitext(fabric.split('\\')[-1])
		path = os.path.join(self.out_dir,filename)
		if not os.path.exists(path):
			os.makedirs(path)
		for body_type in self.body_types:
			body_path = os.path.join(path, body_type)
			if not os.path.exists(body_path):
				os.makedirs(body_path)
		self.generate_cartoons(path)
		
	def generate_cartoons(self, path):
		"""
		Parameters
		----------
		path : path of the fabric for which stencils need to be created
		"""
		img = cv2.imread(self.fabric)
		for body_type in self.body_types:
			body_path = os.path.join(path, body_type)
			resized_img = CartoonGenerator.resize(img)
			for skin_type in self.skin_types:
				stencil = Image.open(self.stencils[body_type][skin_type])
				cartoon = Image.new('RGB', stencil.size)
				cartoon.paste(resized_img, (88, 102))
				cartoon.paste(stencil, (0,0), mask=stencil)
				cartoon.save(body_path+'\\'+skin_type+'.jpg')
				self.cartoons.append(cartoon)
		
	
	def get_cartoons(self):
		return self.cartoons



	@staticmethod
	def convert_to_pil(img):
		"""
		Parameters
		----------
		img : cv2 array form of an image

		Returns
		-------
		pil_img : pil format of the read image
		"""
		cv2_img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
		pil_img = Image.fromarray(cv2_img)
		return pil_img
	
	@staticmethod
	def resize(img):
		"""
			Parameters
			----------
			img : cv2 array form of a read image

			Returns
			-------
			resized pil form of reaad image
		"""
		r = 206.0 / img.shape[1]
		height = int(img.shape[0] * r)
		if height  < 188:
			r = 198.0/img.shape[0]
			dim = (int(img.shape[1] * r), 198)
			resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
			return CartoonGenerator.convert_to_pil(resized)
		else:
			dim = (206, int(img.shape[0] * r))
			resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
			return CartoonGenerator.convert_to_pil(resized)
	
	
	


