"""
CLI script to generate cartoons for given directory of images or an image
"""
import click
import os, cv2
from cartoon_generator import CartoonGenerator

@click.command()
@click.argument('config', type=click.Path(exists=True), required=True)
@click.option('--image', '-i', help="Path of the image for which cartoon needs to be generated")
@click.option('--dir', '-d', help="Cartoons will be generated for all the images in this directory")
@click.option('--out-dir', '-o', help="Path of the output directory in which results need to be stored")
def app(config, image, dir, out_dir):
	"""
	creates a cartoon generator object for a given directory of images or an image

	Parameters
	----------
	config : str
		path of the config json file  which contains body types, skin types, paths to stencils
	img : str
		path to the image
	dir : str
		path to the directory of images
	out_dir : str/None
				path of the output directory in which all generated cartoons will be stored
			
	"""
	if dir:
		images = get_images(dir)
		for image in images:
			CartoonGenerator(image, out_dir, config)
	elif image:
		CartoonGenerator(image, out_dir, config)


def get_images(dir):
	"""
	gets all images from the given directory. If the given image is not readable by cv2
	library then cartoons for that image will not be created
	
	Paramters
	---------
	dir : str
		Path to the directory of images
	"""
	images = []
	for filename in os.listdir(dir):
		img = cv2.imread(os.path.join(dir,filename))
		if img is not None:
			images.append(os.path.join(dir,filename))
	return images

if __name__ == "__main__":
    app()
