import pytest, os
from python_common.crypto_utils import CryptoUtils


class TestCryptoUtils:
    bin_decoded_text = ''
    bin_encoded_text = ''
    url_decoded_text = ''
    url_encoded_text = ''
    base64_decoded_text = ''
    base64_encoded_text = ''
    hash_type = ''
    hash_text = ''
    hash_salt_key = ''
    hash_encoded_text = ''
    filepath = ''

    @pytest.fixture()
    def setup_params(self):
        self.bin_decoded_text = '胜多负少'
        self.bin_encoded_text = b'e8839ce5a49ae8b49fe5b091'
        self.url_decoded_text = '手动'
        self.url_encoded_text = '%E6%89%8B%E5%8A%A8'
        self.base64_decoded_text = '是各个'
        self.base64_encoded_text = b'5piv5ZCE5Liq'
        self.hash_type = 'md5'
        self.hash_text = 'sai yo na na'
        self.hash_salt_key = '时不利兮骓不逝'
        self.hash_encoded_text = '296362f6cddd7032a20b9c4bc8c4b799'
        self.filepath = os.path.dirname(os.getcwd()) + '\\LICENSE'

    def test_bin_encode(self, setup_params):
        assert self.bin_encoded_text == CryptoUtils.bin_encode(self.bin_decoded_text)

    def test_bin_decode(self, setup_params):
        assert self.bin_decoded_text == CryptoUtils.bin_decode(self.bin_encoded_text)

    def test_url_encode(self, setup_params):
        assert self.url_encoded_text == CryptoUtils.url_encode(self.url_decoded_text)

    def test_url_decode(self, setup_params):
        assert self.url_decoded_text == CryptoUtils.url_decode(self.url_encoded_text)

    def test_base64_encode(self, setup_params):
        assert self.base64_encoded_text == CryptoUtils.base64_encode(self.base64_decoded_text)

    def test_base64_decode(self, setup_params):
        assert self.base64_decoded_text == CryptoUtils.base64_decode(self.base64_encoded_text)

    def test_hash_calculate(self, setup_params):
        assert self.hash_encoded_text == CryptoUtils.hash_calculate(self.hash_salt_key, self.hash_type, self.hash_text)

    def test_file_checksum(self, setup_params):
        assert 'B42A17A0F83B737FAF403CAA6B2641AF' == CryptoUtils.file_checksum(self.filepath,'md5',65535)
        assert '29D1871D6CD6CBDA3D35AB3A1448E58822FA1D55' == CryptoUtils.file_checksum(self.filepath,'sha1',65535)
        assert '9F2C16E91B305CC547E159DEDC4E34BDE312B120CB2749E418739C01774156FE' == CryptoUtils.file_checksum(self.filepath,'sha256',65535)
        assert '7A450B78' == CryptoUtils.file_checksum(self.filepath,'crc32',65535)


if __name__ == '__main__':
    pytest.main(['-s', 'test_crypto_utils.py'])