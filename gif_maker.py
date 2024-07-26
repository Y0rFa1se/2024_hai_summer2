import os
from PIL import Image
from IPython.display import Image as Img

def generate_gif(path):
    img_list = os.listdir(path)
    img_list = [path + '/' + x for x in img_list]
    images = [Image.open(x) for x in img_list]
    
    im = images[0]
    im.save(path + '/../sample_images/out.gif', save_all=True, append_images=images[1:],loop=0xff, duration=200)
    
    return Img(url='out.gif')

gif = generate_gif('images')