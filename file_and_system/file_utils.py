import base64
import zipfile
import os


def write_string_to_file(file, text, encode):
    with open(file, 'w', encoding=encode) as f:
        f.write(str(text))


def write_binary_to_file(file, binary):
    with open(file, 'wb') as f:
        f.write(base64.b64decode(binary))


def read_file(file, encode):
    with open(file, 'r', encoding=encode) as f:
        text = f.read()
    return text


def calculate_my_all_code_lines():
    return ''


# this method too slow for big folder, need optimise
def zip_folder(folder, zip_file):
    root_dir = os.path.basename(folder)
    # zip_file_dir = os.path.basename(zip_file)
    # zip_file = zip_file.replace(zip_file_dir, ''.join((str(date.today()).replace('-',''), '_', zip_file_dir)))
    zipf = zipfile.ZipFile(zip_file, 'w', zipfile.ZIP_DEFLATED)
    for root, dirs, files in os.walk(folder):
        for file in files:
            file_path = os.path.join(root, file)
            parent_path = os.path.relpath(file_path, folder)
            arc_name = os.path.join(root_dir, parent_path)
            zipf.write(file_path, arc_name)
    zipf.close()

