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
class ImageUtils():
    # https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html
    @staticmethod
    def combine_images_to_gif(images_path, image_format, gif_path):
        sorted_base_path = images_path
        sorted_images_list = []
        images_path += ''.join(('*.', image_format))
        images_list = []
        for f in glob.glob(images_path):
            images_list.append(f[f.rfind('\\'):].replace('\\', '').replace('.png',''))

        for ff in sorted(images_list,key=int):
            sorted_images_list.append(''.join((sorted_base_path, ff, '.', image_format)))

        img, *imgs = [Image.open(f) for f in sorted_images_list]
        img.save(fp=gif_path, format='GIF', append_images=imgs,
                 save_all=True, duration=100, loop=0,include_color_table=True)

    @staticmethod
    def split_gif_to_images(gif_path):
        image_object = Image.open(gif_path)
        if image_object.is_animated:
            for frame in range(0,image_object.n_frames):
                image_object.seek(frame)
                image_object.save(fp=GlobalParam.get_gif_import() + str(frame) +'.png', format='PNG')


# fp_out = GlobalParam.get_gif_export() + 'out.gif'
# split_gif_to_images(fp_out)

# fp_in = GlobalParam.get_gif_import()
# fp_out = GlobalParam.get_gif_export() + 'out.gif'
# ImageUtils.combine_images_to_gif(fp_in, 'png', fp_out)