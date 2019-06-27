# cartoon-generator
A repository to generate cartoons from stencils and given swatch fabrics. The cartoon generator resizes the fabric to the size of stencil and imposes the stencil on the fabric. Since in the stencil only the shirt part is transparent it appears as if the cartoon is wearing a shirt of the given fabric.

## Directory Structure

1. 2D cartoons
   1. endo
   2. ecto
   3. meso
2. app.py
3. cartoon_generator.py
4. config.json

## Installation Procedure
### Prerequisites
Install Python : Before cloning this repo and running it make sure you have python setup on your system. Following           are the helpful link for setting up python.
1. [windows](https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-local-programming-environment-on-windows-10)
2. [Mac](https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-local-programming-environment-on-macos)
3. [Ubuntu](https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-local-programming-environment-on-ubuntu-16-04)
4. [Other linux systems](https://docs.python.org/3/using/unix.html)
### Installation
      git clone https://github.com/FashionDx/fdx-ml-color-extractor
      cd cartoon-generator
      cd src
      pip install -r requirements.txt

## Commands to run
 * For image
      
        python  app.py ./config.json -i PATH_TO_IMAGE
        
  * For directory of images
        
        python app.py ./config.json -d PATH_TO_DIRECTORY
  
  * To store all cartoons in a output directory
        
        python app.py ./config.json -d PATH_TO_DIRECTORY
 
## Working
* The given fabric image is resized to the dimensions of the stencil
* A blank image with the dimensions of the stencils is created.
* The fabric image is placed at the point where the and the topmost left most part of the cartoon in the stencil meets. This point is hardcoded in the code and all stencils start at have the same structure.
* The stencil is super imposed on the above created image.
* Thus it looks like the cartoon in the stencil is wearing a shirt of the given fabric.
* cv2 library is used for resizing and PIL library is used for super imposing one image on top of another
