from urllib import parse
import binascii, base64, hashlib, zlib


# byte encode and decode
def bin_encode(string):
    return binascii.b2a_hex(string.encode())


def bin_decode(byte):
    return binascii.a2b_hex(byte).decode()


# used for web, eg. web page's url characters, chinese characters
def url_encode(string):
    return parse.quote(string)


def url_decode(string):
    return parse.unquote(string)


# base64 encode and decode
def base64_encode(string):
    return base64.b64encode(string.encode())


def base64_decode(byte):
    return base64.b64decode(byte).decode()


def hash_calculate(key, hash_type, string):
    """
    hash calculate, use key add security, support md5, sha1, sha256...
    warning: don't use simple key!! use complex key like number+notation+uppercase or lowercase ,better to combine
    chinese or other non-english characters
    """
    if hash_type == 'md5':
        ht = hashlib.md5(key.encode('utf-8'))
    elif hash_type == 'sha1':
        ht = hashlib.sha1(key.encode('utf-8'))
    elif hash_type == 'sha256':
        ht = hashlib.sha256(key.encode('utf-8'))
    else:
        return None
    ht.update(string.encode('utf-8'))
    return ht.hexdigest()


'''
argon2
'''


# file checksum using md5, sha1, sha256, crc32...
def file_checksum(file, checksum_type, buffersize):
    if checksum_type == 'md5':
        hash_type = hashlib.md5()
    elif checksum_type == 'sha1':
        hash_type = hashlib.sha1()
    elif checksum_type == 'sha256':
        hash_type = hashlib.sha256()
    else:
        return None

    crc_value = 0
    with open(file, 'rb') as hashfile:
        if checksum_type == 'crc32':
            for buffer in iter(lambda: hashfile.read(buffersize), b''):
                crc_value = zlib.crc32(buffer, crc_value)
            checksum = format(crc_value & 0xFFFFFFFF, '08x')
        else:
            for buffer in iter(lambda: hashfile.read(buffersize), b''):
                hash_type.update(buffer)
            checksum = hash_type.hexdigest()

    return checksum


# print(url_decode(url_encode('手动')))
# print(bin_decode(bin_encode('胜多负少')))
# print(base64_decode(base64_encode('是各个')))
# print(hash_calculate('时不利兮骓不逝','md5','sai yo na na'))
# print(file_checksum(r'D:\file.txt','sha1',65535))
