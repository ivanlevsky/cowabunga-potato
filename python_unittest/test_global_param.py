import os
import unittest
from python_common.global_param import GlobalParam


class TestGlobalParam(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.project_path = os.path.dirname(os.getcwd())
        cls.test_image_path = cls.project_path + '\\test image\\'
        cls.test_video_path = cls.project_path + '\\test video\\'
        cls.test_file_path = cls.project_path + '\\test file\\'
        cls.image_input = cls.project_path + '\\test image\\pic.png'
        cls.image_output = cls.project_path + '\\test image\\picout.png'
        cls.character_output = cls.project_path + '\\test image\\char\\'
        cls.sentence_output = cls.project_path + '\\test image\sentence.png'
        cls.system_font_path = 'C:\\windows\\fonts\\simkai.ttf'
        cls.video_input = cls.project_path + '\\test video\\video1.mp4'
        cls.video_output = cls.project_path + '\\test video\\videoout.mp4'
        cls.tesseract_path = 'D:\\develop\\Tesseract-OCR\\tesseract'
        cls.face_detect_face_xml = cls.project_path + '\\test file\datasets\opencv\haarcascade_frontalface_alt.xml'
        cls.face_detect_eyes_xml = cls.project_path + '\\test file\datasets\opencv\haarcascade_eye_tree_eyeglasses.xml'
        cls.aapt_path = cls.project_path + '\\test file\\appium\\aapt-arm-pie'
        cls.android_apk_list = cls.project_path + '\\test file\\appium\\android_apk_list.txt'
        cls.appium_screenshot_path = cls.project_path + '\\test image\\appium_screenshot.png'
        cls.appium_screenrecord_path = cls.project_path + '\\test video\\appium_screenrecord.mp4'
        cls.qr_code_image_path = cls.project_path + '\\test image\\qr_code.png'
        cls.ml_ch2_housing_data = cls.project_path + '\\test file\\datasets\\housing'
        cls.ml_ch2_housing_image = cls.project_path + '\\test image\\machine learning images\\end_to_end_project\\california.png'
        cls.ml_ch3_sklearn_data_home = cls.project_path + '\\test file\\datasets\\scikit_learn_data'
        cls.ml_numpy_array_save_path = cls.project_path + '\\test file\\datasets\\numpy_array_data\\save_data'
        cls.ml_matplotlib_figure_save_path = cls.project_path + '\\test file\\datasets\\matplotlib_save_figure'
        cls.chrome_driver_path = cls.project_path + '\\test file\\webdriver\\chromedriver.exe'
        cls.edge_driver_path = cls.project_path + '\\test file\\webdriver\\MicrosoftWebDriver.exe'
        cls.ie_driver_path = cls.project_path + '\\test file\\webdriver\\IEDriverServer.exe'
        cls.chromium_path = 'D:\\Program Files\\chromium\\chrome.exe'
        cls.mariadb_url = 'jdbc:mysql://172.21.48.116:3306/mysqltest'
        cls.mariadb_user = 'debianmysql'
        cls.mariadb_password = 'debianmysqlpasswd'
        cls.pgsql_url = 'jdbc:postgresql://172.21.48.116:5432/pgtest'
        cls.pgsql_user = 'debianpgsql'
        cls.pgsql_password = 'debianpgsqlpasswd'
        cls.excel_datasets = cls.project_path + '\\test file\\datasets\\test_excel.xlsx'
        cls.csv_datasets = cls.project_path + '\\test file\\datasets\\test_csv.csv'
        cls.unittest_reports = cls.project_path + '\\test file\\test reports\\unittest\\'
        cls.pytest_reports = cls.project_path + '\\test file\\test reports\\pytest\\'

    def test_get_test_image_path(self):
        self.assertEqual(self.test_image_path, GlobalParam.get_test_image_path())

    def test_get_test_video_path(self):
        self.assertEqual(self.test_video_path, GlobalParam.get_test_video_path())

    def test_get_test_file_path(self):
        self.assertEqual(self.test_file_path, GlobalParam.get_test_file_path())

    def test_get_system_font_path(self):
        self.assertEqual(self.system_font_path, GlobalParam.get_system_font_path())

    def test_get_tesseract_path(self):
        self.assertEqual(self.tesseract_path, GlobalParam.get_tesseract_path())

    def test_get_image_input(self):
        self.assertEqual(self.image_input, GlobalParam.get_image_input())

    def test_get_image_output(self):
        self.assertEqual(self.image_output, GlobalParam.get_image_output())

    def test_get_character_output(self):
        self.assertEqual(self.character_output, GlobalParam.get_character_output())

    def test_get_sentence_output(self):
        self.assertEqual(self.sentence_output, GlobalParam.get_sentence_output())

    def test_get_video_input(self):
        self.assertEqual(self.video_input, GlobalParam.get_video_input())

    def test_get_video_output(self):
        self.assertEqual(self.video_output, GlobalParam.get_video_output())

    def test_get_face_detect_face_xml(self):
        self.assertEqual(self.face_detect_face_xml, GlobalParam.get_face_detect_face_xml())

    def test_get_face_detect_eyes_xml(self):
        self.assertEqual(self.face_detect_eyes_xml, GlobalParam.get_face_detect_eyes_xml())

    def test_get_aapt_path(self):
        self.assertEqual(self.aapt_path, GlobalParam.get_aapt_path())

    def test_get_android_apk_list(self):
        self.assertEqual(self.android_apk_list, GlobalParam.get_android_apk_list())

    def test_get_appium_screenshot_path(self):
        self.assertEqual(self.appium_screenshot_path, GlobalParam.get_appium_screenshot_path())

    def test_get_appium_screenrecord_path(self):
        self.assertEqual(self.appium_screenrecord_path, GlobalParam.get_appium_screenrecord_path())

    def test_get_qr_code_image_path(self):
        self.assertEqual(self.qr_code_image_path, GlobalParam.get_qr_code_image_path())

    def test_get_ml_ch2_housing_data(self):
        self.assertEqual(self.ml_ch2_housing_data, GlobalParam.get_ml_ch2_housing_data())

    def test_get_ml_ch2_housing_image(self):
        self.assertEqual(self.ml_ch2_housing_image, GlobalParam.get_ml_ch2_housing_image())

    def test_get_ml_ch3_sklearn_data_home(self):
        self.assertEqual(self.ml_ch3_sklearn_data_home, GlobalParam.get_ml_ch3_sklearn_data_home())

    def test_get_ml_numpy_array_save_path(self):
        self.assertEqual(self.ml_numpy_array_save_path, GlobalParam.get_ml_numpy_array_save_path())

    def test_get_ml_matplotlib_figure_save_path(self):
        self.assertEqual(self.ml_matplotlib_figure_save_path, GlobalParam.get_ml_matplotlib_figure_save_path())

    def test_get_chrome_driver_path(self):
        self.assertEqual(self.chrome_driver_path, GlobalParam.get_chrome_driver_path())

    def test_get_ie_driver_path(self):
        self.assertEqual(self.ie_driver_path, GlobalParam.get_ie_driver_path())

    def test_get_edge_driver_path(self):
        self.assertEqual(self.edge_driver_path, GlobalParam.get_edge_driver_path())

    def test_get_chromium_path(self):
        self.assertEqual(self.chromium_path, GlobalParam.get_chromium_path())

    def test_get_mariadb_url(self):
        self.assertEqual(self.mariadb_url, GlobalParam.get_mariadb_url())

    def test_get_mariadb_user(self):
        self.assertEqual(self.mariadb_user, GlobalParam.get_mariadb_user())

    def test_get_mariadb_password(self):
        self.assertEqual(self.mariadb_password, GlobalParam.get_mariadb_password())

    def test_get_pgsql_url(self):
        self.assertEqual(self.pgsql_url, GlobalParam.get_pgsql_url())

    def test_get_pgsql_user(self):
        self.assertEqual(self.pgsql_user, GlobalParam.get_pgsql_user())

    def test_get_pgsql_password(self):
        self.assertEqual(self.pgsql_password, GlobalParam.get_pgsql_password())

    def test_get_excel_datasets(self):
        self.assertEqual(self.excel_datasets, GlobalParam.get_excel_datasets())

    def test_get_csv_datasets(self):
        self.assertEqual(self.csv_datasets, GlobalParam.get_csv_datasets())

    def test_get_unittest_reports(self):
        self.assertEqual(self.unittest_reports, GlobalParam.get_unittest_reports())

    def test_get_pytest_reports(self):
        self.assertEqual(self.pytest_reports, GlobalParam.get_pytest_reports())

if __name__ == '__main__':
    unittest.main()
