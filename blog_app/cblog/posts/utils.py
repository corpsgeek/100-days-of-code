import os 
import secrets 
from PIL import Image 
from flask import current_app

def save_heroimg(image):
    #generate a random hex
    random_hex = secrets.token_hex(8)
    #split the iage file into the name and extension
    f_name, f_ext = os.path.splitext(image.filename)
    #a new filename for the image with a combo of the random hex + extension
    image_fn = random_hex + f_ext 
    #store the image in the post_image folder
    image_path = os.path.join(current_app.root_path, 'static/post_image', image_fn)
    #using pillow to change the image size for fast loading
    output_size = (600, 420)
    i = Image.open(image) 
    i.thumbnail(output_size)
    #save the image
    i.save(image_path)

    #returns the image file name when the function is called
    return image_fn
