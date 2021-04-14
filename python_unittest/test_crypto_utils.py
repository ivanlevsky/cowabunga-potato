import unittest
from python_common.crypto_utils import CryptoUtils


class TestCryptoUtils(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.bin_decoded_text = '胜多负少'
        cls.bin_encoded_text = b'e8839ce5a49ae8b49fe5b091'
        cls.url_decoded_text = '手动'
        cls.url_encoded_text = '%E6%89%8B%E5%8A%A8'
        cls.base64_decoded_text = '是各个'
        cls.base64_encoded_text = b'5piv5ZCE5Liq'
        cls.hash_type = 'md5'
        cls.hash_text = 'sai yo na na'
        cls.hash_salt_key = '时不利兮骓不逝'
        cls.hash_encoded_text = '296362f6cddd7032a20b9c4bc8c4b799'

    def test_bin_encode(self):
        self.assertEqual(self.bin_encoded_text, CryptoUtils.bin_encode(self.bin_decoded_text))

    def test_bin_decode(self):
        self.assertEqual(self.bin_decoded_text, CryptoUtils.bin_decode(self.bin_encoded_text))

    def test_url_encode(self):
        self.assertEqual(self.url_encoded_text, CryptoUtils.url_encode(self.url_decoded_text))

    def test_url_decode(self):
        self.assertEqual(self.url_decoded_text, CryptoUtils.url_decode(self.url_encoded_text))

    def test_base64_encode(self):
        self.assertEqual(self.base64_encoded_text, CryptoUtils.base64_encode(self.base64_decoded_text))

    def test_base64_decode(self):
        self.assertEqual(self.base64_decoded_text, CryptoUtils.base64_decode(self.base64_encoded_text))

    def test_hash_calculate(self):
        self.assertEqual(self.hash_encoded_text,
                         CryptoUtils.hash_calculate(self.hash_salt_key, self.hash_type, self.hash_text))

    def test_file_checksum(self):
        self.skipTest('test_file_checksum : check sum file not prepared')
        print(CryptoUtils.file_checksum(r'D:\file.txt','sha1',65535))


if __name__ == '__main__':
    unittest.main()
