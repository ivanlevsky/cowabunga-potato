from python_common.string_utils import split_string_by_numbers


# convert string bytes data to binary string list
def string_to_binary_string_list(string, split_no_ascii):
    bits_string = []

    for e in string:
        if split_no_ascii:
            for b in e.encode():
                bits_string.append(f'{b:08b}')
        else:
            bits_string.append(f'{ord(e):08b}')

    return bits_string


# covert binary string list to string
def binary_string_list_to_string(bits_string):
    string = ''
    for bs in bits_string:
        string = ''.join((string, chr(int(bs, base=2))))
    return string


# https://www.nayuki.io/page/creating-a-qr-code-step-by-step
# https://www.thonky.com/qr-code-tutorial/error-correction-coding
def qr_code_encode(text):
    # segment mode:Numeric, Alphanumeric, Byte, Kanji
    # error correction level: L, M, Q, H
    # version 18
    qr_version = 9
    mode_indicator = '0100'
    text_bit_list = []
    text_bit_string = ''
    for b in text:
        for tb in string_to_binary_string_list(b, True):
            text_bit_list.append(tb)
            text_bit_string = ''.join((text_bit_string, tb))
    if 1 <= qr_version <= 9:
        character_count_indicator = f'{text_bit_list.__len__():08b}'
    elif 10 <= qr_version <= 26:
        character_count_indicator = f'{text_bit_list.__len__():016b}'

    # require_bits_number = 313*8
    require_bits_number = 13 * 8
    text_bit_string = ''.join((mode_indicator, character_count_indicator, text_bit_string))
    if text_bit_string.__len__() < require_bits_number:
        text_bit_string = ''.join((text_bit_string, '0000'))

    first_pad = text_bit_string.__len__() + (text_bit_string.__len__() % 8)
    text_bit_string = text_bit_string.ljust(first_pad, '0')
    diff_number_multi, diff_number_mod = divmod(require_bits_number - text_bit_string.__len__(), 2)

    for i in range(diff_number_multi):
        text_bit_string = ''.join((text_bit_string, '1110110000010001'))
    if diff_number_mod == 1:
        text_bit_string = ''.join((text_bit_string, '11101100'))

    final_text_bit_string_list = split_string_by_numbers(text_bit_string, 8)
    print(final_text_bit_string_list.__len__())
    for e in final_text_bit_string_list:
        print(f'{int(e, base=2):02x}')


qr_code_encode('Hello, world! 123')

# qr_code_encode('你好质数我的个人文章你好质数我的个人文章你好质数我的个人文章你好质数我的个人文章你好质数我的个人文章你好'
#                '质数我的个人文章你好质数我的个人文章你好质数我的个人文章你好质数我的个人文章你好质数我的个人文章')
