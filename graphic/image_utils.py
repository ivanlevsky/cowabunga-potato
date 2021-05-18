import base64,sys,os
import glob
from python_common.global_param import GlobalParam
from PIL import Image, GifImagePlugin


# imagePath = sys.path[0]+r'\image\\'
#
# def convertBase64ToImage(base64Value, image_path):
#     if not os.path.isdir(image_path):
#         os.mkdir(image_path)
#     with open(image_path, 'wb') as f:
#         f.write(base64.b64decode(base64Value))


# https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html
def combine_images_to_gif(images_path, gif_path):
    img, *imgs = [Image.open(f) for f in sorted(glob.glob(images_path))]
    img.save(fp=gif_path, format='GIF', append_images=imgs,
             save_all=True, duration=100, loop=0,include_color_table=True)


def split_gif_to_images(gif_path):
    imageObject = Image.open(gif_path)
    if imageObject.is_animated:
        for frame in range(0,imageObject.n_frames):
            imageObject.seek(frame)
            imageObject.save(fp=GlobalParam.get_gif_import() + str(frame) +'-.png', format='PNG')

# fp_out = GlobalParam.get_gif_export() + 'out.gif'
# split_gif_to_images(fp_out)

fp_in = GlobalParam.get_gif_import() + '*.png'
fp_out = GlobalParam.get_gif_export() + 'out.gif'
combine_images_to_gif(fp_in, fp_out)