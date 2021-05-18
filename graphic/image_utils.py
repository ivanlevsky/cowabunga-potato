import base64,sys,os
import glob
from python_common.global_param import GlobalParam
from PIL import Image


# imagePath = sys.path[0]+r'\image\\'
#
# def convertBase64ToImage(base64Value, image_path):
#     if not os.path.isdir(image_path):
#         os.mkdir(image_path)
#     with open(image_path, 'wb') as f:
#         f.write(base64.b64decode(base64Value))


# filepaths
fp_in = GlobalParam.get_gif_import() + '*.png'
fp_out = GlobalParam.get_gif_export() + 'out.gif'
#

# # https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html#gif
img, *imgs = [Image.open(f) for f in sorted(glob.glob(fp_in))]

img.save(fp=fp_out, format='GIF', append_images=imgs,
         save_all=True, duration=200, loop=0)