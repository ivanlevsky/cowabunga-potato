from urllib import request,parse
from bs4 import BeautifulSoup  
import os,subprocess

OVERWRITE_DOWNLOAS=False
TRANSFER_7Z_TO_ZIP=True
UPDATE_ROMS_LIST=False
PACK_FILES=True
z7EXE="C:\\Program Files\\7-Zip\\7z.exe"
PREFIX="http://123.123.123.123/"
PLATFORM="Axxxx - 1200/"
##PREFIX="https://www.abc.com/files/"
##PLATFORM="Sxxx - PxxxSxxxxx/"

DOWNLOAD_PATH=''.join((os.getcwd(),"\\down\\"))

def get_all_links(url):  
    try:  
        response = request.urlopen(url)  
        html = response.read()  
    except request.URLError as e:  
        print(f"Error fetching the URL: {e}")  
        return None  
   
    soup = BeautifulSoup(html, 'html.parser')  
    links = ''  
    for link in soup.find_all('a'):
        if link.get('href').lower().endswith('.7z') or link.get('href').lower().endswith('.zip'):
            links += ''.join((parse.unquote(link.get('href')),'\n'))
    with open('roms_list.txt', 'w') as file:  
        file.write(links) 
  

def download(file):
    download_url=parse.quote(''.join((PLATFORM,file)))
    download_url=''.join((PREFIX,download_url))
    download_file=''.join((DOWNLOAD_PATH,file))
    zip_file_temp=''.join(('"',DOWNLOAD_PATH,'\\temp\\*.*'))
    zip_file_complete=os.path.exists(download_file.replace('.7z','.zip'))

    if (os.path.exists(download_file) or zip_file_complete) and not OVERWRITE_DOWNLOAS: 
        print(''.join(('skip download rom file:',download_url)))
    else:
        try:
            request.urlretrieve(download_url, download_file)
            print(''.join(('Downloading rom file:',download_url)))
        except OSError as e:
            print(f"'Downloading rom file %s faild：{e}" %(download_url))
            return None
        
    if TRANSFER_7Z_TO_ZIP and not zip_file_complete:
        extract_cmd=''.join(('"',z7EXE,'" e -o"',DOWNLOAD_PATH,'\\temp" "',download_file,'"'))
        del_cmd=''.join(('del "',download_file,'"'))
        del_cmd2=''.join(('del "',DOWNLOAD_PATH,'\\temp\\*.* " /Q'))
        zip_cmd=''.join(('"',z7EXE,'" a -tzip "',download_file.replace('.7z','.zip'),'" "',zip_file_temp,'"'))
        subprocess.getstatusoutput(extract_cmd)
        subprocess.getstatusoutput(del_cmd)
        subprocess.getstatusoutput(zip_cmd)
        subprocess.getstatusoutput(del_cmd2)

#update roms_list.txt
if UPDATE_ROMS_LIST:
    get_all_links(''.join((PREFIX,parse.quote(PLATFORM))))

#download roms in roms_list.txt
if not os.path.exists(DOWNLOAD_PATH):
    os.mkdir(DOWNLOAD_PATH)

with open('roms_list.txt', 'r') as file:  
    lines = [line.strip() for line in file.read().splitlines() if line]
    for ls in lines:
        download(ls)

#clean temp folder, rename download folder
if os.path.exists(''.join((DOWNLOAD_PATH,'temp'))):
    try:
        os.rmdir(''.join((DOWNLOAD_PATH,'temp')))
        print("delete temp folder success")
    except OSError as e:
        print(f"delete temp folder failed：{e}")

#pack files
if PACK_FILES:
    os.rename('down',PLATFORM)
    subprocess.getstatusoutput(''.join(('"',z7EXE,'" a "',os.getcwd(),'\\',PLATFORM.replace('/',''),'.7z" "',PLATFORM,'"')))
    subprocess.getstatusoutput(''.join(('del  /Q /S "',PLATFORM,'"')))
    os.rmdir(PLATFORM)





